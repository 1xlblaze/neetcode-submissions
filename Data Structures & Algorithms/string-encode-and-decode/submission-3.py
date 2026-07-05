class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "-1"
        string = "~ ".join(strs)
        return string
        

    def decode(self, s: str) -> List[str]:
        if s == "-1":
            return []
        return s.split("~ ")


        
