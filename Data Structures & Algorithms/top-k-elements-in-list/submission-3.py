class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        answer = []
        freq = dict(sorted(count.items(),key=lambda item: item[1], reverse=True))
        
        for i, (key, value) in enumerate(freq.items()):
            if i in range(k):
                answer.append(key)
        return answer




        