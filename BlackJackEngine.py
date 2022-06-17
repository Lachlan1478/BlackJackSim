import random


class Player():
    def drawCard(self):
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        index = random.randint(0, 12)
        card = cards[index]
        return card
    def hit(self):
        newCard = self.drawCard()
        pass
    def split(self):
        pass
    def double(self):
        pass
    def stand(self):
        pass
    def Blackjack(self):
        pass

    def __init__(self, card1, card2, dealersCard):
        self.card1 = card1
        self.card2 = card2
        self.dealerscard = dealersCard

        self.sum = card1 + card2


        while(self.sum < 11):
            self.hit()