# Top K Freq Elements
# guve ab ubteger array nums and an inger k, return k, most freq elements within the array
from collections import Counter
import heapq

class Solution():
    # My first solution 
    def topKFrequent(self, nums: list[int], k : int) -> list[int]:
        res = []
        cnter = {}
        for num in nums: 
            if num in cnter:
                cnter[num] += 1
            else:
                cnter[num] = 1
        mostFreq = list(cnter.items())[0][1]
        mostFreqKey = list(cnter.items())[0][0]
        for i in range(k):
            for num, value in list(cnter.items()):
                if mostFreq <= value:
                    mostFreq = value
                    mostFreqKey = num
            res.append(mostFreqKey)
            cnter.pop(mostFreqKey)
            mostFreq =  list(cnter.items())[0][1] if (len(cnter) != 0) else 0

        return res
    
    # Bucket Sort
    def topKFrequentIdeal(self, nums: list[int], k: int) -> list[int]:
        res = []
        counter = Counter(nums)
        bucket = [[] for x in range(len(nums) + 1)]
        for num in counter:
            bucket[counter[num]].append(num)
        for i in range(len(bucket) - 1, 0, -1):
            
            b = bucket[i]
            if len(b) == 0:
                continue
            for num in b:
                res.append(num)
                if len(res) == k:
                    return res
    
    # HEAP
    def topKFrequentHEAP(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            if len(heap) < k:
                heapq.heappush(heap, (count[num], num))
        #print(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

sol = Solution()
print(sol.topKFrequentHEAP([1,2,2,3,3,3], 2))
print(sol.topKFrequentHEAP([7,7], 1))
print(sol.topKFrequentHEAP([1,1,1,2,2,3], 2))