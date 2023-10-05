class Solution: 
    def select(self, arr, i):
        # code here
        pass
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
