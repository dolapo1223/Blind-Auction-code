from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bids = {}
bidding_finished = False

#Funtion to find the highest bidder
def find_highest_bid(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
      clear()
  print(bids)
  print(f"\n\nThe winner is {winner} with bidding amount of ${highest_bid}")


#loop
while not bidding_finished:
  name = input("What is your name? ")
  bid = int(input("Enter your bid price $"))
  bids[name] = bid
  should_continue = input("Are there other user who want to bid? enter 'yes' or 'no'\n")
  if should_continue == "no":
    find_highest_bid(bids)
    bidding_finished = True
  elif should_continue == "yes":
    clear()
# print(bids)
  



 