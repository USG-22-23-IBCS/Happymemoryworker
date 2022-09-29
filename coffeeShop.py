class Coffeeshop:

    def __init__(self):
        self.blackCoffee = 3.50
        self.icedLatte = 4.00
        self.espresso = 1.50
        self.menu = "1 Black Coffee\n2 Iced Latte\n3 Espresso"

    def getMenu(self):
        return self.menu

    def getPrice(self, order):
        if order == "1":
            return round(self.blackCoffee, 2)
        
        if order == "2":
            return round(self.icedLatte, 2) 
        
        if order == "3":
            return round(self.espresso, 2)
        
        else:
            return "We don't have that here"
                
def main():

    C = Coffeeshop()
    print("Welcome to the shop! This is our menu:")
    print(C.menu)
       #need to assign a variable name to the input
    myOrder = input("What number do you want?\n")
    N = input("What name should I get for this?\n")

    print("Sure, " + str(N) + "! This costs $" + str(C.getPrice(myOrder))+ "0. We'll have that right out for you.")






if __name__ == "__main__":
    main()
