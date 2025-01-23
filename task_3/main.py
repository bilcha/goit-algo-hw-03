def move_disk(towers, from_pole, to_pole):
    disk = towers[from_pole].pop()
    towers[to_pole].append(disk)
    print(f"Перемістити диск з {from_pole} на {to_pole}: {disk}")
    print(f"Проміжний стан: {towers}")


def solve_hanoi(n, from_pole, to_pole, aux_pole, towers):
    if n == 1:
        move_disk(towers, from_pole, to_pole)
    else:
        solve_hanoi(n - 1, from_pole, aux_pole, to_pole, towers)
        move_disk(towers, from_pole, to_pole)
        solve_hanoi(n - 1, aux_pole, to_pole, from_pole, towers)


def init_hanoi(n):
    towers = {
        'A': list(range(n, 0, -1)),
        'B': [], 
        'C': []  
    }
    
    print(f"Початковий стан: {towers}")
    solve_hanoi(n, 'A', 'C', 'B', towers)
    print(f"Кінцевий стан: {towers}")


n = int(input("Введіть кількість дисків: "))
init_hanoi(n)
