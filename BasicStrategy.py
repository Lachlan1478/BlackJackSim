

dict1 = {1: {10: "S", 9: "S", 8: "S",
               7: {1: "H", 2: "S", 3: "D", 4: "D", 5: "D", 6: "D", 7: "S", 8: "S", 9: "H", 10: "H"},
               6: {1: "H", 2: "S", 3: "D", 4: "D", 5: "D", 6: "D", 7: "S", 8: "S", 9: "H", 10: "H"},
               5: {1: "H", 2: "H", 3: "H", 4: "D", 5: "D", 6: "D", 7: "H", 8: "H", 9: "H", 10: "H"},
               4: {1: "H", 2: "H", 3: "H", 4: "D", 5: "D", 6: "D", 7: "H", 8: "H", 9: "H", 10: "H"},
               3: {1: "H", 2: "H", 3: "H", 4: "H", 5: "D", 6: "D", 7: "H", 8: "H", 9: "H", 10: "H"},
               2: {1: "H", 2: "H", 3: "H", 4: "H", 5: "D", 6: "D", 7: "H", 8: "H", 9: "H", 10: "H"},
               1: "SP"},
           8: {8: "SP"},
           10: {10: "S"},
           9: {9: {1: "S", 2: "SP", 3: "SP", 4: "SP", 5: "SP", 6: "SP", 7: "S", 8: "SP", 9: "SP", 10: "S"}},
           7: {7: {1: "H", 2: "SP", 3: "SP", 4: "SP", 5: "SP", 6: "SP", 7: "SP", 8: "H", 9: "H", 10: "H"}},
           6: {6: {1: "H", 2: "SP", 3: "SP", 4: "SP", 5: "SP", 6: "SP", 7: "H", 8: "H", 9: "H", 10: "H"}},
           5: {5: {1: "H", 2: "D", 3: "D", 4: "D", 5: "D", 6: "D", 7: "D", 8: "D", 9: "D", 10: "H"}},
           4: {4: {1: "H", 2: "H", 3: "H", 4: "H", 5: "SP", 6: "SP", 7: "H", 8: "H", 9: "H", 10: "H"}},
           3: {3: {1: "H", 2: "SP", 3: "SP", 4: "SP", 5: "SP", 6: "SP", 7: "SP", 8: "H", 9: "H", 10: "H"}},
           2: {2: {1: "H", 2: "SP", 3: "SP", 4: "SP", 5: "SP", 6: "SP", 7: "SP", 8: "H", 9: "H", 10: "H"}}
           }

dict2 = {21: "S",
         20: "S",
         19: "S",
         18: "S",
         17: "S",
         16: {1: "H", 2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "H", 8: "H", 9: "H", 10: "H"},
         15: {1: "H", 2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "H", 8: "H", 9: "H", 10: "H"},
         14: {1: "H", 2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "H", 8: "H", 9: "H", 10: "H"},
         13: {1: "H", 2: "S", 3: "S", 4: "S", 5: "S", 6: "S", 7: "H", 8: "H", 9: "H", 10: "H"},
         12: {1: "H", 2: "H", 3: "H", 4: "S", 5: "S", 6: "S", 7: "H", 8: "H", 9: "H", 10: "H"},
         11: {1: "H", 2: "D", 3: "D", 4: "D", 5: "D", 6: "D", 7: "D", 8: "D", 9: "D", 10: "D"},
         10: {1: "H", 2: "D", 3: "D", 4: "D", 5: "D", 6: "D", 7: "D", 8: "D", 9: "D", 10: "H"},
         9: {1: "H", 2: "H", 3: "D", 4: "D", 5: "D", 6: "D", 7: "H", 8: "H", 9: "H", 10: "H"},
         8: "H",
         7: "H",
         6: "H",
         5: "H"
         }

def Action(card1, card2, dealersCard):
    Move = ""
    small = min(card1, card2)
    big = max(card1, card2)

    if(small == 1):
        if(len(dict1[small][big]) == 10):
            Move = dict1[small][big][dealersCard]
        else:
            Move = dict1[small][big]
    elif(small == big):
        if (len(dict1[small][big]) == 10):
            Move = dict1[small][big][dealersCard]
        else:
            Move = dict1[small][big]
    else:
        sum = small+big
        if (len(dict2[sum]) == 10):
            Move = dict2[sum][dealersCard]
        else:
            Move = dict2[sum]

    return Move
