import random

def newShoe(numDecks):
    ranks = range(2, 15) # 11 = Jack, 12 = Queen, 13 = King, 14 = Ace
    suits = ['C', 'D', 'H', 'S']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    shoe = deck * numDecks
    random.shuffle(shoe)

    return shoe

def main():
    shoe = newShoe(8)
    print (shoe)
    print(f"Shoe Length: {len(shoe)}")

if __name__ == "__main__":
    main()