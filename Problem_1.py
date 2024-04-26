'''
Time Complexity - O(nlogm)
Space Complexity -O(m)

Works on Leetcode
'''
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        cntMap = {}
        #store indices of each character in source string { 'c' -> [3,4...]}
        for i in range(len(source)):
            if source[i] not in cntMap:               
                cntMap[source[i]] = []
            posList = cntMap.get(source[i])
            posList.append(i)
        i, j = 0, 0
        count = 1
        while j < len(target):
            #return -1 if character in target string not in source
            if target[j] not in cntMap:
                return -1
            else:
                #use binary search to get next index of character in source
                pos = self.binarySearch(i, cntMap.get(target[j]))
                if pos == -1:
                #if current point on source is beyond the last occurrence of a char in target,
                #reset the pointer and increase subsequence count as we start a new sequence here
                    posList = cntMap.get(target[j])
                    i = posList[0]
                    count+=1
                else:
                    i = pos
                i+=1
                j+=1
        return count

    def binarySearch(self, tgt, arr):
        #slightly modified BS, check value at mid-1 is smaller than target then only return the target else move left
        if tgt>arr[-1]:
            return  -1
        low, high = 0, len(arr)-1
        while low<=high:
            mid = low + (high-low)//2
            if arr[mid] == tgt:
                if arr[mid-1] < tgt:
                    return arr[mid]
                else:
                    high = mid - 1
            elif tgt > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return arr[low]
            
                                