class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for x in strs:
            hg = [0] * 26
            for c in x:
                hg[ord(c) - ord('a')] += 1
            groups[tuple(hg)].append(x)
        return list(groups.values())
        