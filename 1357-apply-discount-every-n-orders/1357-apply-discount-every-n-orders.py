class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.count = 0
        self.mp = {pro:price for pro,price in zip(products,prices)}
        self.discount = discount
        self.n = n
        
    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count+=1
        
        total = 0
        for pro,amt in zip(product,amount):
            total += self.mp[pro]*amt

        return total if self.count%self.n != 0 else total * ((100 - self.discount) / 100)
    
# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)