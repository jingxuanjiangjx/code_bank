'''
data:2020/4/14
auther:jx
'''

def matrixSearch(matrix, target):
    if not matrix:
        return False
    row = 0
    col = len(matrix[0]) - 1
    found = False
    while row < len(matrix) and col >= 0:
        # print(matrix[row][col])
        if matrix[row][col] == target:
            found=True
            break
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return found

if __name__=='__main__':
    matrix = [
        [1, 2, 4, 5],
        [10, 14, 17, 19],
        [21, 22, 24, 25],
    ]
    target = 18
    res=matrixSearch(matrix, target)
    print(res)