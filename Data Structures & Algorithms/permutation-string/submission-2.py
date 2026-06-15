from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        hist_s1 = Counter(s1)
        hist_s2 = Counter(s2[l:r])

        while r <= len(s2):
            print(hist_s1, hist_s2, hist_s1.items() == hist_s2.items())
            if hist_s1.items() == hist_s2.items():
                return True

            else:
                hist_s2[s2[l]] -= 1 
                if hist_s2[s2[l]] == 0:
                    hist_s2.pop(s2[l])

                if r < len(s2):
                    hist_s2[s2[r]] += 1
            
            l += 1
            r += 1
        
        return False