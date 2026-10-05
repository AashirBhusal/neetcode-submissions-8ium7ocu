class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix = []

        for i in range(rows + 1):
            row = []

            for c in range(cols + 1):
                row.append(0)

            self.prefix.append(row)

        for r in range(rows):
            for c in range(cols):
                self.prefix[r+1][c+1] = ( self.prefix[r][c+1] + self.prefix[r+1][c]-
                self.prefix[r][c] + matrix[r][c]
                )

        print(self.prefix)
                


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_prefix = self.prefix[row2 + 1][col2 + 1]
        top_prefix = self.prefix[row1][col2 + 1]
        left_prefix = self.prefix[row2 + 1][col1]
        current_prefix = self.prefix[row1][col1]

        return total_prefix - top_prefix - left_prefix + current_prefix
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)