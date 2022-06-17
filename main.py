import numpy
import random
from BlackJackEngine import Player

def drawCard():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    index = random.randint(0, 12)
    card = cards[index]
    return card

def main():
    profit = 0
    bet = 10

    card1 = drawCard()
    dealersCard1 = drawCard()
    card2 = drawCard()

    #blackjack
    if((card1 == 1 and card2 == 10) or (card1 == 10 and card2 == 1)):
        profit = profit + bet * 3/2

    person = Player(card1, card2, dealersCard1)

    dealersCard2 = drawCard()


if __name__ == '__main__':
    main()

