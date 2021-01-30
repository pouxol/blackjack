############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from replit import clear
import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def blackjack():
  print(logo)
  your_cards = []
  comp_cards = []
  your_cards.append(random.choice(cards))
  your_cards.append(random.choice(cards))
  comp_cards.append(random.choice(cards))
  comp_cards.append(random.choice(cards))

  def play_round(your_cards, comp_cards):
    your_sum = sum(your_cards)
    comp_sum = sum(comp_cards)
    print(f"  Your cards: {your_cards}, current score: {your_sum}")
    print(f"  Computer's first card: {comp_cards[0]}")

    if your_sum > 21:
      if 11 not in your_cards:
        print(f"  Your final hand: {your_cards}, final score: {your_sum}")
        print(f"  Computer's final hand: {comp_cards}, final score: {comp_sum}")
        print("  You went over. You lose!")
      else:
        your_cards[your_cards.index(11)] = 1
        your_sum = sum(your_cards)
        if your_sum > 21:
          print(f"  Your final hand: {your_cards}, final score: {your_sum}")
          print(f"  Computer's final hand: {comp_cards}, final score: {comp_sum}")
          print("  You went over. You lose!")
        else:
          print(f"  Your cards: {your_cards}, current score: {your_sum}")
          print(f"  Computer's first card: {comp_cards[0]}")
          draw_another_card(your_cards, comp_cards)
    else:
      draw_another_card(your_cards, comp_cards)

  def draw_another_card(your_cards, comp_cards):
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "n":
      
      while sum(comp_cards) < 17:
        comp_cards.append(random.choice(cards))
        comp_sum = sum(comp_cards)
        your_sum = sum(your_cards)
        if sum(comp_cards) > 21:
          if 11 not in comp_cards:
            print(f"  Your final hand: {your_cards}, final score: {your_sum}")
            print(f"  Computer's final hand: {comp_cards}, final score: {comp_sum}")
            print("  Computer went over. You win!")
          else:
            comp_cards[comp_cards.index(11)] = 1
            comp_sum = sum(comp_cards)

      if comp_sum <= 21:
        comp_sum = sum(comp_cards)
        your_sum = sum(your_cards)
        print(f"  Your final hand: {your_cards}, final score: {your_sum}")
        print(f"  Computer's final hand: {comp_cards}, final score: {comp_sum}")
        if comp_sum == your_sum:
          print("  Draw!")
        elif comp_sum > your_sum:
          print("  You lose!")
        elif your_sum > comp_sum:
          print("  You win!")

    elif another_card == "y":
      your_cards.append(random.choice(cards))
      play_round(your_cards, comp_cards)

  play_round(your_cards, comp_cards)

while play == "y":
  clear()
  blackjack()
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")