#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      carricktel
#
# Created:     26/11/2015
# Copyright:   (c) carricktel 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import os
import numpy as np
import pygame
import time
from pygame import locals
from THAIP_Class_Card import Card

class GUI:

    def __init__(self):
        self.screen_width = 550
        self.screen_height = 364
        self.grid = (10,8)
        self.launch = True
        self.buttons_on = False
        self.menu_screen = True
        self.Action = ""
        self.ai_dialog = ""
        self.player_dialog = ""
        self.dealer_dialog = ""
        self.main_screen = pygame.display.set_mode([self.screen_width,self.screen_height])
        self.table_surface = pygame.image.load('static/pokertable.png')

        pygame.RESIZABLE = False
        pygame.init()

    def draw_main_menu(self):

        self.main_screen.blit(self.table_surface,(0,0))

        pygame.draw.rect(self.main_screen, (0,0,0), ((self.screen_width//self.grid[0])*3.5,(self.screen_height//self.grid[1])*2,165,65))
        pygame.draw.rect(self.main_screen, (0,0,0), ((self.screen_width//self.grid[0])*4,(self.screen_height//self.grid[1])*4-13,110,35))
        pygame.draw.rect(self.main_screen, (0,0,0), (((self.screen_width//self.grid[0])*4),(self.screen_height//self.grid[1])*5-13,110,35))

        play = pygame.font.Font(None, 60)
        other = pygame.font.Font(None, 30)

        PLAY = play.render("PLAY",1,(255,255,255))
        Settings = other.render("Settings",1,(255,255,255))
        Rules = other.render("Rules",1,(255,255,255))

        self.main_screen.blit(PLAY,((self.screen_width//self.grid[0])*3.5+30,(self.screen_height//self.grid[1])*2+16))
        self.main_screen.blit(Settings,((self.screen_width//self.grid[0])*4+13,(self.screen_height//self.grid[1])*4-4))
        self.main_screen.blit(Rules,(((self.screen_width//self.grid[0])*4+27),(self.screen_height//self.grid[1])*5-4))

    def exit_event(self):

        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                self.launch = False

    def get_image_source(self,cardobj):

        val = ""
        if cardobj.NumVal <= 9:
            val = str(cardobj.NumVal)
        if cardobj.NumVal > 9:
            if cardobj.NumVal == 10:
                val ="T"
            if cardobj.NumVal == 11:
                val = "J"
            if cardobj.NumVal == 12:
                val = "Q"
            if cardobj.NumVal == 13:
                val = "K"
            if cardobj.NumVal == 14:
                val = "A"

        return "static/" + val + "of" + cardobj.Suit + ".png"

    def draw_pokertable(self):

        self.main_screen.blit(self.table_surface,(0,0))

        pygame.draw.rect(self.main_screen, (0,0,0), ((self.screen_width//self.grid[0]),(self.screen_height//self.grid[1])*7,90,35))
        pygame.draw.rect(self.main_screen, (0,0,0), ((self.screen_width//self.grid[0])*3,(self.screen_height//self.grid[1])*7,90,35))
        pygame.draw.rect(self.main_screen, (0,0,0), (((self.screen_width//self.grid[0])*5)+20,(self.screen_height//self.grid[1])*7,90,35))
        pygame.draw.rect(self.main_screen, (0,0,0), (((self.screen_width//self.grid[0])*7)+20,(self.screen_height//self.grid[1])*7,90,35))

        font = pygame.font.Font(None, 28)
        check = font.render("Check",1,(255,255,255))
        fold = font.render("Fold",1,(255,255,255))
        call = font.render("Call",1,(255,255,255))
        raisex = font.render("Raise",1,(255,255,255))
        aitext = font.render(str(self.ai_dialog),1,(255,255,255))
        plyrtext = font.render(str(self.player_dialog),1,(255,255,255))

        self.main_screen.blit(check,((self.screen_width//self.grid[0])+15,((self.screen_height//self.grid[1])*7)+9))
        self.main_screen.blit(fold,((self.screen_width//self.grid[0])*3+25,((self.screen_height//self.grid[1])*7)+9))
        self.main_screen.blit(call,((self.screen_width//self.grid[0])*5+46,((self.screen_height//self.grid[1])*7)+9))
        self.main_screen.blit(raisex,((self.screen_width//self.grid[0])*7+39,((self.screen_height//self.grid[1])*7)+9))

        self.main_screen.blit(aitext,((self.screen_width//self.grid[0])*7+15,((self.screen_height//self.grid[1])*1)+30))
        self.main_screen.blit(plyrtext,((self.screen_width//self.grid[0])*7+15,((self.screen_height//self.grid[1])*5)+30))

    def draw_preflop(self,plyr_cards):

        c = 0
        for i in plyr_cards:
            src = self.get_image_source(i)
            img = pygame.image.load(src)
            backofcard = pygame.image.load("static/backofcard.png")
            self.main_screen.blit(backofcard,((self.screen_width//self.grid[0])*(4+c),(self.screen_height//self.grid[1])*1))
            self.main_screen.blit(img,((self.screen_width//self.grid[0])*(4+c),(self.screen_height//self.grid[1])*5))
            c += 1

    def draw_comcards(self,com_cards):

        c = 0
        for i in com_cards:
            src = self.get_image_source(i)
            img = pygame.image.load(src)
            self.main_screen.blit(img,((self.screen_width//self.grid[0])*(3+c),(self.screen_height//self.grid[1])*3))
            c += 1

    def draw_aicards(self,ai_cards):

        c = 0
        for i in ai_cards:
            src = self.get_image_source(i)
            img = pygame.image.load(src)
            self.main_screen.blit(img,((self.screen_width//self.grid[0])*(4+c),(self.screen_height//self.grid[1])*1))
            c += 1

    def draw_stacks(self,pot_stack,ai_stack,player_stack,dealer_button,turn):

        if dealer_button == 1:
            d = 5
        if dealer_button == 2:
            d = 1
        if turn == 1:
            t = 5
        if turn == 2:
            t = 1
        pygame.draw.circle(self.main_screen,(0,0,0),(46,((self.screen_height//self.grid[1])*d)+43),10)
        pygame.draw.circle(self.main_screen,(200,0,0),(23,((self.screen_height//self.grid[1])*t)+43),10)

        font = pygame.font.Font(None, 36)
        dfont = pygame.font.Font(None,20)

        potstack = font.render(str(pot_stack),1,(255,255,255))
        aistack = font.render(str(ai_stack),1,(255,255,255))
        playerstack = font.render(str(player_stack),1,(255,255,255))
        db = dfont.render("D",1,(255,255,255))

        self.main_screen.blit(potstack,((self.screen_width//self.grid[0])+15,((self.screen_height//self.grid[1])*3)+30))
        self.main_screen.blit(aistack,((self.screen_width//self.grid[0])+15,((self.screen_height//self.grid[1])*1)+30))
        self.main_screen.blit(playerstack,((self.screen_width//self.grid[0])+15,((self.screen_height//self.grid[1])*5)+30))
        self.main_screen.blit(db,(42,((self.screen_height//self.grid[1])*d)+36))

    def show_dealer_dialog(self):

        font = pygame.font.Font(None, 28)
        text = font.render(str(self.dealer_dialog),1,(255,255,255))
        self.main_screen.blit(text,((self.screen_width//self.grid[0])*3+15,((self.screen_height//self.grid[1])*3)+30))
##
##    def player_dialog(self,dialog):
##
##        font = pygame.font.Font(None, 28)
##        text = font.render(str(dialog),1,(255,255,255))
##        self.main_screen.blit(text,((self.screen_width//self.grid[0])*7+15,((self.screen_height//self.grid[1])*5)+30))


    def button_hover(self):

        mouse = pygame.mouse.get_pos()
        if (self.screen_width//self.grid[0])+90 > mouse[0] > (self.screen_width//self.grid[0]) and ((self.screen_height//self.grid[1])*7)+35 > mouse[1] > ((self.screen_height//self.grid[1])*7):
            pygame.draw.rect(self.main_screen, (70,70,70), ((self.screen_width//self.grid[0]),(self.screen_height//self.grid[1])*7,90,35))
        else:
            pygame.draw.rect(self.main_screen, (0,0,0), ((self.screen_width//self.grid[0]),(self.screen_height//self.grid[1])*7,90,35))

        if ((self.screen_width//self.grid[0])*3+90) > mouse[0] > ((self.screen_width//self.grid[0])*3) and (self.screen_height//self.grid[1])*7+35 > mouse[1] > (self.screen_height//self.grid[1])*7:
            pygame.draw.rect(self.main_screen, (70,70,70), ((self.screen_width//self.grid[0]*3),(self.screen_height//self.grid[1])*7,90,35))
        else:
            pygame.draw.rect(self.main_screen, (0,0,0), ((self.screen_width//self.grid[0]*3),(self.screen_height//self.grid[1])*7,90,35))

        if ((self.screen_width//self.grid[0])*5+20+90) > mouse[0] > ((self.screen_width//self.grid[0])*5+20) and (self.screen_height//self.grid[1])*7+35 > mouse[1] > (self.screen_height//self.grid[1])*7:
            pygame.draw.rect(self.main_screen, (70,70,70), ((self.screen_width//self.grid[0]*5+20),(self.screen_height//self.grid[1])*7,90,35))
        else:
            pygame.draw.rect(self.main_screen, (0,0,0), ((self.screen_width//self.grid[0]*5+20),(self.screen_height//self.grid[1])*7,90,35))


        font = pygame.font.Font(None, 28)

        check = font.render("Check",1,(255,255,255))
        fold = font.render("Fold",1,(255,255,255))
        call = font.render("Call",1,(255,255,255))
        raisex = font.render("Raise",1,(255,255,255))

        self.main_screen.blit(check,((self.screen_width//self.grid[0])+15,((self.screen_height//self.grid[1])*7)+9))
        self.main_screen.blit(fold,((self.screen_width//self.grid[0])*3+25,((self.screen_height//self.grid[1])*7)+9))
        self.main_screen.blit(call,((self.screen_width//self.grid[0])*5+46,((self.screen_height//self.grid[1])*7)+9))
        self.main_screen.blit(raisex,((self.screen_width//self.grid[0])*7+39,((self.screen_height//self.grid[1])*7)+9))

    def check_event(self):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (self.screen_width//self.grid[0])+90 > mouse[0] > (self.screen_width//self.grid[0]) and ((self.screen_height//self.grid[1])*7)+35 > mouse[1] > ((self.screen_height//self.grid[1])*7):
            pygame.draw.rect(self.main_screen, (70,70,70), ((self.screen_width//self.grid[0]),(self.screen_height//self.grid[1])*7,90,35))
        else:
            pygame.draw.rect(self.main_screen, (0,0,0), ((self.screen_width//self.grid[0]),(self.screen_height//self.grid[1])*7,90,35))

        if (self.screen_width//self.grid[0])+90 > mouse[0] > (self.screen_width//self.grid[0]) and ((self.screen_height//self.grid[1])*7)+35 > mouse[1] > ((self.screen_height//self.grid[1])*7):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons_on = False
                    self.Action = "Check"

        font = pygame.font.Font(None, 28)
        check = font.render("Check",1,(255,255,255))
        self.main_screen.blit(check,((self.screen_width//self.grid[0])+15,((self.screen_height//self.grid[1])*7)+9))


    def fold_event(self):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if ((self.screen_width//self.grid[0])*3+90) > mouse[0] > ((self.screen_width//self.grid[0])*3) and (self.screen_height//self.grid[1])*7+35 > mouse[1] > (self.screen_height//self.grid[1])*7:
            pygame.draw.rect(self.main_screen, (70,70,70), ((self.screen_width//self.grid[0]*3),(self.screen_height//self.grid[1])*7,90,35))
        else:
            pygame.draw.rect(self.main_screen, (0,0,0), ((self.screen_width//self.grid[0]*3),(self.screen_height//self.grid[1])*7,90,35))

        if ((self.screen_width//self.grid[0])*3+90) > mouse[0] > ((self.screen_width//self.grid[0])*3) and (self.screen_height//self.grid[1])*7+35 > mouse[1] > (self.screen_height//self.grid[1])*7:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons_on = False
                    self.Action = "Fold"

        font = pygame.font.Font(None, 28)
        fold = font.render("Fold",1,(255,255,255))
        self.main_screen.blit(fold,((self.screen_width//self.grid[0])*3+25,((self.screen_height//self.grid[1])*7)+9))

    def call_event(self):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if ((self.screen_width//self.grid[0])*5+20+90) > mouse[0] > ((self.screen_width//self.grid[0])*5+20) and (self.screen_height//self.grid[1])*7+35 > mouse[1] > (self.screen_height//self.grid[1])*7:
            pygame.draw.rect(self.main_screen, (70,70,70), ((self.screen_width//self.grid[0]*5+20),(self.screen_height//self.grid[1])*7,90,35))
        else:
            pygame.draw.rect(self.main_screen, (0,0,0), ((self.screen_width//self.grid[0]*5+20),(self.screen_height//self.grid[1])*7,90,35))

        if ((self.screen_width//self.grid[0])*5+20+90) > mouse[0] > ((self.screen_width//self.grid[0])*5+20) and (self.screen_height//self.grid[1])*7+35 > mouse[1] > (self.screen_height//self.grid[1])*7:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons_on = False
                    self.Action = "Call"

        font = pygame.font.Font(None, 28)
        call = font.render("Call",1,(255,255,255))
        self.main_screen.blit(call,((self.screen_width//self.grid[0])*5+46,((self.screen_height//self.grid[1])*7)+9))

    def raise_event(self):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if ((self.screen_width//self.grid[0])*7+20+90) > mouse[0] > ((self.screen_width//self.grid[0])*7+20) and (self.screen_height//self.grid[1])*7+35 > mouse[1] > (self.screen_height//self.grid[1])*7:
            pygame.draw.rect(self.main_screen, (70,70,70), ((self.screen_width//self.grid[0]*7+20),(self.screen_height//self.grid[1])*7,90,35))
        else:
            pygame.draw.rect(self.main_screen, (0,0,0), ((self.screen_width//self.grid[0]*7+20),(self.screen_height//self.grid[1])*7,90,35))

        if ((self.screen_width//self.grid[0])*7+20+90) > mouse[0] > ((self.screen_width//self.grid[0])*7+20) and (self.screen_height//self.grid[1])*7+35 > mouse[1] > (self.screen_height//self.grid[1])*7:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons_on = False
                    self.Action = "Raise"

        font = pygame.font.Font(None, 28)
        raisex = font.render("Raise",1,(255,255,255))
        self.main_screen.blit(raisex,((self.screen_width//self.grid[0])*7+39,((self.screen_height//self.grid[1])*7)+9))

##gui = GUI()
##plyrcards = [Card(3,"Hearts",2),Card(12,"Spades",38)]
##comcards = [Card(10,"Diamonds",2),Card(12,"Clubs",38),Card(14,"Spades",52),Card(4,"Clubs",8)]
##
##while gui.launch == True:
##    gui.exit_event()
##    gui.draw_pokertable()
##    gui.draw_preflop(plyrcards)
##    gui.draw_comcards(comcards)
##    gui.draw_aicards(plyrcards)
##    gui.button_hover()
##    gui.check_event()
##    pygame.display.flip()
##pygame.quit()



##def main():
##
##    global SCREEN_SIZE
##    global GRID
##    global launch
##
##    SCREEN_SIZE = [544, 544]
##    GRID = (32, 32)
##    GRID_SIZE = [SCREEN_SIZE[0] // GRID[0], SCREEN_SIZE[1] // GRID[1]]
##    launch = True
##    FPS = 60
##    pygame.init()
##    pygame.RESIZABLE = False
##    pygame.NOFRAME = True
##    table_surface = pygame.image.load('static/pokertable.png')
##    QofH = pygame.image.load('static/QofHearts.png')
##
##
##
##    main_screen = pygame.display.set_mode(SCREEN_SIZE)

##    while launch:
##        pygame.display.update()
##        for events in pygame.event.get():
##            if events.type==pygame.QUIT:
##                launch = False
##        main_screen.blit(table_surface,(0,0))
##        main_screen.blit(QofH,(0,0))
##        pygame.display.flip()
##    pygame.quit()

