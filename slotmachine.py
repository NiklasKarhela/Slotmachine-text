import time
import random

letters = ["U", "Q", "W", "E", "R", "T", "Y"]
worth = [30, 60, 90, 120, 150, 180, 210]
balance = []

biggest_win = [0]


def insert_money():
        balance.append(int(input("How much money do you want to put in? $")))

def ask_lines_spin():
    spins = 0
    #lines
    while True:
        time.sleep(0.5)
        lines = int(input("How many lines do you want? (1-3, one line is $15)"))
        if lines <= 3:
            break
        else:
            time.sleep(0.5)
            print("there are max 3 lines")
    n = 0
    for x in range(len(worth)):
        n = n+1
        worth[x] = 30 * n * lines

    if input("Do you want to see the pay rate? (yes/no)") == "yes":
        print(f"U = {worth[0]}, Q = {worth[1]}, W = {worth[2]}, E = {worth[3]}, R = {worth[4]}, T = {worth[5]} and Y = {worth[6]}")

    #spin
    while True:
        if input("Do you want to spin? (yes/no) ") == "yes":
            spins += 1
            balance[0] = balance[0] - lines * 15

            top = random.choices(letters, weights =[0.5, 0.3, 0.1, 0.05, 0.03, 0.02, 0.01], k=3)
            middle = random.choices(letters, weights =[0.5, 0.3, 0.1, 0.05, 0.03, 0.02, 0.01], k=3)
            bottom = random.choices(letters, weights =[0.5, 0.3, 0.1, 0.05, 0.03, 0.02, 0.01], k=3)

            if lines == 1:
                time.sleep(0.5)
                print(top)
                check_win(top, 0, 0, balance)

            elif lines == 2:
                time.sleep(0.5)
                print(top)
                print(middle)
                check_win(top, middle, 0,balance)

            else:
                time.sleep(0.5)
                print(top)
                print(middle)
                print(bottom)
                check_win(top, middle, bottom, balance)

            if balance[0] < lines*15:
                time.sleep(0.5)
                print("Your balance is too low, put more in")
                print(f"It took {spins} spins")
                print(f"Your biggest win was {biggest_win[0]} (three in a row of {letters[worth.index(biggest_win[0])]})")
                break

        else:
            time.sleep(0.5)
            print(f"Your balance is {balance[0]}")
            print(f"You had {spins} spins")
            print(f"Your biggest win was {biggest_win[0]} (three in a row of {letters[worth.index(biggest_win[0])]}:s)")
            break




def check_win(t, m, b, balance):
    rows = [t, m, b]

    if m == 0 and b == 0:
        if t[0] == t[1] and t[1] == t[2]:
            balance[0] = balance[0] + worth[letters.index(t[0])]
        if worth[letters.index(t[0])] > biggest_win[0]:
            biggest_win[0] = worth[letters.index(t[0])]

        print(f"Your balance is: {balance[0]}")

    if b == 0:
        for x in range(2):
            if rows[x][0] == rows[x][1] and rows[x][1] == rows[x][2]:
                balance[0] = balance[0] + worth[letters.index(rows[x][0])]
            if worth[letters.index(rows[x][0])] > biggest_win[0]:
                biggest_win[0] = worth[letters.index(rows[x][0])]

        print(f"Your balance is: {balance[0]}")
        
    else:
        for x in range(3):
            if rows[x][0] == rows[x][1] and rows[x][1] == rows[x][2]:
                balance[0] = balance[0] + worth[letters.index(rows[x][0])]
            if worth[letters.index(rows[x][0])] > biggest_win[0]:
                biggest_win[0] = worth[letters.index(rows[x][0])]

        print(f"Your balance is: {balance[0]}")


while True:
    insert_money()
    ask_lines_spin()
    break
