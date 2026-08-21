class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = []
        for word in strs:
            encoded = str(len(word)) + '-' + word 
            encoded_strs.append(encoded)
        
        final = "".join(encoded_strs)
        
        return final


    def decode(self, s: str) -> List[str]:
        final_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '-':
                j += 1
            
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            final_list.append(word)

            i = j + 1 + length        
        return final_list 


            
