def printf(num):
    max_num = 2 * num - 1
    l = list(range(1, num)) + list(range(num, 0, -1))
    for _ in l:
        x = 2 * _ - 1
        space = (max_num - x) // 2
        print(space * " " + "*" * x + space * " ")

if "__main__" == __name__:
    printf(8)