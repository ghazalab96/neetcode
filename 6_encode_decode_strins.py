from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "None"

        elif strs == [""]:
            return ""

        single_str = "||".join(strs)
        return single_str

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []

        elif s == "":
            return [""]
        return s.split("||")