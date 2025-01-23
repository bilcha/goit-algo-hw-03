import sys
from pathlib import Path
from shutil import copyfile

path_arguments = sys.argv
output_folder: Path 


def read_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            read_folder(el)
        else:
            copy_file(el)


def copy_file(file: Path) -> None:
    ext = file.suffix
    new_path = output_folder / ext
    new_path.mkdir(exist_ok=True, parents=True)
    copyfile(file, new_path / file.name)


if len(path_arguments) > 1:
  try:
    source = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else "dist/"
    output_folder = Path(output)
    read_folder(Path(source))
  except FileNotFoundError:
    print(f"Wasn't able to find a file")

else: print(f"Please provide path arguments")
