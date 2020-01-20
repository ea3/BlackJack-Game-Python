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


		# Tracking aces:
		if card.rank == 'Ace':
			self.aces += 1


	def adjust_for_ace(self):
		
		# If total value > 21 and I still have an ace, then change my ace to 1 instead of 11. 
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

test_deck = Deck()
test_deck.shuffle()

test_player = Hand()
#Deal one card from the Deck
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)



class Chips:

	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet


	def take_bet(chips):

		while True:

			try:
				chips.bet = int(input("How many chips would you like to bet? "))

			except:
				print("Sorry, please provide a real amount")

			else:
				if chips.bet > chips.total:
					print('Sorry, you do not have enough chips! You have: {}'.format(chips.total))
				else:
					break

	def hit(deck, hand):

		single_card = deck.deal()
		hand.add_card(single_card)
		hand.adjust_for_ace()

	def hit_or_stand(deck, hand):
		global playing    # to control upocming while loop

		while True:
			x = input('Hit or Stand? Enter h or s ')

			if x[0].lower() == 'h':
				hit(deck,hand)

			elif x[0].lower() == 's':
				print("Player Stands, Dealer's Turn")
				playing = False

			else:
				print("I did not understand that, Please enter h or s only: ")
				continue
			break









































