class Solution:
    def select(self,arr,i):
        min = i
        length= len(arr)
        for _ in range(i,length):
            min= _

        return min
    def selectionSort(self,arr,n):
        for ind in range(n-1):
            selected = self.select(arr,ind+1)
            if arr[ind] > arr[selected]:
                arr[ind], arr[selected] = arr[selected],arr[ind]
        return arr