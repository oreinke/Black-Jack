import shuffler as shuffler
def getHand(hand):
    str = ""
    for i in range (0, len(hand)):
        if hand[i][0] < 10:
            str += f"{hand[i]}, "
        elif hand[i][0] == 10:
            str += "T, "
        elif hand[i][0] == 11:
            str += "J, "
        elif hand[i][0] == 12:
            str += "Q, "
        elif hand[i][0] == 13:
            str += "K, "
        elif hand[i][0] == 14:
            str += "A, "

    return str[:-2]

# To be implemented later. Handles Splits. Should basically copy the double and split process. 
# returns an array of the player totals from split hands
def splitGame(stack, playerHand[0][0], playerHand[0], dealerHand[1][0], bet):
    return

# returns a tuple where [0] = stack, [1] = shoe, after this game of blackjack
def blackJack(bet, shoe, shoeCut, stack):
    playerAce = False
    dealerAce = False
    playerHand = []
    dealerHand = []
    playerTotals = []
    playerTotals.append(0)

    stack -= bet

    playerHand.append(shoe.pop(0))
    dealerHand.append(shoe.pop(0)) # face down
    playerHand.append(shoe.pop(0))
    dealerHand.append(shoe.pop(0))

    if playerHand[0][0] == 14 or playerHand[1][0] == 14:
        playerAce = True

    if dealerHand[1][0] == 14:
        dealerAce = True

    print(f"You have: {getHand(playerHand)}")

    # Funcitionality for dealing with dealer showing an ace and Insurance
    if dealerAce == True:
        print("Dealer: A")
        insurance = 0

        # all input line will be replaced with neural net decisions.
        # Handles insurance decisions
        if stack >= bet / 2.0:
            insurance = input("Insurance? (0/1)")
            while insurance != 0 and insurance != 1:
                insurance = input("Invalid input. Input 1 or 0. (y/n)")
            if insurance == 1:
                stack -= bet / 2.0
        else:
            print("Not enough in stack to place insurance.")
        
        if dealerHand[0][0] > 9 and dealerHand[0][0] < 14:
            print("Dealer Blackjack. Dealer wins.")
            if insurance == 1:
                print("Insurance Claimed.")
                stack += bet * 1.5
                return stack, shoe
            else:
                print("Womp Womp.")
                return stack, shoe
        else:
            print ("No dealer 10. Continue Play.")
    
    print(f"Dealer: {getHand[1][0]}")

    # Handles splitting hands
    # we handle split games seperately to easier deal with successive splits recursively.
    # player totals from each hand are recorded and added to playerTotals
    if (stack >= bet and (playerHand[0][0] == playerHand[1][0] or ((playerHand[0][0] > 9 and playerHand[0][0] < 14) and (playerHand[1][0] > 9 and playerHand[1][0] < 14)))):
        split = input("Split? 1 for yes, 0 for no")
        if split == 1:
            stack -= bet
            newTotals = splitGame(stack, playerHand[0][0], playerHand[0], dealerHand[1][0], bet)
            for total in newTotals:
                playerTotals.append(total)
        

    

    


def main():
    print("Beginning new session.\n Starting Balance: 1000\n Min Bet: 5\nMax Bet: 200")
    playerBalance = 1000
    print("Shuffling shoe...")
    shoe = shuffler.newShoe("")
    print("Shuffling complete.")
    while((playerAction = input("How ")))


if __name__ == "__main__":
    main()