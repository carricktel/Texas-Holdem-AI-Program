
#-------------------------------------------------------------------------------
# Name:        Simple_Game_Loop
# Purpose:     basic game loop with text interface for Texas Hold'em game testing
#
# Author:      Joseph Carrick
#
# Created:     07/09/2015
#-------------------------------------------------------------------------------
from THAIP_Class_Card import Card
from THAIP_Class_Table import Table
from THAIP_Class_GamePhase import GamePhase
from THAIP_Class_DetermineHand import DetermineHand
from THAIP_Class_AI import AI
from THAIP_Class_GUI import GUI
import pygame
import time
import copy

#Instantiate a GUI object
gui = GUI()

#Instantiate a GamePhase object
phase = GamePhase()

#Instantiate a Table object
table = Table(25000,25000,150,phase)

#Instantiate an AI object
THAIP = AI(table,phase)

def Pause():

    raw_input("PRESS RETURN TO CONTINUE")

def Input_Action():
    """ PURPOSE: This function is called whenever an action is needed by a player.
                 If it is the human player's turn, a request is sent to the GUI
                 for an action input. If it is the AI's turn, the AI function
                 is called with the current game state info inserted as parameters.
                 The action returned by either player is returned back to the
                 game loop as 'Output' """

    if table.Action_To == 1:
        gui.buttons_on = True
        while gui.buttons_on == True and gui.launch == True:
            gui.exit_event()
            gui.draw_pokertable()
            gui.draw_preflop(table.Player_Cards)
            gui.draw_comcards(table.Community_Cards)
            gui.draw_stacks(table.Pot_Stack,table.AI_Stack,table.Player_Stack,table.Dealer_Button,table.Action_To)
#            gui.button_hover()
            if table.lastAction[1] == "Check" or table.lastAction[1] == "Fold" or table.lastAction[1] == "Call" or table.lastAction[1] == "":
                gui.check_event()
                gui.fold_event()
                gui.raise_event()
            if table.lastAction[1] == "Raise":
                gui.fold_event()
                gui.call_event()
                gui.raise_event()
            pygame.display.flip()
        theAction = gui.Action
##        theAction = raw_input("HUMAN PLAYER ACTION:")
        if theAction == "Raise":
            theAmount = int(raw_input("AMOUNT TO RAISE:"))
        elif theAction == "Call":
            theAmount = table.lastAction[2]
        elif theAction == "Check" or theAction == "Fold":
            theAmount = 0
##        else:
##            print " "
##            print "***INCORRECT INPUT***"
##            print " "
##
##            theAction = "Incorrect"
##            theAmount = 0

        Output = [1,theAction,theAmount]
#        Output = [1,"Check",0]
        return Output

    if table.Action_To == 2:
##        theAction = raw_input("AI PLAYER ACTION:")
##        if theAction == "Raise":
##            theAmount = int(raw_input("AMOUNT TO RAISE:"))
##        elif theAction == "Call":
##            theAmount = table.lastAction[2]
##        elif theAction == "Check" or theAction == "Fold":
##            theAmount = 0
##        else:
##            print " "
##            print "***INCORRECT INPUT***"
##            print " "
##
##            theAction = "Incorrect"
##            theAmount = 0
        print "The AI is thinking..."
        print " "
        gui.ai_dialog = "..."
        gui.draw_pokertable()
        gui.draw_preflop(table.Player_Cards)
        gui.draw_comcards(table.Community_Cards)
        gui.draw_stacks(table.Pot_Stack,table.AI_Stack,table.Player_Stack,table.Dealer_Button,table.Action_To)
        pygame.display.flip()
#        THAIP.Level_One_Algorithm()
        THAIP.Level_Two_Algorithm()
#        THAIP.Level_Three_Algorithm()
        Output = THAIP.action
        return Output


def Next_Phase():
    """ PURPOSE:  Checks the current phase of the game and advances
                  the phase appropiately."""
    fromRiver = False
    if phase.isRiver == True:
        phase.allToFalse()
        phase.isEnd_of_Hand = True
        fromRiver = True
    if phase.isTurn == True:
        phase.allToFalse()
        phase.isRiver = True
    if phase.isFlop == True:
        phase.allToFalse()
        phase.isTurn = True
    if phase.isPreFlop == True:
        phase.allToFalse()
        phase.isFlop = True
    if table.lastAction[1] == "Fold" or (phase.isEnd_of_Hand == True and fromRiver == False):
        phase.allToFalse()
        phase.isPreFlop = True
    fromRiver = False
    gui.exit_event()
    gui.draw_pokertable()
    gui.draw_preflop(table.Player_Cards)
    gui.draw_comcards(table.Community_Cards)
    gui.draw_stacks(table.Pot_Stack,table.AI_Stack,table.Player_Stack,table.Dealer_Button,table.Action_To)
    pygame.display.flip()
    gui.ai_dialog = ""
    gui.player_dialog = ""



def Raise(player,amount):
    """ PURPOSE:  Called by Call_Action() when the player or AI raises.
                  Updates the interface so the user can see that there has been
                  a raise, and how much has been raised. Takes raised amount of
                  chips from the raiser's stack and puts them into the pot stack.
                  Updates the Last_Action attribute of the Table object to
                  [player,"Raise",amount] where 'player' is 1 or 2 (1 for human
                  player, 2 for AI), and amount is an integer of the amount of
                  chips raised.
        CONTRACT: Raise : player, amount -> Table.Player_Stack,
                  Table.AI_Stack, Table.Pot_Stack, Table.Last_Action"""

    table.RaisePot += table.lastAction[2]

    # If the raise is by the human player, take the raised chips (plus the AI's raise if it did) out of his stack and move them to the pot.
    if player == 1:
        # If the raise is equal to the number of the AI's chips, then only raise that much, and declare all in.
        if amount >= table.AI_Stack+table.lastAction[2] or amount >= table.Player_Stack:
            if amount > table.Player_Stack:
                amount = table.Player_Stack-table.lastAction[2]
            if amount > table.AI_Stack and table.AI_Stack+table.lastAction[2] <= table.Player_Stack:
                amount = table.AI_Stack
            print " "
            print "Human player is all in for " + str(amount+table.RaisePot) + "!"
            print " "
            table.Pot_Stack += (amount+table.lastAction[2])
            table.Player_Stack -= (amount+table.lastAction[2])
            gui.player_dialog="All in!"
        # If the raise is not an all in move, then raise 'amount'.
        else:
            print " "
            print "Human player raises to " + str(amount+table.RaisePot) + "."
            print " "
            gui.player_dialog="Raise " + str(amount)
            table.Pot_Stack += (amount+table.lastAction[2])
            table.Player_Stack -= (amount+table.lastAction[2])

    # Same process as raise by human player, except for AI.
    if player == 2:
        if amount >= table.Player_Stack+table.lastAction[2] or amount >= table.AI_Stack:
            if amount > table.AI_Stack:
                amount = table.AI_Stack-table.lastAction[2]
            if amount > table.Player_Stack and table.Player_Stack+table.lastAction[2] <= table.AI_Stack:
                amount = table.Player_Stack
            print " "
            print "AI player is all in for " + str(amount+table.RaisePot) + "!"
            print " "
            gui.ai_dialog="All in!"
            table.Pot_Stack += (amount+table.lastAction[2])
            table.AI_Stack -= (amount+table.lastAction[2])

        else:
            print " "
            print "AI player raises to " + str(amount+table.RaisePot) + "."
            print " "
            gui.ai_dialog="Raise " + str(amount)
            table.Pot_Stack += (amount+table.lastAction[2])
            table.AI_Stack -= (amount+table.lastAction[2])

    #Change the last action to the player's raise, and the action goes to the opponent.
    table.lastAction = [player,"Raise",amount]
    table.Action_To = 3 - table.Action_To

    print " "
    print "PLAYER STACK: "+str(table.Player_Stack)
    print "AI STACK: "+str(table.AI_Stack)
    print " "



def Call(player):
    """ PURPOSE:  Called by Call_Action() when the player or AI calls.
                  Updates the interface so the user can see that there has been
                  a call, and how much has been called. Takes called amount of
                  chips from the caller's stack and puts them into the pot stack.
                  Updates the Last_Action attribute of the Table object to
                  [player,"Call",amount] where 'player' is 1 or 2 (1 for human
                  player, 2 for AI), and amount is an integer of the amount of
                  chips called. Calls Next_Phase() to advance the game phase.
        CONTRACT: Call : player -> Table.Player_Stack,
                  Table.AI_Stack, Table.Pot_Stack, Table.Last_Action"""

    # If the human player is calling, remove the called amount of chips from his stack and put them in the pot.
    amount = table.lastAction[2]
    if player == 1:
        if amount >= table.Player_Stack or amount >= table.AI_Stack:
            phase.isAllIn = True
        table.Pot_Stack += amount
        table.Player_Stack -= amount
        print " "
        print "Human player calls for " + str(amount) + "."
        print " "
        gui.player_dialog="Call"
    # Same as human player, except for AI player.
    if player == 2:
        if amount >= table.Player_Stack or amount >= table.AI_Stack:
            phase.isAllIn = True
        table.Pot_Stack += amount
        table.AI_Stack -= amount
        print " "
        print "AI player calls for " + str(amount) + "."
        print " "
        gui.ai_dialog="Call"
    # Advance to the next stage of play. If the call was in response to an all-in move, the next stage of play is the end of the hand.
    Next_Phase()
    table.Action_To = table.Dealer_Button

    # Change the last action to nothing.
    table.lastAction = [0,"",0]
    table.RaisePot = 0



def Check(player):
    """ PURPOSE:  Called by Call_Action() when the player or AI checks.
                  Updates the interface so the user can see that there has been
                  a check. Updates the Last_Action attribute of the Table object to
                  [player,"Check",0] where 'player' is 1 or 2 (1 for human
                  player, 2 for AI). Calls Next_Phase() to advance the game phase. """

    # If the player is checking after his opponent, move the game to the next state of play.
    if table.lastAction[1] == "Check":
        if player == 1:
            print " "
            print "Human player checks."
            print " "
            gui.player_dialog="Check"
        if player == 2:
            print " "
            print "AI player checks."
            print " "
            gui.ai_dialog="Check"

        Next_Phase()
        table.Action_To = table.Dealer_Button
        table.lastAction = [0,"",0]

    # If the player is trying to check after his opponent raised, raise an error.
    elif table.lastAction[1] == "Raise":
        print " "
        print "You do not have the option to check. You can either call, raise, or fold"
        print " "

    # If the player is first to check, then the state of play stays the same, and the action goes to his opponent.
    elif table.lastAction[1] != "Check" and table.lastAction[1] != "Raise":
        if player == 1:
            print " "
            print "Human player checks."
            print " "
            gui.player_dialog="Check"
        if player == 2:
            print " "
            print "AI player checks."
            print " "
            gui.ai_dialog="Check"
        table.Action_To = 3 - table.Action_To
        table.lastAction = [player,"Check",0]



def Fold(player):
    """ PURPOSE:  Called by Call_Action() when the player or AI folds.
                  Updates the interface so the user can see that there has been
                  a fold. Updates the Last_Action attribute of the Table object to
                  [player,"Fold",0] where 'player' is 1 or 2 (1 for human
                  player, 2 for AI). Calls Next_Phase() and Clear_Table() to
                  advance the game phase and clear the table to get ready for the
                  next hand. """

    # Give pot to opponent.
    if player == 1:
        print " "
        print "Human player folds."
        print " "
        gui.player_dialog="Fold"
        table.AI_Stack += table.Pot_Stack
    if player == 2:
        print " "
        print "AI player folds."
        print " "
        gui.ai_dialog="Fold"
        table.Player_Stack += table.Pot_Stack
    table.Pot_Stack = 0
    table.Action_To = table.Dealer_Button
    table.lastAction = [player,"Fold",0]
    Next_Phase()
    Clear_Table()



def Clear_Table():
    """ PURPOSE: Takes all of the cards in play (Table.Player_Cards,
                 Table.AI_Cards, and Table.Community_Cards) and
                 returns them to the deck (Table.Deck). Resets the
                 Table.Last_Action attribute to [0,"",0] indicating
                 that there was no previous action since a new hand
                 is starting. """

    # Put all of the cards back in the deck.
    for card in table.Player_Cards:
        table.Deck.append(card)
    for i in range(len(table.Player_Cards)):
        del table.Player_Cards[0]
    for card in table.AI_Cards:
        table.Deck.append(card)
    for i in range(len(table.AI_Cards)):
        del table.AI_Cards[0]
    for card in table.Community_Cards:
        table.Deck.append(card)
    for i in range(len(table.Community_Cards)):
        del table.Community_Cards[0]
    table.lastAction = [0,"",0]
    table.Dealer_Button = 3 - table.Dealer_Button

def Call_Action(action):
    """ PURPOSE:  Called in the game loop when an action is needed
                  by one of the players. Input_Action() is called first to
                  ask the player or AI for an input. The action that is returned
                  by Input_Action() is put into Call_Action(). Call_Action() then
                  calls Raise(), Call(), Check() or Fold() depending on what the
                  player inputed. """

    if action[1] == "Raise":
        Raise(action[0],action[2])
    if action[1] == "Call":
        Call(action[0])
    if action[1] == "Check":
        Check(action[0])
    if action[1] == "Fold":
        Fold(action[0])
    if action[1] == "Incorrect" or action[1] == "pass":
        pass

def Print_Preflop():
    """ PURPOSE:  Shuffles the deck, deals the players and updates the
                  interface (currently this is just text)."""

    gui.draw_pokertable()
    print "--------------------PRE FLOP--------------------"
    print " "
    print " "

    print "Shuffling deck ..."
    gui.dealer_dialog = "Shuffling deck ..."
    gui.show_dealer_dialog()
    gui.draw_stacks(table.Pot_Stack,table.AI_Stack,table.Player_Stack,table.Dealer_Button,table.Action_To)
    pygame.display.flip()
    print " "
    time.sleep(1.5)

    table.Shuffle_Deck()

    print "Dealing players ..."
    gui.dealer_dialog = "Dealing players ..."
    gui.draw_pokertable()
    gui.draw_stacks(table.Pot_Stack,table.AI_Stack,table.Player_Stack,table.Dealer_Button,table.Action_To)
    gui.show_dealer_dialog()
    pygame.display.flip()
    print " "
    time.sleep(1.5)

    table.Deal_Players()
    gui.draw_preflop(table.Player_Cards)

    print "HUMAN PLAYER:"
    print table.Player_Stack
    print " "
    for i in table.Player_Cards:
        i.ReturnAsString()
    print " "
    print "AI PLAYER:"
    print table.AI_Stack
    print " "
    for i in table.AI_Cards:
#        print "X"
        i.ReturnAsString()
    print " "
    print "COMMUNITY CARDS:"
    for i in range(5):
        print "X"
    print " "
    print "POT:"
    print table.Pot_Stack
    print " "
    print " "

def Print_Flop():
    """ PURPOSE:  Deals the flop cards and updates the interface
                  (currently this is just text)."""

    print "--------------------FLOP--------------------"
    print " "
    print " "

    table.Deal_Flop()
    gui.draw_comcards(table.Community_Cards)

    print "HUMAN PLAYER:"
    print " "
    print table.Player_Stack
    print " "
    for i in table.Player_Cards:
        i.ReturnAsString()
    print " "
    print "AI PLAYER:"
    print " "
    print table.AI_Stack
    print " "
    for i in table.AI_Cards:
#        print "X"
        i.ReturnAsString()
    print " "
    print "COMMUNITY CARDS:"
    for i in table.Community_Cards:
        if i != None:
            i.ReturnAsString()
    for i in range(2):
        print "X"
    print " "
    print "POT:"
    print table.Pot_Stack
    print " "
    print " "

def Print_Turn():
    """ PURPOSE:  Deals the turn card and updates the interface
                  (currently this is just text)."""

    print "--------------------TURN--------------------"
    print " "
    print " "

    table.Deal_Turn()
    gui.draw_comcards(table.Community_Cards)

    print "HUMAN PLAYER:"
    print " "
    print table.Player_Stack
    print " "
    for i in table.Player_Cards:
        i.ReturnAsString()
    print " "
    print "AI PLAYER:"
    print " "
    print table.AI_Stack
    print " "
    for i in table.AI_Cards:
#        print "X"
        i.ReturnAsString()
    print " "
    print "COMMUNITY CARDS:"
    for i in table.Community_Cards:
        if i != None:
            i.ReturnAsString()
    for i in range(1):
        print "X"
    print " "
    print "POT:"
    print table.Pot_Stack
    print " "
    print " "

def Print_River():
    """ PURPOSE:  Deals the river card and updates the interface
                  (currently this is just text)."""

    print "--------------------RIVER--------------------"
    print " "
    print " "

    table.Deal_River()
    gui.draw_comcards(table.Community_Cards)

    print "HUMAN PLAYER:"
    print " "
    print table.Player_Stack
    print " "
    for i in table.Player_Cards:
        i.ReturnAsString()
    print " "
    print "AI PLAYER:"
    print " "
    print table.AI_Stack
    print " "
    for i in table.AI_Cards:
#        print "X"
        i.ReturnAsString()
    print " "
    print "COMMUNITY CARDS:"
    for i in table.Community_Cards:
        i.ReturnAsString()
    print " "
    print "POT:"
    print table.Pot_Stack
    print " "
    print " "

def Print_Show():
    """ PURPOSE:  Updates the interface by showing of the cards in play
                  (currently this is just text)."""

    gui.draw_aicards(table.AI_Cards)
    pygame.display.flip()
    print "--------------------SHOW CARDS--------------------"
    print " "
    print " "
    print "HUMAN PLAYER:"
    print " "
    print table.Player_Stack
    print " "
    for i in table.Player_Cards:
        i.ReturnAsString()
    print " "
    print "AI PLAYER:"
    print " "
    print table.AI_Stack
    print " "
    for i in table.AI_Cards:
        i.ReturnAsString()
    print " "
    print "COMMUNITY CARDS:"
    for i in table.Community_Cards:
        i.ReturnAsString()
    print " "
    print "POT:"
    print table.Pot_Stack
    print " "
    print " "

def Determine_Winner():
    """ PURPOSE:  Creates two DetermineHand objects (one for each player).
                  The DetermineHand objects return the name of each player's
                  best hand, the cards that make up the best hands, and the
                  respective weights. The weights are compared to see which
                  player won the hand. The player that wins gets all of the
                  chips in Table.Pot_Stack. If there is a tie, the chips in
                  Table.Pot_Stack are split. """

    AI_Determine_Hand = DetermineHand(table.AI_Cards + table.Community_Cards)
    Player_Determine_Hand = DetermineHand(table.Player_Cards + table.Community_Cards)

    AI_Best_Hand_Name = AI_Determine_Hand.best_hand[0]
    table.AI_Best_Cards = AI_Determine_Hand.best_hand[1]
    AI_Best_Hand_Weight = AI_Determine_Hand.best_hand[2]

    Player_Best_Hand_Name = Player_Determine_Hand.best_hand[0]
    table.Player_Best_Cards = Player_Determine_Hand.best_hand[1]
    Player_Best_Hand_Weight = Player_Determine_Hand.best_hand[2]


    print " "
    print "Human Player has " + Player_Best_Hand_Name + ": " #+ table.Player_Best_Cards[0].ReturnAsShorthand() + " " + table.Player_Best_Cards[1].ReturnAsShorthand() + " " + table.Player_Best_Cards[2].ReturnAsShorthand() + " " + table.Player_Best_Cards[3].ReturnAsShorthand() + " " + table.Player_Best_Cards[4].ReturnAsShorthand()
    print " "
    for i in range(5):
        table.Player_Best_Cards[i].ReturnAsString()
    print " "
    print " "
    print "AI Player has " + AI_Best_Hand_Name + ": " #+ table.AI_Best_Cards[0].ReturnAsShorthand() + " " + table.AI_Best_Cards[1].ReturnAsShorthand() + " " + table.AI_Best_Cards[2].ReturnAsShorthand() + " " + table.AI_Best_Cards[3].ReturnAsShorthand() + " " + table.AI_Best_Cards[4].ReturnAsShorthand()
    print " "
    for i in range(5):
        table.AI_Best_Cards[i].ReturnAsString()
    print " "

    if Player_Best_Hand_Weight > AI_Best_Hand_Weight:
        table.Winner = 1
        table.Player_Stack += table.Pot_Stack
        table.Pot_Stack = 0
        print "Human Player wins hand"
        gui.dealer_dialog = "Human Player wins with " + Player_Best_Hand_Name
    elif Player_Best_Hand_Weight < AI_Best_Hand_Weight:
        table.Winner = 2
        table.AI_Stack += table.Pot_Stack
        table.Pot_Stack = 0
        print "AI Player wins hand"
        gui.dealer_dialog = "AI Player wins with " + AI_Best_Hand_Name
    elif Player_Best_Hand_Weight == AI_Best_Hand_Weight:
        table.Winner = 0
        table.Player_Stack += table.Pot_Stack/2
        table.AI_Stack += table.Pot_Stack/2
        table.Pot_Stack = 0
        print "It's a tie"
        gui.dealer_dialog = "It's a tie"

    gui.ai_dialog = AI_Best_Hand_Name
    gui.player_dialog = Player_Best_Hand_Name
    gui.draw_pokertable()
    gui.draw_preflop(table.Player_Cards)
    gui.draw_aicards(table.AI_Cards)
    gui.draw_comcards(table.Community_Cards)
    pygame.display.flip()
    time.sleep(3)

    gui.ai_dialog = ""
    gui.player_dialog = ""
    gui.draw_pokertable()
    gui.draw_preflop(table.Player_Best_Cards)
    gui.draw_aicards(table.AI_Best_Cards)
    gui.draw_stacks(table.Pot_Stack,table.AI_Stack,table.Player_Stack,table.Dealer_Button,table.Action_To)
    gui.show_dealer_dialog()
    pygame.display.flip()
    time.sleep(5)
#    THAIP.Update_TrendTracker()


def End_Game():
    """ PURPOSE:  Updates the interface to say which player won the game.
                  This fuction is only called if it has already been
                  determined that the game is over (when one of the players
                  runs out of chips. """
    print "--------------------GAME OVER---------------------"
    print ""
    print ""
    if table.AI_Stack == 0 and table.Winner == 1:
        gui.draw_pokertable()
        gui.dealer_dialog = "HUMAN PLAYER WINS!"
        print "----------------HUMAN PLAYER WINS-----------------"
    if table.Player_Stack == 0 and table.Winner == 2:
        gui.draw_pokertable()
        gui.dealer_dialog = "AI PLAYER WINS"
        print "-----------------AI PLAYER WINS-------------------"
    gui.draw_pokertable()
    gui.show_dealer_dialog()
    pygame.display.flip()
    time.sleep(2.5)
    gui.dealer_dialog = "  GAME OVER"
    gui.draw_pokertable()
    gui.show_dealer_dialog()
    pygame.display.flip()
    time.sleep(2.5)



#----------------------THE GAME LOOP------------------------#



while phase.isGame_Over == False and gui.launch == True:
    """ Game loop runs by continually checking to see which phase boolean
        is set to True and running the appropriate functions for that phase. """

##    if gui.menu_screen == True:
##        while gui.menu_screen == True and gui.launch == True:
##            gui.exit_event()
##            gui.draw_main_menu()
##            pygame.display.flip()
##        pygame.QUIT()


    action = [0,"pass",0]

    if phase.isPreFlop == True and table.lastAction[0] == 0:
        Print_Preflop()

    if phase.isPreFlop == True:
        if phase.isAllIn == True:
            Next_Phase()
        if phase.isAllIn == False:
            Call_Action(Input_Action())

    if phase.isFlop == True and table.lastAction[0] == 0:
        Print_Flop()

    if phase.isFlop == True:
        if phase.isAllIn ==True:
            Next_Phase()
        if phase.isAllIn == False:
            Call_Action(Input_Action())

    if phase.isTurn == True and table.lastAction[0] == 0:
        Print_Turn()

    if phase.isTurn == True:
        if phase.isAllIn ==True:
            Next_Phase()
        if phase.isAllIn == False:
            Call_Action(Input_Action())

    if phase.isRiver == True and table.lastAction[0] == 0:
        Print_River()

    if phase.isRiver == True:
        if phase.isAllIn ==True:
            Next_Phase()
        if phase.isAllIn == False:
            Call_Action(Input_Action())

    if phase.isEnd_of_Hand == True:

        Print_Show()
        Determine_Winner()
        Clear_Table()
        Next_Phase()
        if (table.AI_Stack == 0 or table.Player_Stack == 0) and phase.isAllIn == True:
            End_Game()
            phase.isGame_Over = True
        phase.isAllIn = False
    gui.exit_event()
    gui.draw_pokertable()
    gui.draw_preflop(table.Player_Cards)
    gui.draw_comcards(table.Community_Cards)
    gui.draw_stacks(table.Pot_Stack,table.AI_Stack,table.Player_Stack,table.Dealer_Button,table.Action_To)
    pygame.display.flip()

pygame.quit()




