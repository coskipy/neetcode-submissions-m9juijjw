class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hg = defaultdict(int)
        for x in nums:
            hg[x] += 1
        print(hg.items())

        out = []

        while k > 0:
            max_key = max(hg.items(), key=lambda item: item[1])[0] # get key with max value
            out.append(max_key)
            hg.pop(max_key)
            k -= 1 # remove to get new max for k
        
        return out
    