class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        for word in strs:
            word_key = [0] * 26
            for ch in word:
                word_key[ord(ch) - ord('a')] += 1 
            
            res[tuple(word_key)].append(word)
        
        return list(res.values())