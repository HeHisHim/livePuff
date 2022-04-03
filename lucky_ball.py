def kaigenhao(value, precision):
    calc_value = value if value > 1 else 1 / value
    left, right = 0, calc_value
    while right - left > precision:
        mid = (left + right) / 2
        if mid * mid == calc_value:
            break
        elif mid * mid < calc_value:
            left, right = mid, right
        else:
            left, right = left, mid
    return (left + right) / 2 if value > 1 else 2 / (left + right)


if "__main__" == __name__:
    print(kaigenhao(10, 0.1))