class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prev_table = {}
        for word in strs:
            s_word = "".join(sorted(word))
            if s_word in prev_table:
                prev_table[s_word].append(word)
            else:
                prev_table[s_word] = [word]
        return list(prev_table.values())