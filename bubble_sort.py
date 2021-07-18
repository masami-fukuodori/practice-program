from array import array

def sort(arrays):
    length = len(arrays)
    for i in range(0, length-1):
        isSwap = False
        for j in range(0, length-i-1):
            if arrays[j] > arrays[j+1]:
                flag = arrays[j]
                arrays[j] = arrays[j+1]
                arrays[j+1] = flag
                isSwap = True
        if isSwap == False:
            break

def main():
    scores = array('i')
    scores = array('i', [60,50,95,80,70])

    sort(scores)

    for score in scores:
        print(score, ',', end='')

if __name__ == '__main__':
    print('bubble_sort')
    main()