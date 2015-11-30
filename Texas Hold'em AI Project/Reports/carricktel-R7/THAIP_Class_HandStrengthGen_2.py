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
import random

class HandStrengthGen:

    def __init__(self):
        self.AItable = Table(0,0,0)
        self.COMtable = Table(0,0,0)
        self.PLYRtable = Table(0,0,0)

        self.AItable.Deck = [Card(2,"Hearts",1),Card(3,"Hearts",2),Card(4,"Hearts",3),Card(5,"Hearts",4),
                    Card(6,"Hearts",5),Card(7,"Hearts",6),Card(8,"Hearts",7),Card(9,"Hearts",8),
                    Card(10,"Hearts",9),Card(11,"Hearts",10),Card(12,"Hearts",11),Card(13,"Hearts",12),
                    Card(14,"Hearts",13),Card(2,"Diamonds",14),Card(3,"Diamonds",15),Card(4,"Diamonds",16),
                    Card(5,"Diamonds",17),Card(6,"Diamonds",18),Card(7,"Diamonds",19),Card(8,"Diamonds",20),
                    Card(9,"Diamonds",21),Card(10,"Diamonds",22),Card(11,"Diamonds",23),Card(12,"Diamonds",24),
                    Card(13,"Diamonds",25),Card(14,"Diamonds",26)]
        random.shuffle(self.AItable.Deck)
        random.shuffle(self.COMtable.Deck)
        random.shuffle(self.PLYRtable.Deck)

        self.wins = 0
        self.total = 0

    def Reset_Deck(self,table):
        table.Deck =[Card(2,"Hearts",1),Card(3,"Hearts",2),Card(4,"Hearts",3),Card(5,"Hearts",4),
                    Card(6,"Hearts",5),Card(7,"Hearts",6),Card(8,"Hearts",7),Card(9,"Hearts",8),
                    Card(10,"Hearts",9),Card(11,"Hearts",10),Card(12,"Hearts",11),Card(13,"Hearts",12),
                    Card(14,"Hearts",13),Card(2,"Diamonds",14),Card(3,"Diamonds",15),Card(4,"Diamonds",16),
                    Card(5,"Diamonds",17),Card(6,"Diamonds",18),Card(7,"Diamonds",19),Card(8,"Diamonds",20),
                    Card(9,"Diamonds",21),Card(10,"Diamonds",22),Card(11,"Diamonds",23),Card(12,"Diamonds",24),
                    Card(13,"Diamonds",25),Card(14,"Diamonds",26),Card(2,"Clubs",27),Card(3,"Clubs",28),
                    Card(4,"Clubs",29),Card(5,"Clubs",30),Card(6,"Clubs",31),Card(7,"Clubs",32),
                    Card(8,"Clubs",33),Card(9,"Clubs",34),Card(10,"Clubs",35),Card(11,"Clubs",36),
                    Card(12,"Clubs",37),Card(13,"Clubs",38),Card(14,"Clubs",39),Card(2,"Spades",40),
                    Card(3,"Spades",41),Card(4,"Spades",42),Card(5,"Spades",43),Card(6,"Spades",44),
                    Card(7,"Spades",45),Card(8,"Spades",46),Card(9,"Spades",47),Card(10,"Spades",48),
                    Card(11,"Spades",49),Card(12,"Spades",50),Card(13,"Spades",51),Card(14,"Spades",52)]


        random.shuffle(table.Deck)

    def Next_AI_2cards(self):
        """Generates every 2 card combination in the AItable.deck, and yields
           them one at a time into to a list.
           --> [3h,Qc] ..."""

        for i in itertools.combinations(self.AItable.Deck,2):
            yield i



    def Next_COM_5cards(self,aicards):
        """Generates every 5 card combination in the COMtable.deck with the
           exception of the cards in the list aicards, and yields
           them one at a time into a list.
           [3h,Qc] --> [2h,4h,9s,Jc,Kc] ... """

        card_to_remove1 = False
        card_to_remove2 = False
        for card in self.COMtable.Deck:
            if card.ID == aicards[0].ID:
                card_to_remove1 = card
            if card.ID == aicards[1].ID:
                card_to_remove2 = card
            if card_to_remove1 != False and card_to_remove2 != False:
                break
        self.COMtable.Deck.remove(card_to_remove1)
        self.COMtable.Deck.remove(card_to_remove2)

        cardsets = []
        for i in itertools.combinations(self.COMtable.Deck,5):
##            cardsets.append(i)
##        random.shuffle(cardsets)
##        for i in cardsets:
            yield i

    def Next_COM_2cards(self,aicards,comcards):
        """Generates every 2 card combination in the COMtable.deck with the
           exception of the cards in the lists aicards and flopcards, and yields
           them one at a time into comcards.
           [3h,Qc],[2h,4h,9s] --> [2h,4h,9s,Jc,Kc] ... """
        card_to_remove1 = False
        card_to_remove2 = False
        card_to_remove3 = False
        card_to_remove4 = False
        card_to_remove5 = False

        for card in self.COMtable.Deck:
            if card.ID == aicards[0].ID:
                card_to_remove1 = card
            if card.ID == aicards[1].ID:
                card_to_remove2 = card
            if card.ID == comcards[0].ID:
                card_to_remove3 = card
            if card.ID == comcards[1].ID:
                card_to_remove4 = card
            if card.ID == comcards[2].ID:
                card_to_remove5 = card
            if card_to_remove1 != False and card_to_remove2 != False and card_to_remove3 != False and card_to_remove4 != False and card_to_remove5 != False:
                break
        self.COMtable.Deck.remove(card_to_remove1)
        self.COMtable.Deck.remove(card_to_remove2)
        self.COMtable.Deck.remove(card_to_remove3)
        self.COMtable.Deck.remove(card_to_remove4)
        self.COMtable.Deck.remove(card_to_remove5)

        flopcards = (card_to_remove3,card_to_remove4,card_to_remove5)
        cardpairs = []
        for i in itertools.combinations(self.COMtable.Deck,2):
            cardpairs.append(i)
        random.shuffle(cardpairs)
        for i in cardpairs:
            yield flopcards+i

    def Next_COM_1cards(self,aicards,comcards):
        """Generates every 2 card combination in the COMtable.deck with the
           exception of the cards in the lists aicards and flopcards, and yields
           them one at a time into comcards.
           [3h,Qc],[2h,4h,9s] --> [2h,4h,9s,Jc,Kc] ... """
        card_to_remove1 = False
        card_to_remove2 = False
        card_to_remove3 = False
        card_to_remove4 = False
        card_to_remove5 = False
        card_to_remove6 = False

        for card in self.COMtable.Deck:
            if card.ID == aicards[0].ID:
                card_to_remove1 = card
            if card.ID == aicards[1].ID:
                card_to_remove2 = card
            if card.ID == comcards[0].ID:
                card_to_remove3 = card
            if card.ID == comcards[1].ID:
                card_to_remove4 = card
            if card.ID == comcards[2].ID:
                card_to_remove5 = card
            if card.ID == comcards[3].ID:
                card_to_remove6 = card
            if card_to_remove1 != False and card_to_remove2 != False and card_to_remove3 != False and card_to_remove4 != False and card_to_remove5 != False and card_to_remove6 != False:
                break
        self.COMtable.Deck.remove(card_to_remove1)
        self.COMtable.Deck.remove(card_to_remove2)
        self.COMtable.Deck.remove(card_to_remove3)
        self.COMtable.Deck.remove(card_to_remove4)
        self.COMtable.Deck.remove(card_to_remove5)
        self.COMtable.Deck.remove(card_to_remove6)

        turncards = (card_to_remove3,card_to_remove4,card_to_remove5,card_to_remove6)
        for i in self.COMtable.Deck:
            yield turncards+(i,)




    def Next_PLYR_2cards(self,aicards,comcards):
        """Generates every 2 card combination in the PLYRtable.deck with the
           exception of the cards in the lists aicards and comcards, and yields
           them one at a time into a list.
           [3h,Qc],[2h,4h,9s,Jc,Kc] --> [5h,Ac] ... """

        card_to_remove1 = False
        card_to_remove2 = False
        card_to_remove3 = False
        card_to_remove4 = False
        card_to_remove5 = False
        card_to_remove6 = False
        card_to_remove7 = False

        for card in self.PLYRtable.Deck:
            if card.ID == aicards[0].ID:
                card_to_remove1 = card
            if card.ID == aicards[1].ID:
                card_to_remove2 = card
            if card.ID == comcards[0].ID:
                card_to_remove3 = card
            if card.ID == comcards[1].ID:
                card_to_remove4 = card
            if card.ID == comcards[2].ID:
                card_to_remove5 = card
            if card.ID == comcards[3].ID:
                card_to_remove6 = card
            if card.ID == comcards[4].ID:
                card_to_remove7 = card
            if card_to_remove1 != False and card_to_remove2 != False and card_to_remove3 != False and card_to_remove4 != False and card_to_remove5 != False and card_to_remove6 != False and card_to_remove7 != False:
                break
        self.PLYRtable.Deck.remove(card_to_remove1)
        self.PLYRtable.Deck.remove(card_to_remove2)
        self.PLYRtable.Deck.remove(card_to_remove3)
        self.PLYRtable.Deck.remove(card_to_remove4)
        self.PLYRtable.Deck.remove(card_to_remove5)
        self.PLYRtable.Deck.remove(card_to_remove6)
        self.PLYRtable.Deck.remove(card_to_remove7)

        cardpairs = []
        for i in itertools.combinations(self.PLYRtable.Deck,2):
            cardpairs.append(i)
        random.shuffle(cardpairs)
        for i in cardpairs:
            yield i

    def Determine_Winner(self,aicards,comcards,plyrcards):
        """ Returns the winner of one hand scenario. 1 for AI, 0 for opponent.
            [3h,Qc],[2h,4h,9s,Jc,Kc],[5h,Ac] --> 0"""

        AI_Determine_Hand = DetermineHand(aicards + comcards)
        Player_Determine_Hand = DetermineHand(plyrcards + comcards)

        AI_Best_Hand_Weight = AI_Determine_Hand.best_hand[2]
        Player_Best_Hand_Weight = Player_Determine_Hand.best_hand[2]

        if AI_Best_Hand_Weight > Player_Best_Hand_Weight:
            self.wins += 1
            self.total += 1
        if AI_Best_Hand_Weight < Player_Best_Hand_Weight:
            self.total += 1


    def PreflopHS(self,aicards,iterations,oppon_hand_iters,runs):
        count = 0
        meanlist = []
        for g in range(runs):
            for z in range(iterations):
                for j in self.Next_COM_5cards(aicards):
                    for k in self.Next_PLYR_2cards(aicards,j):
                        count += 1
                        self.Determine_Winner(aicards,j,k)
                        if count == oppon_hand_iters:
                            break
                    self.Reset_Deck(self.PLYRtable)
                    if count == oppon_hand_iters:
                        break
                count = 0
                self.Reset_Deck(self.COMtable)

            print str(iterations*oppon_hand_iters) + " total"
            print str(iterations) + " opponent hands for 1 community card set"
            print (str((float(self.wins)/float(self.total))*100))+"%"
            print " "
            meanlist.append((float(self.wins)/float(self.total))*100)
            self.wins = 0
            self.total = 0
        thesum = 0
        for i in meanlist:
            print i
            thesum+=i
        print "Average: "+str(float(thesum)/float(runs))
        return float(thesum)/float(runs)



    def FlopHS(self,aicards,comcards,iterations,oppon_hand_iters,runs):
        count = 0
        meanlist = []
        for g in range(runs):
            for z in range(iterations):
                for j in self.Next_COM_2cards(aicards,comcards):
                    for k in self.Next_PLYR_2cards(aicards,j):
                        count += 1
                        self.Determine_Winner(aicards,j,k)
                        if count == oppon_hand_iters:
                            break
                    self.Reset_Deck(self.PLYRtable)
                    if count == oppon_hand_iters:
                        break
                count = 0
                self.Reset_Deck(self.COMtable)

            print str(iterations*oppon_hand_iters) + " total"
            print str(oppon_hand_iters) + " opponent hands for 1 community card set"
            print (str((float(self.wins)/float(self.total))*100))+"%"
            print " "
            meanlist.append((float(self.wins)/float(self.total))*100)
            self.wins = 0
            self.total = 0
        thesum = 0
        for i in meanlist:
            print i
            thesum+=i
        print "Average: "+str(float(thesum)/float(runs))
        return float(thesum)/float(runs)

    def TurnHS(self,aicards,comcards,iterations,oppon_hand_iters,runs):
        count = 0
        meanlist = []
        for g in range(runs):
            for z in range(iterations):
                for j in self.Next_COM_1cards(aicards,comcards):
                    for k in self.Next_PLYR_2cards(aicards,j):
                        count += 1
                        self.Determine_Winner(aicards,j,k)
                        if count == oppon_hand_iters:
                            break
                    self.Reset_Deck(self.PLYRtable)
                    if count == oppon_hand_iters:
                        break
                count = 0
                self.Reset_Deck(self.COMtable)

            print str(iterations*oppon_hand_iters) + " total"
            print str(oppon_hand_iters) + " opponent hands for 1 community card set"
            print (str((float(self.wins)/float(self.total))*100))+"%"
            print " "
            meanlist.append((float(self.wins)/float(self.total))*100)
            self.wins = 0
            self.total = 0
        thesum = 0
        for i in meanlist:
            print i
            thesum+=i
        print "Average: "+str(float(thesum)/float(runs))
        return float(thesum)/float(runs)

    def RiverHS(self,aicards,comcards,oppon_hand_iters,runs):
        count = 0
        meanlist = []
        for g in range(runs):
            for k in self.Next_PLYR_2cards(aicards,comcards):
                count += 1
                self.Determine_Winner(aicards,comcards,k)
                if count == oppon_hand_iters:
                    break
            count = 0
            self.Reset_Deck(self.PLYRtable)
            print str(oppon_hand_iters) + " total"
            print (str((float(self.wins)/float(self.total))*100))+"%"
            print " "
            meanlist.append((float(self.wins)/float(self.total))*100)
            self.wins = 0
            self.total = 0
        thesum = 0
        for i in meanlist:
            print i
            thesum+=i
        print "Average: "+str(float(thesum)/float(runs))
        return float(thesum)/float(runs)


aicards1 = (Card(13,"Diamonds",25),Card(3,"Hearts",2))
comcards1 = (Card(11,"Diamonds",23),Card(8,"Hearts",7),Card(9,"Hearts",8))
comcards2 = (Card(11,"Hearts",10),Card(7,"Diamonds",19),Card(12,"Diamonds",24),Card(5,"Spades",43))
comcards3 = (Card(11,"Hearts",10),Card(7,"Diamonds",19),Card(12,"Diamonds",24),Card(5,"Spades",43),Card(3,"Clubs",28))
iterations1 = 40
oppon_hand_iters1 = 1
runs1 = 1

this = HandStrengthGen()
#this.PreflopHS(aicards1,iterations1,oppon_hand_iters1,runs1)
#this.FlopHS(aicards1,comcards1,iterations1,oppon_hand_iters1,runs1)
this.TurnHS(aicards1,comcards2,iterations1,oppon_hand_iters1,runs1)
#this.RiverHS(aicards1,comcards3,oppon_hand_iters1,runs1)






#for i in this.Next_AI_2cards():

##iterations = 1000
##oppon_hand_iters = 5
##for z in range(iterations):
##    i = (Card(13,"Hearts",12),Card(14,"Hearts",13))
##    for j in this.Next_COM_5cards(i):
##        for k in this.Next_PLYR_2cards(i,j):
##            count += 1
##            this.Determine_Winner(i,j,k)
##            if count == oppon_hand_iters:
####                print "count "+str(5) + ": " + (str((float(this.wins)/float(this.total))*100))+"%"
####                meanlist.append((float(this.wins)/float(this.total))*100)
##                break
##        this.Reset_Deck(this.PLYRtable)
##        if count == oppon_hand_iters:
##            break
##    count = 0
##    this.Reset_Deck(this.COMtable)
##
##print str(iterations*oppon_hand_iters) + " total"
##print str(oppon_hand_iters) + " opponent hands for 1 community card set"
##print (str((float(this.wins)/float(this.total))*100))+"%"





##if count == 10:
##    break

##i = (Card(10,"Clubs",35),Card(11,"Clubs",36))
##j = (Card(6,"Diamonds",18),Card(2,"Hearts",1),Card(14,"Clubs",39),Card(3,"Spades",41),Card(11,"Hearts",10))
##
##for k in this.Next_PLYR_2cards(i,j):
##    count += 1
##    this.Determine_Winner(i,j,k)
##    if count == 300:
##        print (str((float(this.wins)/float(this.total))*100))+"%"
##        break






