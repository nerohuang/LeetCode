class ProductOfNumbers:

    def __init__(self):
        self.prepro = [1];

    def add(self, num: int) -> None:
        if num == 0:
            self.prepro = [1];
        else:
            self.prepro.append(self.prepro[-1] * num);

    def getProduct(self, k: int) -> int:
        if k >= len(self.prepro):
            return 0;
        else:
            return int(self.prepro[-1]/self.prepro[-1 - k])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)