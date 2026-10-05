

from random import random


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def take_cards(self, cards):
        self.hand.extend(cards)

    def play_card(self):
        return self.hand.pop(0)

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
            
    def __str__(self):
        return f"{self.suit} {self.value}"
        
    def __repr__(self):
        return f"Card('{self.suit}', {self.value})"

class Deck:
    def __init__(self, cards=None): 
        if cards is None:
            cards = []
        self.cards = cards

    def deal(self, num_cards):
        if num_cards > len(self.cards):
            raise ValueError("Inte tillräckligt med kort i leken.")

        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards
    
    def shuffle_deck(cards):
        for c in range(len(cards)):
            
            r = random.randint(c, len(cards) - 1)

            temp_cards = cards[r]

            cards[r] = cards[c]
            cards[c] = temp_cards
        
            return cards



    def make_deck():  
        cards = [] 
        suits = ["♠", "♥", "♣", "♦"]
        values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        
        for suit in suits: 
            for value in values: 
                cards.append(Card(suit, value))               
        return cards
    
def play_game():
        # Mappning för att kunna jämföra strängar ("J", "Q", "K", "A") med siffror
    card_ranks = {
        2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
        8: 8, 9: 9, 10: 10, "J": 11, "Q": 12, "K": 13, "A": 14
    }




    cards = Deck.make_deck()
    deck = Deck(cards)

    player1 = Player("Spelare 1")
    player2 = Player("Spelare 2")




                    # 2. Dela ut 1 kort var
    player1.take_cards(deck.deal(1))
    c1 = player1.play_card()
    player2.take_cards(deck.deal(1))
    c2 = player2.play_card()

                    # 3. Spela ut korten


    print(f"{player1.name} drog: {c1}")
    print(f"{player2.name} drog: {c2}")

                    # 4. Hämta numeriskt värde och jämför
    v1 = card_ranks[c1.value]
    v2 = card_ranks[c2.value]

    if v1 > v2:
            print(f"{player1.name} vinner med högst kort!")
    elif v2 > v1:
            print(f"{player2.name} vinner med högst kort!")
    else:
            print("Det blev oavgjort!")

    print("antal kort kvar: ",(len(deck.cards)))

play_game()