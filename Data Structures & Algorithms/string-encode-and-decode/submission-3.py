class Solution:

    def encode(self, strs: List[str]) -> str:
        out_str = ""
        for s in strs:
            out_str += f"{len(s)}#{s}"
        return out_str

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            size = 0
            while s[i] != "#":
                size = size * 10 + int(s[i])
                i += 1
            i += 1
            out.append(s[i:i+size])
            i += size
        return out
            