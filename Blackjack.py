from Deck import Deck
from Player import Player
from Chips import Chips

# --------------------------------------------- FUNCTIONS --------------------------------------------- #

def place_bet(chips):

    is_valid = False

    while not is_valid:

        try:

            chips.bet = int(input("Please enter your bet: "))

        except ValueError:

            print("Please enter a valid integer. ")

        else:

            if chips.bet > chips.total:

                print(f"Insufficient chips. You only have {chips.total} chips")

            else:

                is_valid = True

# ------------------------------------------------------------------------------------------ #

def hit(the_deck, hand):

    hand.new_card(the_deck.deal_card())
    hand.adjust_for_ace()

# ------------------------------------------------------------------------------------------ #

def hit_or_stand(the_deck, hand):

    global playing

    is_valid = False

    while not is_valid:

        choice = input("Enter H for Hit and S for Stand: ")

        if choice.upper() == "H":

            hit(the_deck, hand)
            is_valid = True

        elif choice.upper() == "S":

            print("Dealer's Turn")
            playing = False
            is_valid = True

        else:

            print("Invalid choice. Please enter a valid choice. ")

# ------------------------------------------------------------------------------------------ #

def player_busts(chips):

    print("Player busts, Dealer Wins")
    chips.lose_bet()

# ------------------------------------------------------------------------------------------ #

def player_wins(chips):

    print("Player Wins")
    chips.win_bet()

# ------------------------------------------------------------------------------------------ #

def dealer_busts(chips):

    print("Dealer busts, Player wins")
    chips.win_bet()

# ------------------------------------------------------------------------------------------ #

def dealer_wins(chips):

    print("Dealer Wins")
    chips.lose_bet()

# ------------------------------------------------------------------------------------------ #

def push():
    print("Game is a tie")

# ------------------------------------------------------------------------------------------ #

def show_one(player, dealer):

    print("Dealer's Hand: ")
    print("Not shown")
    print(dealer.cards[1])

    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

    print("\n")

# ------------------------------------------------------------------------------------------ #

def show_all(player, dealer):

    print("Dealer's Hands: ")

    print("\n")

    for card in dealer.cards:
        print(card)

    print("\n")

    print("Player's Hand:")

    for card in player.cards:
        print(card)

    print("\n")

# --------------------------------------------- MAIN GAME --------------------------------------------- #
playing = True
game_continue = True

while game_continue:

    print("Game Starting...")

    # Initialises and shuffles the deck of cards
    deck = Deck()
    deck.shuffle_deck()

    # Initialises the player's hand and deals him two cards
    player_hand = Player()
    player_hand.new_card(deck.deal_card())
    player_hand.new_card(deck.deal_card())

    # Initialises the dealer's hand and deals him two cards
    dealer_hand = Player()
    dealer_hand.new_card(deck.deal_card())
    dealer_hand.new_card(deck.deal_card())

    player_chips = Chips()  # Initialises the player's chips
    place_bet(player_chips)  # Allows the player to place a bet

    show_one(player_hand, dealer_hand)  # Shows one card of the dealer's and both of the players

    # While the player is playing (i.e. he is still hitting)
    while playing:

        # Take the player's choice on what to do
        hit_or_stand(deck, player_hand)

        # Show one hand of the dealer and all of the player
        show_one(player_hand, dealer_hand)

        if player_hand.value > 21:  # If the player busts

            player_busts(player_chips)
            break  # Break the current while loop and go to the end of the game

    # If the player decided to stand (i.e. he didn't bust)
    # This section only runs if the player is still in the game (stood and did not bust)
    if player_hand.value <= 21:

        # As long as the dealer has not hit 17 yet, keep hitting (Dealer's turn now)
        while dealer_hand.value < 17:

            hit(deck, dealer_hand)

        # Once the dealer is also finished, show down
        show_all(player_hand, dealer_hand)

        # Figure out who is the winner and what the outcome of the game is
        if dealer_hand.value > 21:

            dealer_busts(player_chips)

        elif dealer_hand.value > player_hand.value:

            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:

            player_wins(player_chips)

        else:
            push()

    print(f"\nPlayer total chips are at: {player_chips.total}")

    new_game = input("Play again? Y/N: ")

    if new_game == "Y":

        # Resets playing in case the player stood in the last round
        # This ensures that the actual game play part can happen because hit or stand makes it false if stand was chosen
        playing = True

    # If the player wants to stop
    else:
        print("Thank you for playing!")

        # This sets the main game boolean to be false, hence breaking out of the main lop
        game_continue = False
