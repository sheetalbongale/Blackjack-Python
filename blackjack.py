########################################################## Blackjack ###########################################################
# -*- coding: utf-8 -*-
# Submitted by : Sheetal Bongale
# Python script simulates a simple command-line Blackjack game implemented using Python and Object Oriented Programming concepts
# System Requirements: Python 3.8 (Python3)
################################################################################################################################

import random

# define class for cards - holds the value and suit of an individual card
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return " of ".join((self.value, self.suit))


# define class for deck - holds the 52 unique cards and the logic for shuffling and dealing
class Deck:

    # list comprehension containing lists of every suit and value
    def __init__(self):
        self.cards = [
            Card(suit, value)
            for suit in ["Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦"]
            for value in [
                "A",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
            ]
        ]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    # return the top card and remove it from the deck so that it cannot be dealt again - pop fn
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)


# define class for Hand - holds the value of cards based by the rules of the game, define and display scores
class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    #  add the Card instance
    def add_card(self, card):
        self.cards.append(card)

    # calculating the currently held cards value
    def calculate_value(self):
        # assume start value = 0 and the player does not have an ace
        self.value = 0
        has_ace = False

        # loop to add values of the card: non-ace cards and ace cards
        for card in self.cards:
            # this will add value to hand if the cards are numerical i.e non-ace cards
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                # value to hand for ace-cards
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        # make ace value = 1 instead of 11
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    # display each hand's cards
    def display(self):
        if self.dealer:
            print("Hidden")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())


# main script to define the game flow
class Game:
    def __init__(self):
        pass

    # track whether or not we are still playing the game
    def play(self):
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            # deal two cards each to the player and the dealer
            for _ in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("---------------------------------")
            print("Lets play the game of BlackJack!")
            print("---------------------------------")
            print("")
            print("Your hand is:")
            self.player_hand.display()
            print()
            print("Dealer's hand is:")
            self.dealer_hand.display()

            # enter a loop that will run until a winner is decided
            game_over = False

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(
                        player_has_blackjack, dealer_has_blackjack
                    )
                    continue

                choice = input("\nPlease choose [Hit(H) / Stand(S)] ").lower()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'hit' or 'stand' (or H/S) ").lower()
                if choice in ["hit", "h"]:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You have lost!")
                        game_over = True
                else:
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()
                    print("---------------------------------")
                    print("Final Results")
                    print("Your hand:", player_hand_value)
                    print("Dealer's hand:", dealer_hand_value)
                    print("---------------------------------")
                    if player_hand_value > dealer_hand_value:
                        print("Blackjack! You Win!")
                    elif player_hand_value == dealer_hand_value:
                        print("Tie!")
                    else:
                        print("Dealer Wins!")
                    print("---------------------------------")
                    game_over = True

            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("\n-------Thanks for playing!-------")
                playing = False
            else:
                game_over = False

    def player_is_over(self):
        return self.player_hand.get_value() > 21

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")

        elif player_has_blackjack:
            print("You have blackjack! You win!")

        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")


# run the game - create an instance of the Game class and call the play() method
if __name__ == "__main__":
    g = Game()
    g.play()
