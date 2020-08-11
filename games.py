import random

money = 100

#Write your game of chance functions here
def flip_coin(side, bet):
    if bet < 0:
        print("Your bet should be above 0")
        return 0
    print("------------------")
    print("Let's flip a coin! You guesses {side}".format(side = side))
    num = random.randint(1, 2)
    if num == 1:
        machine_side = "heads"
    elif num == 2:
        machine_side = "tails"
    print("It's {side}!!".format(side = machine_side))
    
    if side == machine_side:
        print("You have won! You get {money} dollars".format(money = bet*2))
        return bet*2
    else:
        print("You have lost. You lose {money} dollars".format(money = -(bet)))
        return -bet
    print("------------------")
    
def cho_han(guess, bet):
    if bet < 0:
        print("Your bet should be above 0")
        return 0
    print("------------------")
    num = random.randint(1, 6)
    num2 = random.randint(1, 6)
    total = num + num2
    print("Dice 1 is: {num}, Dice 2 is: {num2}. Total is: {total}".format(num = num, num2 = num2, total = total))
    if total % 2 == 0:
        result = "even"
    else:
        result = "odd"
    
    if result == guess:
        print("You have won! The result of the sum of the two dices is {guess}. You get {money} dollars".format(guess = guess, money = bet*2))
        return bet*2
    else:
        print("You have lost. The result of the sum of the two dices is not {guess}. You lose {money} dollars".format(guess = guess, money = -(bet)))
        return -bet
    print("------------------")


def pick_cards(bet):
    if bet < 0:
        print("Your bet should be above 0")
        return 0
    print("------------------")
    num = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print("Your card was {num}".format(num = num))
    print("Their card was {num2}".format(num2 = num2))
    if num > num2:
        print("Player number 1 has won. His card was higher than player's 2 card. Player number 1 gets {bet} dollars".format(bet = bet))
        return bet
    elif num < num2:
        print("Player number 2 has won. His card was higher than player's 1 card. Player number 1 loses {bet} dollars".format(bet = -(bet)))
        return -bet
    elif num == num2:
        print("Both cards are the same number! It's a tie.")
        return 0
    print("------------------")

def roulette(guess, bet):
    if bet < 0:
        print("Your bet should be above 0")
        return 0
    print("------------------")
    num = random.randint(0, 36)
    if num % 2 == 0 and guess == "even" and num != 0:
        print("You have won! The number is even! You get {bet} dollars".format(bet = bet / 2))
        return bet / 2
    elif num % 2 == 0 and guess == "odd":
        print("You have lost! The number is even. You lose {bet} dollars").format(bet = -bet)
        return -bet
    elif num % 2 != 0 and guess == "even":
        print("You have lost! The number is odd. You lose {bet} dollars").format(bet = -bet)
        return -bet
    elif num % 2 !=0 and guess == "odd" and num != 0:
        print("You have won! The number is odd! You get {bet} dollars".format(bet = bet / 2))
        return bet / 2
    elif num == guess:
        print("You have won! You get {bet} dollars".format(bet = bet * 10))
        return bet * 10
    elif num > 18 and num != 0 and guess == "high":
        print("You have won! The number is between 19-36. You get {bet} dollars".format(bet = bet / 2))
        return bet / 2
    elif num < 18 and num != 0 and guess == "low":
        print("You have won! The number is between 1-18. You get {bet} dollars".format(bet = bet / 2))
        return bet / 2
    elif (num > 18 or num != 0) and guess == "low":
        print("You have lost! The number is not between 1-18. You lose {bet} dollars").format(bet = -bet)
        return -bet
    elif (num < 18 or num != 0) and guess == "high":
        print("You have lost! The number is not between 19-36. You lose {bet} dollars").format(bet = -bet)
        return -bet
    print("------------------")

#Call your game of chance functions here
money += flip_coin("Heads", 10)
money += cho_han("odd", 15)
money += pick_cards(20)
money += roulette("high", 25)
print("You have {money} dollars left!".format(money = money))
