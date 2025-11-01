logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
user_inputs = {}
continueProgram = True

while continueProgram :
    print("Welcome to the secret Auction ")
    name = input("What is your name? ")
    bid = input("What is your bid? ")

    user_inputs[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes or 'no'.").lower()

    if more_bidders == "no":
        continueProgram = False
        break
    print("\n" * 1000000)

largestBid = user_inputs[name]

for names in user_inputs:
    if user_inputs[names] > largestBid:
        largestBid = user_inputs[names]

for names in user_inputs:
    if user_inputs[names] == largestBid:
        largestBidName = names
print("The winner is " + largestBidName + " with a bid of " + largestBid)
