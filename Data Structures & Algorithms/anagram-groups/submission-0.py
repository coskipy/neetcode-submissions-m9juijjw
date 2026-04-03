class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hg = {}
        for x in strs:
            strsum = 0
            for c in x:
                strsum += ord(c) * ord(c) # square to avoid different strings giving same sum
            if strsum in hg:
                print(strsum, hg, x)
                hg[strsum].append(x)
            else:
                hg.update({strsum: [x]})

        return list(hg.values())
        