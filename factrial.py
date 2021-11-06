def factrial(n):
    if n == 1:
        return 1
    else:
        return factrial(n-1)*n

def main(n):
    fac = factrial(n)
    print(f"The factrial of {n} is :",fac)

if __name__ == '__main__':
    print('factrial')
    print('階乗計算：再帰関数')
    n = int(input('数字を入力'))
    main(n)