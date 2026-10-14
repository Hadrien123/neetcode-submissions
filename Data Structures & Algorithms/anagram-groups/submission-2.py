class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #idea: make dict for first string 
        #following strings: add to first array if anagram to first string
        #make new dict if not anagram to first string, etc... 
        groups = defaultdict(list)
        for s in strs: 
            count = [0] * 26
            for c in s: 
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())
        