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

    # Creates a new deck of cards then shuffles it
    deck = Deck()
    deck.shuffle_deck()

    # Creates Player 1
    player_hand = Player()
    player_hand.new_card(deck.deal_card())
    player_hand.new_card(deck.deal_card())

    # Creates the dealer
    dealer_hand = Player()
    dealer_hand.new_card(deck.deal_card())
    dealer_hand.new_card(deck.deal_card())

    # Creates the player's chips (plan to integrate it into Player instance soon)
    player_chips = Chips()
    place_bet(player_chips)

    # Shows one card of the dealer's cards but both of the player's
    show_one(player_hand, dealer_hand)

    # While the player is is still hitting
    while playing:

        # Obtain user input on how to proceed
        hit_or_stand(deck, player_hand)

        # Shows one card of the dealer's cards but both of the player's
        show_one(player_hand, dealer_hand)

        # Will run if the player has bust
        if player_hand.value > 21:

            player_busts(player_chips)
            break

    # If the player wants to stand
    # This block runs if the player stands
    if player_hand.value <= 21:

        while dealer_hand.value < 17:

            hit(deck, dealer_hand)

        # This will run when either the dealer has bust or the value of his cards have exceeded 17
        show_all(player_hand, dealer_hand)

        # Determine winner
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

        # If the player chooses to play again
        playing = True

    # If the player chooses to quit
    else:
        
        print("Thank you for playing!")

        game_continue = False
