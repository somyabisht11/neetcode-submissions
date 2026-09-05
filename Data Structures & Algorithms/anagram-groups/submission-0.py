class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = {}
        for i in strs:
           key = tuple(sorted(i))
           if key not in new:
            new[key] = [i]
           else:
                new[key].append(i)
        return list(new.values())



                