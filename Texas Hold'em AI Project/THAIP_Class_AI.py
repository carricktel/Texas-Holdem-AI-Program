#-------------------------------------------------------------------------------
# Name:        THAIP_Class_AI
# Purpose:     Contains algorithms to determine the AI's actions in THAIP program
#
# Author:      carricktel
#
# Created:     23/09/2015
# Copyright:   (c) carricktel 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from THAIP_Class_Table import Table
from THAIP_Class_HandStrengthGen_2 import HandStrengthGen
from THAIP_Class_TrendTracker import TrendTracker

class AI:

    def __init__(self,table,phase):
        self.trendtracker = TrendTracker(None)
        self.HS_Gen = HandStrengthGen()
        self.phase = phase
        self.table = table
        self.action = [0,"",0]
        self.hs = 0
        self.opponhs = 0
        self.betsize = 0

    def Determine_HS(self):
        """PURPOSE: Calls HandStrengthGen object to calculate the AI's
                    handstrength given the current hand."""

        aicards = tuple(self.table.AI_Cards)
        comcards = tuple(self.table.Community_Cards)

        if len(self.table.Community_Cards) == 0:
            self.hs = self.HS_Gen.PreflopHS(aicards,40,1,1)

        if len(self.table.Community_Cards) == 3:
#            print self.table.Community_Cards
            self.hs = self.HS_Gen.FlopHS(aicards,comcards,40,1,1)

        if len(self.table.Community_Cards) == 4:
            self.hs = self.HS_Gen.TurnHS(aicards,comcards,40,1,1)

        if len(self.table.Community_Cards) == 5:
            self.hs = self.HS_Gen.RiverHS(aicards,comcards,40,1)

    def Determine_Opponent_HS(self):
        """PURPOSE: Guesses the opponent's hand strength based on the amount
                    bet. Can only be called after opponent raises."""

        betsize = self.table.lastAction[2]
        self.opponhs = (betsize)*(100)/(self.table.Pot_Stack + betsize)

    def Determine_Betsize(self):

        print "HS: " + str(self.hs)
        pot = self.table.Pot_Stack
        print "pot: " + str(pot)
        self.betsize = (self.hs*pot)/(101-self.hs)
        print "betsize: " + str(self.betsize)
        print ""

    def Update_TrendTracker(self):
        """ PURPOSE:  Called when the cards are shown at the end of a hand to
                      compare how the opponent played his hand in every phase
                      versus how the AI thought he would play. TrendTracker is
                      called to update the hand strength adjustment value."""

        if self.trendtracker.Played_PF_HS != 0:
            pfhs = self.HS_Gen.PreflopHS(tuple(self.table.Player_Cards),40,1,1)
#            print "played: " + str(self.trendtracker.Played_PF_HS)
            self.trendtracker.Adjust_PF_HS(pfhs,self.trendtracker.Played_PF_HS)

        if self.trendtracker.Played_F_HS != 0:
            fhs = self.HS_Gen.FlopHS(tuple(self.table.Player_Cards),tuple(self.table.Community_Cards[2:]),40,1,1)
 #           print "played: " + str(self.trendtracker.Played_F_HS)
            self.trendtracker.Adjust_F_HS(fhs,self.trendtracker.Played_F_HS)

        if self.trendtracker.Played_T_HS != 0:
            ths = self.HS_Gen.TurnHS(tuple(self.table.Player_Cards),tuple(self.table.Community_Cards[1:]),40,1,1)
 #           print "played: " + str(self.trendtracker.Played_T_HS)
            self.trendtracker.Adjust_T_HS(ths,self.trendtracker.Played_T_HS)

        if self.trendtracker.Played_R_HS != 0:
            rhs = self.HS_Gen.RiverHS(tuple(self.table.Player_Cards),tuple(self.table.Community_Cards),40,1)
 #           print "played: " + str(self.trendtracker.Played_R_HS)
            self.trendtracker.Adjust_R_HS(rhs,self.trendtracker.Played_R_HS)

        self.trendtracker.Reset_Played_HS()

    def Level_One_Algorithm(self):
        """ PURPOSE:  Looks at the state of the table and follows the draft
                      algorithm to determine what action to play. The algorithm
                      is very simple: If the opponent raised, then call. If the
                      opponent checked, folded, or called, then check. """

        if self.table.lastAction[1] == "Raise":
            self.action = [2,"Call",self.table.lastAction[2]]
        if self.table.lastAction[1] == "Check" or self.table.lastAction[1] == "Fold" or self.table.lastAction[1] == "Call" or self.table.lastAction[1] == "" or self.table.lastAction[1] == "pass":
            self.action = [2,"Check",0]

    def Level_Two_Algorithm(self):
        """ PURPOSE:  Given the strength of current hand and the pot odds,
                      the algorithm calculates the most profitalbe bet or
                      call size."""

        self.Determine_HS()
        self.Determine_Betsize()

        if self.table.lastAction[1] == "Raise":
            if self.betsize < self.table.lastAction[2]:
                self.action = [2,"Fold",0]
            if (self.betsize >= self.table.lastAction[2] and self.betsize < 2*int(self.table.lastAction[2])) or (self.betsize >= self.table.lastAction[2] and self.phase.isAllIn == True):
                self.action = [2,"Call",self.table.lastAction[2]]
            if self.betsize >= 2*int(self.table.lastAction[2]) and self.phase.isAllIn != True:
                self.action = [2,"Raise",int(self.betsize)]

        if self.table.lastAction[1] == "Check" or self.table.lastAction[1] == "Fold" or self.table.lastAction[1] == "Call" or self.table.lastAction[1] == "" or self.table.lastAction[1] == "pass":
            if self.betsize < self.table.Pot_Stack:
                self.action = [2,"Check",0]
            if self.betsize >= self.table.Pot_Stack:
                self.action = [2,"Raise",int(self.betsize)]
        print self.action


    def Level_Three_Algorithm(self):
        """PURPOSE:  If the last action by the oppenent was not a raise
                     then the level two algorithm is called. If the last
                     action was a raise then  """

        if self.table.lastAction[1] != "Raise":
            self.Level_Two_Algorithm()

        if self.table.lastAction[1] == "Raise":
            self.Determine_HS()
            self.Determine_Opponent_HS()
            if self.phase.isPreFlop == True:
                self.trendtracker.Played_PF_HS = self.opponhs
                self.hs += self.trendtracker.PFadjustment
            if self.phase.isFlop == True:
                self.trendtracker.Played_F_HS = self.opponhs
                self.hs += self.trendtracker.Fadjustment
            if self.phase.isTurn == True:
                self.trendtracker.Played_T_HS = self.opponhs
                self.hs += self.trendtracker.Tadjustment
            if self.phase.isRiver == True:
                self.trendtracker.Played_R_HS = self.opponhs
                self.hs += self.trendtracker.Radjustment
            print self.hs

            self.Determine_Betsize()

            if self.betsize < self.table.lastAction[2]:
                self.action = [2,"Fold",0]
            if (self.betsize >= self.table.lastAction[2] and self.betsize < 2*int(self.table.lastAction[2])) or (self.betsize >= self.table.lastAction[2] and self.table.Player_Stack == 0):
                self.action = [2,"Call",self.table.lastAction[2]]
            if self.betsize >= 2*int(self.table.lastAction[2]) and self.phase.isAllIn == False and self.table.Player_Stack != 0:
                self.action = [2,"Raise",int(self.betsize)]











