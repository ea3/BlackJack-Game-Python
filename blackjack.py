import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + " of " + self.suit


class Deck:

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))


	def __str__(self):
		deck_composition = ''
		for card in self.deck:
			deck_composition += '\n' + card.__str__()
		return "The Deck has: " + deck_composition


	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

#test_deck = Deck()
#test_deck.shuffle()

#print(test_deck)

#print(suits)


class Hand:
	def __init__(self):
		self.cards = [] 	# Start with an empty list
		self.value = 0   	# Start with zero value
		self.aces = 0    # Add a value to keep track of aces


	def add_card(self,card):

		self.cards.append(card)
		self.value += values[card.rank]


	def adjust_for_ace(self):
		pass

test_deck = Deck()
test_deck.shuffle()

test_player = Hand()
#Deal one card from the Deck
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)





































