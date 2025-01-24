import sys
from pathlib import Path
from shutil import copyfile

output_folder: Path

def read_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            read_folder(el)
        else:
            copy_file(el)

def copy_file(file: Path) -> None:
    ext = file.suffix if file.suffix else "no_extension"
    new_path = output_folder / ext
    new_path.mkdir(exist_ok=True, parents=True)
    destination = new_path / file.name
    copyfile(file, destination)
    print(f"Copied: {file} -> {destination}")

def main():
    global output_folder
    if len(sys.argv) > 1:
        try:
            source = Path(sys.argv[1])
            if not source.exists() or not source.is_dir():
                print(f"Error: Source path '{source}' does not exist or is not a directory.")
                return
            output = sys.argv[2] if len(sys.argv) > 2 else "dist/"
            output_folder = Path(output)
            output_folder.mkdir(exist_ok=True) 

            read_folder(source)
            print(f"All files have been processed and copied to '{output_folder}'.")
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"Usage: python script.py <source_folder> [output_folder]")

if __name__ == "__main__":
    main()
