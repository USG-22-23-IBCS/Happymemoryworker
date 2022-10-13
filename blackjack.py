import random

class Card:

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def getName(self):
        return self.name

    def getSuit(self):
        return self.suit

    def getCard(self):
        #defines what a card is
        return [self.suit, self.name]

class Deck:

    def __init__(self):
        self.cards = []
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        #rewrites the original value of some cards to fit the specifics of a card deck
        for s in suits:
            for i in range(1, 14):
                if i == 1:
                    name = "Ace"
                elif i == 11:
                    name = "Jack"
                elif i == 12:
                    name = "Queen"
                elif i == 13:
                    name = "King"
                else:
                    name = str(i)

                C = Card(s, name)
                self.cards.append(C)

    def getCards(self):
        return self.cards

    def dealCard(self):
        newCard = random.choice(self.cards)
        #chooses random cards from the optio
        self.cards.remove(newCard)
        #removes the card so the same card is not dealed again
        return newCard

def calcHandValue(hand):
    #this part of the code define the value for specific card that doesn't have a direct number associated to them.
    #It also specifies the different values of "ace" and the diferent options it should have in certain ocassions
    #This part is responsible to sum up the number of the cards with the already existing value
    total = 0
    for h in hand:
        name = h[1]
        
##H is the name of the list of suit (0 position) and name (1 position) of the card. Because it is h[1] it is
##relating to the name of the card, because in the code it is in the 1 position
        if name == "Ace":
            total = total + 11
            if total > 21:
                total = total - 10
                # it is -10 because the 11 was already added so it's just adding 1
        elif name == "King" or name == "Queen" or name == "Jack" :
            total = total + 10
        else:
            total = total + int(name)
        
    return total
#sum up the value of the cards

def main():

    print("Welcome to Blackjack!\n") 

    D = Deck()

    userHand = [D.dealCard().getCard(), D.dealCard().getCard()]
    dealerHand = [D.dealCard().getCard(), D.dealCard().getCard()]

    print("Dealer hand:")
    print(dealerHand)
    print("")
    print(userHand)
    print("Your hand's value is :" + str(calcHandValue(userHand)))
    print("")

    while True:
        option = input("Type 1: Hit  or 2: Stand\n")
        if option == "1":
            userHand.append(D.dealCard().getCard())
        else:
            break
        print("")
        print(userHand)
        print("Your hand's value is :" + str(calcHandValue(userHand)))
        print("")

    print("")
    print("Dealer hand:")
    print(dealerHand)
    print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))
    print("")
    
    while True:
        #creates different options of what could happen depending on the dealer's moves.
        if calcHandValue(dealerHand) < 17:
            print("Dealer hits!\n")
            dealerHand.append(D.dealCard().getCard())
            print("Dealer hand:")
            print(dealerHand)
            print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))
            print("")
        else:
            print("Dealer stands!\n")
            break
        if calcHandValue(dealerHand) > 21:
            print("Dealer bust!")
            break

#tell if the user won
# give the user a option to replay the game
#dosn't have a limit of hits



if __name__ == "__main__":
    main()
