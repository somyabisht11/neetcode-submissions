class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
           encoded += str(len(i)) + "#" + str(i)
        return encoded
 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
          j = s.find("#", i)
          length = int(s[i:j])
          decoded = s[j+1:j+1+length]

          res.append(decoded)
          i = j + 1 + length
        return res


