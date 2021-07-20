def add_all(a, b):
    if a == b:
        return a
    else:
        return add_all(a, b-1)+b
        
def main():
    a, b = 0, 3
    sum = add_all(a,b)
    print(f'sum is {sum}')

if __name__ == '__main__':
    print('sum')
    main()