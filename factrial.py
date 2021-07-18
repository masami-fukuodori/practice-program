def factrial(n):
    if n == 1:
        return 1
    else:
        return factrial(n-1)*n

def main():
    n = 5
    fac = factrial(n)
    print("The factrial of 5 is :",fac)

if __name__ == '__main__':
    print('factrial')
    main()