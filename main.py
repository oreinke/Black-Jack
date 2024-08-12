import shuffler as shuffler
def getHand(hand):
    str = ""
    for i in range (0, len(hand)):
        if hand[i] < 10:
            str += f"{hand[i]}, "
        elif hand[i] == 10:
            str += "T, "
        elif hand[i] == 11:
            str += "J, "
        elif hand[i] == 12:
            str += "Q, "
        elif hand[i] == 13:
            str += "K, "
        elif hand[i] == 14:
            str += "A, "

    return str[:-2]

def blackJack(bet, shoe, shoeCut, stack):
    playerAce = False
    dealerAce = False
    playerHand = []
    dealerHand = []

    if shoe[0] == 14 or shoe[2] == 14:
        playerAce = True
    if shoe[3] == 14:
        dealerAce = True
    playerHand.append(shoe.pop(0))
    dealerHand.append(shoe.pop(0)) # face down
    playerHand.append(shoe.pop(0))
    dealerHand.append(shoe.pop(0))

    print(f"You have: {getHand(playerHand)}")
    if dealerAce == True:
        print("Dealer: A")
        # all input line will be replaced with neural net decisions.
        insurance = input("Insurance? (0/1)")
        while insurance != 0 and insurance != 1:
            insurance = input("Invalid input. Input 1 or 0. (y/n)")
        
    

    

    


def main():
    print("Beginning new session.\n Starting Balance: 1000\n Min Bet: 5\nMax Bet: 200")
    playerBalance = 1000
    print("Shuffling shoe...")
    shoe = shuffler.newShoe("")
    print("Shuffling complete.")


if __name__ == "__main__":
    main()