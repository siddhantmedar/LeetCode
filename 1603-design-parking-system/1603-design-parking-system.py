class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.mid = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big:
                self.big-=1
                return True
            else:
                return False
            
        elif carType == 2:
            if self.mid:
                self.mid-=1
                return True
            else:
                return False
            
        elif carType == 3:
            if self.small:
                self.small-=1
                return True
            else:
                return False
            

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)