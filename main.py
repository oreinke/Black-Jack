import shuffler as shuffler

def main():
    print("Beginning new session.\n Starting Balance: 1000\n Min Bet: 5\nMax Bet: 200")
    print("Shuffling shoe...")
    shoe = shuffler.newShoe("")
    print("Shuffling complete.")

if __name__ == "__main__":
    main()