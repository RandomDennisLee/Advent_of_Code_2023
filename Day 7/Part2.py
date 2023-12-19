import operator


class Hand:
    def __init__(self):
        self.cards = []
        self.strength = 1
        self.my_set = []
        self.bid = 0

    def find_strength(self):
        self.my_set = set(self.cards)

        for each in self.my_set:
            if each != 1:
                count = self.cards.count(each)
                if count == 5:
                    self.strength = 7
                elif count == 4:
                    self.strength = 6
                elif (count == 3 and self.strength == 2) or (count == 2 and self.strength == 4):
                    self.strength = 5
                elif count == 3:
                    self.strength = 4
                elif count == 2 and self.strength == 2:
                    self.strength = 3
                elif count == 2:
                    self.strength = 2

        for each in range(self.cards.count(1)):
            if 4 >= self.strength >= 2:
                self.strength += 2
            elif self.strength < 7:
                self.strength += 1

        return self.strength

    def get_type(self):
        return self.types.get(self.strength)

    types = {1: 'single', 2: 'pair', 3: 'two pair', 4: '3 of a kind', 5: 'full house', 6: '4 of a kind', 7: '5 of a kind'}


if __name__ == '__main__':
    data = open('input.txt').readlines()
    face_card_values = {'A':14, 'K':13, 'Q':12, 'J':1, 'T':10}
    hands = []
    total_win = 0

    for line in data:
        hand = Hand()
        for each in line[0:5]:
            if each.isalpha():
                each = face_card_values.get (each)

            hand.cards.append (int (each))

        for token in line[6:len(line)].split():
            hand.bid = int(token)

        hand.find_strength()
        hands.append(hand)

    hands.sort (key = operator.attrgetter ('strength', 'cards'))
    for i in range(len(hands)):
        hand = hands[i]
        hand.bid = (i+1) * hand.bid
        total_win += hand.bid
        print ('Hand:', hand.cards, hand.get_type(), hand.bid, hand.strength)

    print (total_win)


