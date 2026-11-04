class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += s + "\n"
        return out

    def decode(self, s: str) -> List[str]:
        return s.split("\n")[:-1]