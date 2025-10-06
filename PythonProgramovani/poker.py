import random

ZNAKY = ["♠", "♥", "♦", "♣"]
HODNOTY = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def balik(ZNAKY, HODNOTY):
    global deck
    deck = [f"{hodnota} of {znak}" for znak in ZNAKY for hodnota in HODNOTY]

def shuffle(deck):
    random.shuffle(deck) 

def vytahnout(deck):
    karta_dealt = deck.pop()
    print(karta_dealt)

def hrac_vytah(deck):
    print("Hrac vytahuje karty:")
    for _ in range(2):
        vytahnout(deck)

# balik(ZNAKY, HODNOTY)
# shuffle(deck)
# vytahnout(deck)
# hrac_vytah(deck)

def dealer_vytah_start(deck):
    print("Dealer vytahuje karty:")
    for _ in range(3):
        vytahnout(deck)
def dealer_vytah(deck):
    print("Dealer vytahuje dalsi kartu:")
    vytahnout(deck)


while True:
    balik(ZNAKY, HODNOTY)
    shuffle(deck)
    hrac_vytah(deck)
    dealer_vytah_start(deck)
    dealer_vytah(deck)
    dealer_vytah(deck)
    znovu = input("Chcete hrat znovu? (a/n): ")
    if znovu.lower() != 'a':
        print("Dekuji za hru!")
        break