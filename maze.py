import sys

maze = [
    [2,2,2,2,2,2,2],
    [2,0,0,0,0,0,2],
    [2,2,2,0,2,0,2],
    [2,0,2,0,0,2,2],
    [2,2,0,2,0,2,2],
    [2,0,0,0,0,0,2],
    [2,2,2,2,2,2,2],
]

startI = 1
startJ = 1
endI = 5
endJ = 5
success = 0

def image():
    for i in range(0,7):
        for j in range(0,7):
            if (maze[i][j] == 2):
                print('# ',end='')
            elif (maze[i][j] == 1):
                print('- ',end='')
            else:
                print('* ',end='')
        print('')

def visit(i,j):
    global success
    maze[i][j] = 1
    if (i == endI and j == endJ):
        success = 1
    if (success != 1 and maze[i][j + 1] == 0):
        print(i,j)
        image()
        visit(i,j+1)
    if (success != 1 and maze[i + 1][j] == 0):
        print(i,j)
        image()
        visit(i+1,j)
    if (success != 1 and maze[i][j - 1] == 0):
        print(i,j)
        image()
        visit(i,j-1)
    if (success != 1 and maze[i - 1][j] == 0):
        print(i,j)
        image()
        visit(i-1,j)
    if (success != 1):
        print(i,j)
        image()
        maze[i][j] = 0
    return success

def main():
    print('Maze :')
    for i in range(0,7):
        for j in range(0,7):
            if (maze[i][j] == 2):
                print("# ",end="")
            else:
                print('* ',end='')
        print('')

    if (visit(startI, startJ) == 0):
        print("NO exit found")
    else:
        print('Maze Path :')
        #ここからが迷路のアルゴリズム
        for i in range(0,7):
            for j in range(0,7):
                if (maze[i][j] == 2):
                    print('# ',end='')
                elif (maze[i][j] == 1):
                    print('- ',end='')
                else:
                    print('* ',end='')
            print('')

if __name__ == '__main__':
    main()
