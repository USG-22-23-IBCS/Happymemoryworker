class Animal:

    def __init__ (self, e, x, col, age):
                  self.Paws = x
                  self.especies = e
                  self.color = col
                  self.age = age
                  

    def getEspecies(self):
        return self.especies

    def setColor(self, c):
        self.color = c

    def getColor (self):
        return self.color

    def getPaws(self):
        return self.Paws

    def getAge(self):
        return self.age
    def setAge(self, age):
        self.age = age
    
    


def main():
    ani1 = Animal("cat", 4, "black and white","adult")
    ani2 = Animal ("cat", 4, "white and orange","adult")
    
    print (ani1.getEspecies())
    print (ani1.getColor())
    print(ani1.getPaws())
    print(ani1.getAge())

 
    print (ani2.getEspecies())
    print (ani2.getColor())
    print(ani2.getPaws())
    ani2.setAge ("child")
    print(ani2.getAge())
    
    
    

if __name__ == "__main__":
    main()
