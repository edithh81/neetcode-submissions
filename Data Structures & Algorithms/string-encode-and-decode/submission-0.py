class Solution:
    def _caesar(self, text: str, shift: int) -> str:
        res = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                res.append(chr((ord(char) - base + shift) % 26 + base))
            else:
                res.append(char)
        return ''.join(res)
    def encode(self, strs: List[str]) -> str:
        k = 3

        encoded_lst = []
        for s in strs:
            caesar_s = self._caesar(s, k)
            encoded_lst.append(f"{len(caesar_s)}#{caesar_s}")

        return ''.join(encoded_lst)


    def decode(self, s: str) -> List[str]:
        k = 3
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            start = j + 1
            end = start + length
            encoded_str = s[start:end]

            res.append(self._caesar(encoded_str, -k))
            i = end

        return res
