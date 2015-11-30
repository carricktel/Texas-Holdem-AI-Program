#-------------------------------------------------------------------------------
# Name:        Simple_Server
# Purpose:     Originally, this program was going to be a server program that would
#              run the connection to a client and the AI software, but this is now
#              a RELIC OF THE PAST. No communication is needed between a server and
#              client. If there is a need to download a client, the whole program can
#              be downloaded, and this would avoid a lot of hassle.
#              This file is also in a FIXME state because it was realized half way through it's
#              creation that this attempt was pointless, and was consequently dropped
#              immediately.
#
# Author:      carricktel
#
# Created:     03/10/2015
# Copyright:   (c) carricktel 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import socket
from THAIP_Class_AI import AI
from THAIP_Class_Table import Table
from THAIP_Class_Card import Card
from THAIP_Class_DetermineHand import DetermineHand


Host = ''
Port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

def Construct_Cards(cardstr,comstr,tableinst):


    cardlist = cardstr.split("*")
    comlist = cardstr.split("*")
    for card in tableinst.Deck:
        for card2 in cardlist:
            if card.ID == card2:
                tableinst.AI_Cards.append(card)
                tableinst.Deck.remove(card)
        for card2 in comlist:
            if card.ID == card2:
                tableinst.Community_Cards.append(card)
                tableinst.Deck.remove(card)

def Construct_Lastaction(actionstr,tableinst):



def Construct_Table(tablestr):
    """ Takes in a string of Table attributes and reconstructs them
        as Table attributes of an instance called 'table'. Returns
        the Table object."""

    print tablestr
    tablelist = tablestr.split("|")
    table = Table(tablelist[1],tablelist[6],tablelist[9])
    Construct_AI_Cards(tablelist[0],tablelist[3],table)
    table.BB = tablelist[2]
    table.Dealer_Button = tablelist[4]
    table.lastAction = tablelist[5]
    table.Pot_Stack = tablelist[7]
    table.Round = tablelist[8]
    return table

def Deconstruct_AI_Action(actionlist):
    """Takes in the AI's action (ex: [0,Raise,75]), and returns
        a string representing the aciton (ex: "0|Raise|0") so it
        can be sent through the server socket."""

    actionstr = ""
    for i in actionlist:
        actionstr += str(i) + "|"
    actionstr = actionstr[:-1]
    return actionstr

while 1:
    table = conn.recv(1024)
    if repr(table) == "close":
        break
    theAI = AI(Construct_Table(table))
    theAI.Run_Draft_Algorithm()
    AI_response = Deconstruct_AI_Action(AI.action)
    conn.sendall(AI_response)
conn.close()
