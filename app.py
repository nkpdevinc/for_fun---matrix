'''
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/?envType=featured-list&envId=challenges-for-new-users

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

'''
def kWeakestRows(mat :list, k :int) -> list: 
    # Create a list of tuples where each tuple contains the index of a row and the number of soldiers in that row
    rows = [(i, sum(row)) for i, row in enumerate(mat)]
    #rows_sort = [(i, sum(row)) for i, row in enumerate(mat)]
    # Sort the list of tuples by the number of soldiers in each row, then by the index of the row
    rows_sort = sorted(rows, key=lambda x: (x[1], x))
    # Return the indices of the k weakest row
    print('Input: mat = ')
    for m in mat:
        print(m,',')
    print('k = ', k)
    print(f'Output: {[row[0] for row in rows_sort[:k]]}')
    print('Explanation: ')
    for i in rows:
        print(i)
   
    return 

mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1],[1,1,0,0,0,0,0]]
k =9

if __name__ == '__main__':
    kWeakestRows(mat, k)  # Output: [2, 0, 3, 5, 1, 4]