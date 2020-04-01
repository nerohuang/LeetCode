class Solution:
    def addBinary(self, a: str, b: str) -> str:
       return bin(int(a,2)+int(b,2))[2:]

    def abc(self):
        print(self.addBinary(input(),input()))