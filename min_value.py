from array import array

def min(arrays):
    minIndex = 0;
    length = len(arrays)-1
    for j in range(0, length):
        if (arrays[minIndex] > arrays[j]):
            minIndex = j
    return arrays[minIndex]

def main():
    scores = array('i')
    scores = array('i', [60,50,95,80,70])
    minValue = min(scores)
    print('Min Value = ', minValue)

if __name__ == '__main__':
    print('min_value')
    main() 