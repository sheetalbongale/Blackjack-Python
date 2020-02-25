# Blackjack Game ♠️♥️♣️♦️

#### Submitted by : Sheetal Bongale | Feb 23, 2020

A simple Blackjack game using Python implementing Object Oriented Programming concepts.

- - -

### Instructions

`> git clone https://github.com/sheetalbongale/Blackjack-Python.git`

`> python blackjack.py or in ipython: %run blackjack.py`

- - -

### OBJECT OF THE GAME
Each player attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.

### CARD VALUES/SCORING
- An ace is worth 1 or 11. 
- Face cards are 10
- Any other card is its pip value.

### BUST-HIT-STAY
- Hit: To 'Hit' is to ask for another card. 
- Stand: To 'Stand' is to hold your total and end your turn.
- Bust: If your card total goes over 21 you bust, and the dealer wins regardless of the dealer's hand.

### DEALING:
Each player starts with two cards, one of the dealer's cards is hidden until the end.

### INITITATE PLAY:
After the first round of dealing, each player has the option to hit (receive more cards) or stay (no more cards). If hitting results in the player busting (total going over 21), then his or her bet is lost.

### DEALER'S TURN
After all the players are done hitting/staying, the dealer flips over his hidden card. If the dealer’s total is less than 17, then he or she needs to hit (receive a new card). This process repeats until the dealer’s hand either totals to 17 or more or busts (goes above 21).