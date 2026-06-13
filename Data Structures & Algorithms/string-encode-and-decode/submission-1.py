class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += i + ";"
        
        return encoded_string;

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        word = ""
        for i in s:
            if i == ";":
                decoded_strs.append(word)
                word = ""
            else:
                word += i
        
        return decoded_strs;


