from BlackJackEngine import Game

def main():
    result = 0
    iterations = 10000

    for i in range(0, iterations):
        Sim = Game()
        result = result + Sim.returnResult()

    print(result)
    print(result/iterations)

if __name__ == '__main__':
    main()

