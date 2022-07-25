import random
from BasicStrategy import Action


def drawCard(dealer = False):
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    index = random.randint(0, 12)
    card = cards[index]
    if(card == 1 and dealer):
        card = 11
    return card

class Game():
    def hit(self, sum):
        action = "H"
        while(action != "S"):
            sum += drawCard()
            if(sum > 21):
                break
            else:
                action = Action(sum, 0, self.dealersCard[0], False)
        return sum

    def double(self):
        lastCard = drawCard()
        return lastCard+self.hand[0]+self.hand[1]

    def getResult(self, PlayerHand, dealersHand):
        # Standoff
        if (PlayerHand > 21):
            self.result = -1
        elif (dealersHand == 22):
            self.result = 0
        elif(dealersHand > 22):
            self.result = 1

        else:
            if (dealersHand > PlayerHand):
                self.result = -1
            elif (dealersHand == PlayerHand):
                self.result = 0
            else:
                self.result = 1
        return self.result

    def actAction(self, move):
        if (move == "H"):
            self.sum = self.hit(self.hand[0] + self.hand[1])
            self.getResult(self.sum, sum(self.dealersCard))
        elif (move == "D"):
            self.sum = self.double()
            self.getResult(self.sum, sum(self.dealersCard))
            self.result = self.result * 2
        else:
            self.sum = self.hand[0] + self.hand[1]
            self.getResult(self.sum, sum(self.dealersCard))
        return self.result

    def split(self):
        self.hand2.append(self.hand[0])
        self.hand2.append(drawCard())
        self.hand[1] = drawCard()

        #hand 1
        move1 = Action(self.hand[0], self.hand[1], self.dealersCard[0], False)
        result1 = self.actAction(move1)

        #hand 2
        move2 = Action(self.hand2[0], self.hand2[1], self.dealersCard[0], False)
        result2 = self.actAction(move2)

        return result1+result2


    def __init__(self):
        ## Deal cards
        # Dealers Card
        self.dealersCard = [drawCard(True)]
        while (sum(self.dealersCard) < 17):
            self.dealersCard.append(drawCard(True))
            if(sum(self.dealersCard)>22 and 11 in self.dealersCard):
                self.dealersCard.remove(11)
                self.dealersCard.append(1)

        self.hand = [drawCard(), drawCard()]
        self.hand2 = []

        self.sum = 0
        self.sum2 = 0
        self.result = 0

        #Get action
        self.move = Action(self.hand[0], self.hand[1], self.dealersCard[0])

        if(self.move == "SP"):
            self.result = self.split()
        else:
            self.actAction(self.move)

    def returnResult(self):
        print("Hand: ", self.sum, "Dealer: ", sum(self.dealersCard))
        return self.result


