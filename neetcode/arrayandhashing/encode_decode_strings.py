from typing import List

class Solution:
    def encode(self, strs:List[str])-> str:
        """_summary_

        Args:
            strs (List[str]): _description_

        Returns:
            str: _description_
        """
        res = ""
        for s in strs:
            res += str(len(s)) + '$'+ s
        return res

    def decode(self, encoded_str:str)-> List[str]:
        """_summary_

        Args:
            encoded_str (str): _description_

        Returns:
            List[str]: _description_
        """
        res, i = [], 0

        while i < len(encoded_str):
            j = i
            while encoded_str[j] != '$':
                j += 1
            length = int(encoded_str[i:j])
            res.append(encoded_str[j+1 : length + j + 1])
            i = length + j + 1
        return res   

if __name__ == '__main__':
    input1 = ["neet" , "co$de"]
    solution = Solution()
    encoded_str = solution.encode(strs=input1)
    result = solution.decode(encoded_str=encoded_str)
    print(f'Orginal input:{input1}')
    print(f"Encoded string: {encoded_str}")
    print(f'Decoded output:{result}')
    
    input2 = ["lint" , "code", "love", "you"]
    solution = Solution()
    encoded_str = solution.encode(strs=input2)
    result = solution.decode(encoded_str=encoded_str)
    print(f'Orginal input:{input1}')
    print(f"Encoded string: {encoded_str}")
    print(f'Decoded output:{result}')


