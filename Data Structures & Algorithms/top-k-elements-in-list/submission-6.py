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
        for i in range(len(buckets) - 1, 0, -1):
            out.extend(buckets[i])
            if len(out) == k:
                return out[:k]