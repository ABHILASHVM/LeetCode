class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        save=[]
        k,l=len(matrix),len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==min(matrix[i]):
                    k=0
                    while k<len(matrix):
                        save.append(matrix[k][j])
                        k+=1
                    if max(save)==matrix[i][j]:
                        return [matrix[i][j]]
                    save=[]
                    # if matrix[i][j]==max(matrix[i][i]):
                    #     return matrix[i][j]
                    # save.append(matrix[i][j])
                else:
                    continue
        