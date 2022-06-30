import random



def drawCard():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    index = random.randint(0, 12)
    card = cards[index]
    return card

class Actions():
    def hit(self):
        newCard = drawCard()
        self.sum += newCard
    def split(self):
        pass
    def double(self):
        lastCard = drawCard()
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


class Game():
    def __init__(self):
        ## Deal cards
        # Dealers Card
        self.dealersCard = drawCard()
        self.card1 = drawCard()
        self.card2 = drawCard()

        #Get action

        while(self.dealersCard < 17):
            self.dealersCard += drawCard()

        #-1 if split or double loss, -1 if loss, 0 if draw, 1 if won and 2 if double or split win
        self.result =  0

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



