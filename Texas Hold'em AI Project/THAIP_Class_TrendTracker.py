#-------------------------------------------------------------------------------
# Name:
# Purpose:     Logs information about how the AI's opponent plays and organizes
#              this information in ways that helps the AI class determine the
#              best action for it to take.
#
# Author:      carricktel
#
# Created:     18/11/2015
# Copyright:   (c) carricktel 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class TrendTracker:

    def __init__(self,table):
        self.table = table      #The table object in play is passed in here.

        self.Played_PF_HS = 0   #Temporary record of how the opponent played his preflop hand.

        self.Played_F_HS = 0    #Temporary record of how the opponent played his flop hand.

        self.Played_T_HS = 0    #Temporary record of how the opponent played his turn hand.

        self.Played_R_HS = 0    #Temporary record of how the opponent played his river hand.

        self.PFadjustment = 0   #Percentage difference of how the opponent is
                                #valuing his hand strength before the Flop
                                #versus his actual hand strength before the Flop.

        self.Fadjustment = 0    #Percentage difference of how the opponent is
                                #valuing his hand strength on the Flop
                                #versus his actual hand strength on the Flop.

        self.Tadjustment = 0    #Percentage difference of how the opponent is
                                #valuing his hand strength on the Turn
                                #versus his actual hand strength on the Turn.

        self.Radjustment = 0     #Percentage difference of how the opponent is
                                #valuing his hand strength on the River
                                #versus his actual hand strength on the River.

        self.PFadjustment_counter = 0   #Keeps track of how many times the
                                        #Preflop hand strength has been adjusted.

        self.Fadjustment_counter = 0    #Keeps track of how many times the
                                        #Flop hand strength has been adjusted.

        self.Tadjustment_counter = 0    #Keeps track of how many times the
                                        #Turn hand strength has been adjusted.

        self.Radjustment_counter = 0    #Keeps track of how many times the
                                        #River hand strength has been adjusted.

    def Reset_Played_HS(self):
        """PURPOSE: Should be called after every hand to reset the played hand
                    strength values. """

        self.Played_PF_HS = 0
        self.Played_F_HS = 0
        self.Played_T_HS = 0
        self.Played_R_HS = 0

    def Adjust_PF_HS(self,actualHS,playedHS):
        """PURPOSE: Adjusts the opponents Preflop hand strength to more accurately
                    represent how the opponent is valuing his hand strength.

                    EX: Opponent's actual hand strength is - 62%
                        Opponent valued his hand stength at - 75%
                        Opponent played three hands before this one, over-valuing his
                        hand 17% on average. The opponent's current over-value is
                        13%. The new average hand strength adjustment is:
                            (17% + 17% + 17% + 13%) / 4 = 16%
                        """

        currentHSdiff = playedHS - actualHS
        self.PFadjustment_counter += 1
        self.PFadjustment = ((self.PFadjustment * (self.PFadjustment_counter-1)) + currentHSdiff)/self.PFadjustment_counter
        print self.PFadjustment


    def Adjust_F_HS(self,actualHS,playedHS):
        """PURPOSE: Adjusts the opponents Flop hand strength to more accurately
                    represent how the opponent is valuing his hand strength.

                    EX: Opponent's actual hand strength is - 62%
                        Opponent valued his hand stength at - 75%
                        Opponent played three hands before this one, over-valuing his
                        hand 17% on average. The opponent's current over-value is
                        13%. The new average hand strength adjustment is:
                            (17% + 17% + 17% + 13%) / 4 = 16%
                        """

        currentHSdiff = playedHS - actualHS
        self.Fadjustment_counter += 1
        self.Fadjustment = ((self.Fadjustment * (self.Fadjustment_counter-1)) + currentHSdiff)/self.Fadjustment_counter
        print self.Fadjustment


    def Adjust_T_HS(self,actualHS,playedHS):
        """PURPOSE: Adjusts the opponents Turn hand strength to more accurately
                    represent how the opponent is valuing his hand strength.

                    EX: Opponent's actual hand strength is - 62%
                        Opponent valued his hand stength at - 75%
                        Opponent played three hands before this one, over-valuing his
                        hand 17% on average. The opponent's current over-value is
                        13%. The new average hand strength adjustment is:
                            (17% + 17% + 17% + 13%) / 4 = 16%
                        """

        currentHSdiff = playedHS - actualHS
        self.Tadjustment_counter += 1
        self.Tadjustment = ((self.Tadjustment * (self.Tadjustment_counter-1)) + currentHSdiff)/self.Tadjustment_counter
        print self.Tadjustment


    def Adjust_R_HS(self,actualHS,playedHS):
        """PURPOSE: Adjusts the opponents River hand strength to more accurately
                    represent how the opponent is valuing his hand strength.

                    EX: Opponent's actual hand strength is - 62%
                        Opponent valued his hand stength at - 75%
                        Opponent played three hands before this one, over-valuing his
                        hand 17% on average. The opponent's current over-value is
                        13%. The new average hand strength adjustment is:
                            (17% + 17% + 17% + 13%) / 4 = 16%
                        """

        currentHSdiff = playedHS - actualHS
        self.Radjustment_counter += 1
        self.Radjustment = ((self.Radjustment * (self.Radjustment_counter-1)) + currentHSdiff)/self.Radjustment_counter
        print self.Radjustment

##tracker = TrendTracker(None)
##tracker.Adjust_R_HS(50,70)
##tracker.Adjust_T_HS(44,32)
##tracker.Adjust_T_HS(30,16)




