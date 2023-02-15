class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        result = ''
        if columnNumber > 26:
            result = self.convertToTitle((columnNumber - 1)// 26)
        result += chr(65 + (columnNumber - 1) % 26)
        return result