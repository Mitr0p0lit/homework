import random
from random import randint
import sys

number = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

B1 = random.choice(number)
B2 = random.choice(number)
B3 = random.choice(number)
P1 = random.choice(number)
P2 = random.choice(number)
P3 = random.choice(number)
P4 = random.choice(number)
P5 = random.choice(number)

Bankir = B1 + B2
if Bankir < 15:
    Bankir = Bankir + B3
    
Player1 = P1 + P2

print( " Банкир: " )
print( "   1. Первая карта: ", B1)
print( "   2. Вторая карта: ...")
print(" Сумма карт Банкира: ")
print(" ")
print( " Игрок 1: " )
print( "   1. Первая карта: ", P1)
print( "   2. Вторая карта: ", P2)
print(" Сумма карт игрока: ", Player1)
print( "  " )

if Bankir > 21:
    sys.exit( " Игрок победил! ")

if Player1 > 21:
    sys.exit( " Банкир победил! " )

a = int(input(" Выбор: \n 1. Карта игроку \n 2. Итог \n "))
if a == 1:
    Player1 = Player1 + P3
    if Player1 > 21:
        sys.exit( " Банкир победил! " )
    print(" Сумма карт игрока: ", Player1)
    b = int(input(" Выбор: \n 1. Карта игроку \n 2. Итог \n "))
    if b == 2:
        print( " Банкир: ", Bankir )
        print( " Игрок: ", Player1 )
        if Bankir > Player1:
            print( " Банкир победил! " )
        else:
            print( " игрок победил! " )
    else:
        Player1 = Player1 + P4
        if Player1 > 21:
            sys.exit( " Банкир победил! " )
        print(" Сумма карт игрока: ", Player1)
        c = int(input(" Выбор: \n 1. Карта игроку \n 2. Итог \n "))
        if b == 2:
            print( " Банкир: ", Bankir )
            print( " Игрок: ", Player1 )
            if Bankir > Player1:
                print( " Банкир победил! " )
            else:
                print( " игрок победил! " )
        else:
            Player1 = Player1 + P5
            if Player1 > 21:
                sys.exit( " Банкир победил! " )
            else:
                print( " Банкир: ", Bankir )
                print( " Игрок: ", Player1 )
                if Bankir > Player1:
                    print( " Банкир победил! " )
                else:
                    print( " игрок победил! " )
elif a == 2:
    print( " Банкир: ", Bankir )
    print( " Игрок: ", Player1 )
    if Bankir > Player1:
        print( " Банкир победил! " )
    else:
        print( " игрок победил! " )
else:
    print(" idi naxyi ")
