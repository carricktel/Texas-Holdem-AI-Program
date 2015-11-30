#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      carricktel
#
# Created:     16/09/2015
# Copyright:   (c) carricktel 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from THAIP_Class_Card import Card
from THAIP_Class_DetermineHand import DetermineHand
card1 = Card(3,"Spades",1)
card2 = Card(9,"Spades",2)
card3 = Card(10,"Spades",3)
card4 = Card(11,"Spades",4)
card5 = Card(12,"Spades",5)
card6 = Card(13,"Spades",6)
card7 = Card(2,"Spades",7)

hand = DetermineHand([card1,card2,card3,card4,card5,card6,card7])
print hand.best_hand[0]
print " "
for i in hand.best_hand[1]:
    i.ReturnAsString()
print " "
print hand.best_hand[2]

##def findBestHand():
##    """ FIXME """
##    allhands = []
##    best_hand = [0,0,0]
##    for i in hand.Possible_Hands():
##        allhands.append([hand.findHandType(i), i, hand.WeightHand(i,hand.findHandType(i))])
##    for i in allhands:
##        if i[2] > best_hand[2]:
##            best_hand = i
##    return best_hand
##print findBestHand()[0]
##print hand.findStraight()
##print hand.findFlush()

##for i in hand.straights:
##    for j in i:
##        j.ReturnAsString()
##for i in hand.flushes:
##    for j in i:
##        j.ReturnAsString()
##print hand.isSameHand([card2,card3,card4,card5,card6],[card6,card2,card4,card3,card5])

##def findHandType():
##    if hand.findStraightFlush() == True:
##        return "straightflush"
##    if hand.findQuads() == True:
##        return "quads"
##    for i in hand.Possible_Hands():
##        if hand.findFullHouse(i) == True:
##            return "fullhouse"
##    if hand.findFlush() == True:
##        return "flush"
##    if hand.findStraight() == True:
##        return "straight"
##    if hand.findTrips() == True:
##        return "trips"
##    for i in hand.Possible_Hands():
##        if hand.findTwoPair(i) == True:
##            return "twopair"
##    if hand.findPair() == True:
##        return "pair"
##    else:
##        return "highcard"
##
##print findHandType()
##
##hand = DetermineHand([two,four,seven,ten,eight,queen,three])
##for i in hand.Rank_Cards(5,[two,four,seven,ten,eight,queen,three]):
##    i.ReturnAsString()

##def WeightHand(hand,handtype):
##    if handtype == "pair":
##        pair = []
##        for i in hand:
##            for j in hand:
##                if i > j and i.NumVal == j.NumVal:
##                    pair.append(i)
##                    pair.append(j)
##        for i in pair:
##            hand.remove(i)
##        for i in hand:
##            for j in hand:
##                for k in hand:
##                    if i.NumVal > j.NumVal and j.NumVal > k.NumVal:
##                        weight = float(2) + (float(pair[0].NumVal))*0.01 + (float(pair[1].NumVal))*0.0001 + (float(i.NumVal))*0.000001 + (float(j.NumVal))*0.00000001 + (float(k.NumVal))*0.0000000001
##
##    if handtype == "twopair":
##        weight = float(3)
##        pair1 = []
##        pair2 = []
##
##        breakloop = False
##        for i in hand:
##            for j in hand:
##                if i > j and i.NumVal == j.NumVal:
##                    pair1.append(i)
##                    pair1.append(j)
##                    breakloop = True
##                    break
##            if breakloop == True:
##                break
##
##        for i in pair1:
##            hand.remove(i)
##
##        for i in hand:
##            for j in hand:
##                if i > j and i.NumVal == j.NumVal:
##                    pair2.append(i)
##                    pair2.append(j)
##        for i in pair2:
##            hand.remove(i)
##
##        if pair1[0].NumVal > pair2[0].NumVal:
##            weight += (float(pair1[0].NumVal))*0.01 + (float(pair1[1].NumVal))*0.0001 + (float(pair2[0].NumVal))*0.000001 + (float(pair2[1].NumVal))*0.00000001 + (float(hand[0].NumVal))*0.0000000001
##        if pair1[0].NumVal < pair2[0].NumVal:
##            weight += (float(pair2[0].NumVal))*0.01 + (float(pair2[1].NumVal))*0.0001 + (float(pair1[0].NumVal))*0.000001 + (float(pair1[1].NumVal))*0.00000001 + (float(hand[0].NumVal))*0.0000000001
##        return weight
##
##    if handtype == "trips":
##        trips = []
##        for i in hand:
##            for j in hand:
##                if j > i and i.NumVal == j.NumVal:
##                    for k in hand:
##                        if k > j and i.NumVal == k.NumVal:
##                            trips.append(i)
##                            trips.append(j)
##                            trips.append(k)
##        for i in trips:
##            hand.remove(i)
##
##        for i in hand:
##            for j in hand:
##                if i.NumVal > j.NumVal:
##                    weight = float(4) + float(trips[0].NumVal)*0.01 + float(trips[1].NumVal)*0.0001 + float(trips[2].NumVal)*0.000001 + float(i.NumVal)*0.00000001 + float(j.NumVal)*0.0000000001
##        return weight
##
##    if handtype == "quads":
##        quads = []
##        for i in hand:
##            for j in hand:
##                if j > i and i.NumVal == j.NumVal:
##                    for k in hand:
##                        if k > j and i.NumVal == k.NumVal:
##                            for l in hand:
##                                if l > k and i.NumVal == k.NumVal:
##                                    quads.append(i)
##                                    quads.append(j)
##                                    quads.append(k)
##                                    quads.append(l)
##        for i in quads:
##            hand.remove(i)
##
##        weight = float(8) + float(quads[0].NumVal)*0.01 + float(quads[1].NumVal)*0.0001 + float(quads[2].NumVal)*0.000001 + float(quads[3].NumVal)*0.00000001 + float(hand[0].NumVal)*0.0000000001
##        return weight
##
##    if handtype == "fullhouse":
##        trips = []
##        for i in hand:
##            for j in hand:
##                if j > i and i.NumVal == j.NumVal:
##                    for k in hand:
##                        if k > j and i.NumVal == k.NumVal:
##                            trips.append(i)
##                            trips.append(j)
##                            trips.append(k)
##        for i in trips:
##            hand.remove(i)
##        weight = float(7) + float(trips[0].NumVal)*0.01 + float(trips[1].NumVal)*0.0001 + float(trips[2].NumVal)*0.000001 + float(hand[0].NumVal)*0.00000001 + float(hand[1].NumVal)*0.0000000001
##        return weight
##    if handtype == "straightflush":
##        weight = float(9)
##    if handtype == "flush":
##        weight = float(6)
##    if handtype == "straight":
##        weight = float(5)
##    if handtype == "highcard":
##        weight = float(1)
##
##    for i in hand:
##        for j in hand:
##            for k in hand:
##                for l in hand:
##                    for m in hand:
##                        if i.NumVal > j.NumVal and j.NumVal > k.NumVal and k.NumVal > l.NumVal and l.NumVal > m.NumVal:
##                            weight += float(i.NumVal)*0.01 + float(j.NumVal)*0.0001 + float(k.NumVal)*0.000001 + float(l.NumVal)*0.00000001 + float(m.NumVal)*0.0000000001
##                            return weight
##print WeightHand([card1,card2,card3,card4,card5],"highcard")

