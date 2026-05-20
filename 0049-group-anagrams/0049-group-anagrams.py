class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for words in strs:
            key="".join(sorted(words))
            if key not in groups:
                groups[key]=[]
            groups[key].append(words)

        return list(groups.values())

