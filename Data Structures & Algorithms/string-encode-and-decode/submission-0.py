class Solution:

    # Hello, World, Times, 500
    # "HelloWorldTimes500,5,10,15,3" <- Encoded
    # Hello, World, Times, 500 <- Decoded

    def encode(self, strs: List[str]) -> str:

        chars = []
        curr_index = 0
        for s in strs:
            chars.append(len(s) + curr_index)
            curr_index += len(s)

        chars.insert(0, 0)
        collapsed = ''.join(strs)
        chars.append(len(chars))
        chars = ','.join(str(char) for char in chars)

        return collapsed + ',' + chars


    def decode(self, s: str) -> List[str]:
        splat = s.split(',')
        last_index = len(splat) - 1
        num_splits = int(splat[last_index])

        indexes = []
        for i in splat[(last_index - num_splits):(last_index)]:
            indexes.append(int(i))

        output = []

        for index in indexes[::-1]:
             print(s[index:])
             output.insert(0, s[index:])
             s = s[:index]

        return output[:len(output)-1]