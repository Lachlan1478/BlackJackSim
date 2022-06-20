import random


def drawCard():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    index = random.randint(0, 12)
    card = cards[index]
    return card

class Player():
    def hit(self):
        newCard = drawCard()
        self.sum += newCard

    def split(self):
        pass
    def double(self):
        pass
    def stand(self):
        pass
    def HandValue(self):
        if(self.sum > 21):
            return 0
        else:
            return self.sum
    def Blackjack(self):
        pass

    def __init__(self, card1, card2, dealersCard):
        self.card1 = card1
        self.card2 = card2
        self.dealerscard = dealersCard
        self.sum = card1 + card2

        while(self.sum < 11):
            self.hit()

        print(self.sum)

        self.stand()


class Game():
    def getResult(self):
        # Standoff
        print(self.dealersHand)
        if (self.PlayerHand == 0):
            self.result = -1
            return self.result
        if (self.dealersHand == 22):
            self.result = 0

        else:
            if (self.dealersHand > self.PlayerHand):
                self.result = -1
            elif (self.dealersHand == self.PlayerHand):
                self.result = 0
            else:
                self.result = 1
        return self.result

    def __init__(self):
        ## Deal cards
        # Dealers Card
        self.dealersCard = drawCard()
        self.Player = Player(drawCard(), drawCard(), self.dealersCard)
        self.PlayerHand = self.Player.HandValue()

        self.dealersHand = self.dealersCard
        while(self.dealersHand < 17):
            self.dealersHand += drawCard()

        #-1 if split or double loss, -1 if loss, 0 if draw, 1 if won and 2 if double or split win
        self.result =  0



