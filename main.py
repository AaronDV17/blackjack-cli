######### Blackjack House Rules ###########

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##########################################

## Imports
from art import logo
from random import choice
import os

## Definition of initial variables & functions
cards = [11,  2,  3,  4,  5,  6,  7,  8,  9,  10,  10,  10,  10]

def clear_screen():
    _ = os.system('clear')

def deal(usr, no_cards):
    """
    Deals the card holder a stated number of cards.
    """
    for i in range(0, no_cards):
        dealt = choice(cards)
        usr.append(dealt)

def ace_check(usr, score):
    """
    Changes an ace's value in the card holder's hand from  11 to  1
    if their total score is above  21
    """
    if score >  21 and  11 in usr:
        ace_pos = usr.index(11)
        usr[ace_pos] =  1

def print_scores(dealer_hand, dealer_score, player_hand, player_score):
    """
    Prints the current scores of the dealer and the player.
    """
    print(f"The dealer's hand is {dealer_hand} with a value of {dealer_score}.")
    print(f"Your hand is {player_hand} with a value of {player_score}.")

def game():
    """
    Complete logic for the blackjack game.
    """
    # Initial Values Set
    dealer = []
    player = []
    deal(dealer,  2)
    deal(player,  2)
    d_score = sum(dealer)
    p_score = sum(player)

    # Game Phase & Logic
    if d_score ==  21:
        print(f"The dealer has blackjack - {dealer}")
        print(f"Your cards are {player} with a value of {p_score}")
        print("You lose :(")
    elif p_score ==  21:
        print(f"The dealer's upcard is [{dealer[0]}]")
        print(f"You have blackjack - {player}")
        print("You win!")
    else:
        ace_check(dealer, d_score)
        d_score = sum(dealer)

        ace_check(player, p_score)
        p_score = sum(player)

        print(f"The dealer's upcard is [{dealer[0]}]")
        print(f"Your cards are {player} with a value of {p_score}")

        while p_score <=  21:
            if input("Would you like to hit (type 'y') or stay (type 'n')?\n") == 'y':
                deal(player,  1)
                ace_check(player, p_score)
                p_score = sum(player)
                print(f"The dealer's upcard is [{dealer[0]}]")
                print(f"Your cards are {player} with a value of {p_score}.")
            else:
                break

        if p_score >  21:
            print("Bust")
            print("You lose :(")

        else:
            while d_score <  17:
                deal(dealer,  1)
                ace_check(dealer, d_score)
                d_score = sum(dealer)
            if d_score >  21:
                print_scores(dealer, d_score, player, p_score)
                print("Dealer is bust")
                print("You win!")
            elif p_score > d_score:
                print_scores(dealer, d_score, player, p_score)
                print("You win!")
            elif d_score > p_score:
                print_scores(dealer, d_score, player, p_score)
                print("You lose :(")
            elif d_score == p_score:
                print_scores(dealer, d_score, player, p_score)
                print("Push")

    if input("Would you like to play again? Type 'y' or 'n'...\n") == 'y':
        clear_screen()
        print(logo)
        game()

## Game Implementation
print(logo)
print("Welcome to the blackjack CLI game!")
if input("Would you like to play a game?\nType 'y' or 'n'...\n") == 'y':
    clear_screen()
    print(logo)
    game()
    clear_screen()
    print(logo)
    print("Thanks for playing!")
