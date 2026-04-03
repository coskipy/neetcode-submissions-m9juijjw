class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hg = defaultdict(int)
        for x in nums:
            hg[x] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in hg.items():
            buckets[freq].append(num)
        
        # print(buckets[::-1])
        out = []
        for i in buckets[::-1]:
            if i != []:
                out.extend(i)

        return out[:k]