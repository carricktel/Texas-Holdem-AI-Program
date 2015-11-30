#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      carricktel
#
# Created:     29/09/2015
# Copyright:   (c) carricktel 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from THAIP_Class_Card import Card
from THAIP_Class_DetermineHand import DetermineHand
from THAIP_Class_Table import Table
import itertools

class HandStrengthGen:

    def __init__(self,hand):
        self.hand = hand
        self.table = Table(0,0,0)
        self.table2 = Table(0,0,0)
        self.table3 = Table(0,0,0)
        self.hand = hand
        for card in self.table.Deck:
            if card.ID == self.hand[0].ID or card.ID == self.hand[1].ID:
                self.table.AI_Cards.append(self.table.Deck.pop(self.table.Deck.index(card)))
        for card in self.table2.Deck:
            if card.ID == self.hand[0].ID or card.ID == self.hand[1].ID:
                self.table2.Deck.remove(card)
        for card in self.table3.Deck:
            if card.ID == self.hand[0].ID or card.ID == self.hand[1].ID:
                self.table3.Deck.remove(card)


    def GenPreflopHS(self):
        """We don't want to mess up the previous iteration by taking a card out of the list being iterated on"""
        """remember to put the cards back into table2 and table3"""
        """ FIXME """
        wins = 0
        total = 0
        player_combinations = itertools.combinations(self.table.Deck,2)
        for i in player_combinations: # ((K!,10%),(3@,4!),(6#,Q!),.....)
            for card in self.table.Deck:
                if card.ID == i[0].ID or card.ID == i[1].ID:
                    self.table.Player_Cards.append(self.table.Deck.pop(self.table.Deck.index(card)))
            for card in self.table.Deck:
                if card.ID == i[0].ID or card.ID == i[1].ID:
                    self.table3.Deck.remove(card)
            for j in itertools.combinations(self.table.Deck,5):
                for card in self.table.Deck:
                    if card.ID == j[0].ID or card.ID == j[1].ID or card.ID == j[2].ID or card.ID == j[3].ID or card.ID == j[4].ID:
                        self.table.Community_Cards.append(self.table3.Deck.pop(self.table3.Deck.index(card)))
                #Now the table's cards are full (player, ai, and community)
                AI_Determine_Hand = DetermineHand(self.table.AI_Cards + self.table.Community_Cards)
                Player_Determine_Hand = DetermineHand(self.table.Player_Cards + self.table.Community_Cards)

                AI_Best_Hand_Weight = AI_Determine_Hand.best_hand[2]

                Player_Best_Hand_Weight = Player_Determine_Hand.best_hand[2]


                if Player_Best_Hand_Weight > AI_Best_Hand_Weight:
                    total += 1
                elif Player_Best_Hand_Weight < AI_Best_Hand_Weight or Player_Best_Hand_Weight == AI_Best_Hand_Weight:
                    total += 1
                    wins += 1
                for k in self.table.Community_Cards:
                    self.table.Deck.append(self.table.Community_Cards.pop(self.table.Community_Cards.index(k)))
                print wins/total
            for j in self.table.Player_Cards:
                self.table2.append(self.table.Player_Cards.pop(self.table.Player_Cards.index(j)))





##        print "It's a tie"


thisHand = HandStrengthGen([Card(4,"Hearts",3),Card(13,"Hearts",12)])
thisHand.GenPreflopHS()

