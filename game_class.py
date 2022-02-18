#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:06:43 2021

@author: robertblack
"""
import game_data_class as gd
import game_enums as ens
import render_class as ren

class Game:
    
    def __init__(self):
        
        self.__m_gameData = gd.GameData()
        self.__m_renderGame = ren.Render()
        
    def initailiseGame(self):
        
        #Will collect the players but stop with a maximun of 8 or sooner
        #if the players are all in the game.
        while (self.__m_gameData.getNumberOfParticipants() 
               <= self.__m_gameData.getMaxNumParticipants()):
            
            while True:
                
                self.__m_renderGame.clearScreen()
                
                participantType = None
                
                #Check if user types "--help" and wants to see the rules.
                checkRules = True
                while(checkRules):
                
                    if self.__m_gameData.getNumberOfParticipants() == 0:
                        
                        participantName = input("Dealer, please enter your name: ")
                        participantType = ens.PARTICIPANT.DEALER
                        
                    else:
                        
                        numParts = self.__m_gameData.getNumberOfParticipants()
                        participantName = input("Player " + str(numParts + 1) + 
                                            ", please enter your name: ")
                        participantType = ens.PARTICIPANT.PLAYER
                        
                    participantName = participantName.strip(" ")
                    
                    checkRules = self.checkIsUserWantsToSeeRules(
                        participantName)
                
                #Capitalise the first letter and make the rest lower case.
                participantName = participantName.lower()
                nameList = participantName.split()
                participantName = ""
                
                numOfWords = len(nameList)
                for i in range(numOfWords):
                    
                    if i == numOfWords - 1:
                        
                        nameList[i] = nameList[i].capitalize()
                        participantName += nameList[i]
                               
                    else:
                        
                        nameList[i] = nameList[i].capitalize()
                        participantName += nameList[i] + " "
                
                #Check that user has actually entered a name.
                if participantName == "":
                    
                    self.__m_renderGame.clearScreen()
                    
                    print("The name did not register, please try again.")
                    
                else:
                    
                    #Check that the name is unique.
                    sameName = False
                    
                    for part in self.__m_gameData.getPaticipants():
                    
                        if part.getName() == participantName:
                            
                            self.__m_renderGame.clearScreen()
                            
                            print("There is a player with the same name.\n" +
                                  "please enter another name or add your " +
                                  "family name.")
                            
                            sameName = True
                        
                    if not sameName:
                        
                        break
            
            #Add the participant to the game.
            self.__m_gameData.addParticipant(participantName, participantType)
            
            #Let the players know when the maximun number of players has been 
            #reached.
            if self.__m_gameData.hasReachedMaximunParticipants():
                
                print("\nYou have reached the maximum number of players.\n")
                break
                
            else:
        
                if self.__m_gameData.getNumberOfParticipants() >= 2:
                    
                    self.__m_renderGame.clearScreen()
                    
                    #Check if user types "--help" and wants to see the rules.
                    checkRules = True
                    while(checkRules):
                    
                        anyMore = input(
                            "Are there any more players?\nEnter y/n")
                        checkRules = self.checkIsUserWantsToSeeRules(anyMore)
        
                    if anyMore == "n":
                        
                        break
        
        #set the card decks and deal the cards to all participants.
        self.__m_gameData.initCardDecks()
        self.__m_gameData.dealTheCards()
        
        #Once the cards are delt, dealer takes a card for the first play.
        #Dealer always goes first.
        self.__m_gameData.dealerGetsFirstPlayDeckCard()
        
        #Add the spoons. The number is one less of the number of players.
        numOfSpoons = self.__m_gameData.getNumberOfParticipants() - 1
        self.__m_gameData.initTableSpoons(numOfSpoons)
        
        #Initalise and update the render class.
        self.__m_renderGame.initRenderMatrix()
        self.__m_renderGame.addPartisipants(self.__m_gameData.getPaticipants())
        self.__m_renderGame.setNumberOfTableSpoons(numOfSpoons)
        dealer = (self.__m_gameData.getPaticipants())[0]
        self.__m_renderGame.updateLeftCardCounter(
            dealer.getCardsLeftInLeftDeck())
        self.__m_renderGame.updateRightCardCounter(
            dealer.getCardsLeftInRightDeck())
        self.__m_renderGame.clearScreen()
        self.__m_renderGame.renderGame()
        
    def startPlay(self):
        
        #Start the game session loop.
        while True:
            
            numberOfParticipants = self.__m_gameData.getNumberOfParticipants()
            
            #Start the play round loop.
            for i in range(numberOfParticipants):
                
                #Get players card choice and check validity of choice.
                playerName = self.__m_gameData.getPaticipants()[i].getName()
                playerCardsNum = self.__m_gameData.getPaticipants()[
                    i].getNumOfCards()
                cardNum = self.getPlayCardNumber(playerName, playerCardsNum)
                
                #Dealer is always at playerIndex 0.
                if i == 0:
                    
                    # #Dealer takes a card from the apprpiate deck of cards
                    # #and gives one of his cards to the next player.
                    self.__m_gameData.dealerPassCardToPlayer(i, cardNum)
                
                #Last player will always pass to the dealer.
                elif i == numberOfParticipants - 1:
                    
                    #The last player gives a card to the dealer and the dealer 
                    #puts one of his cards on the appropriate deck
                    self.__m_gameData.playerPassCardToDealer(i, cardNum)
                
                #All other plays are between players.
                else:
                    
                    #The player gives one of his cards to the next player.
                    self.__m_gameData.playerPasCardToPlayer(i, cardNum)
                
                # self.__m_gameData.playCard(i)
                
                #Render the play.
                self.updateAndRender()
                
                #This checks if one of the players gets four matching cards
                #which will end this play session, give a spoon to the player 
                #with matching cards and restart another if there are still 
                #spoons on the table.
                participant = self.__m_gameData.checkFourCardsMatch()
                
                if participant is not None:
                    
                    self.__m_renderGame.clearScreen()
                    
                    #Announce the participant with the four card match
                    print(participant.getName() + " has four matching " + 
                          "cards and gets a spoon!\n")
                    
                    #Check if user types "--help" and wants to see the rules.
                    checkRules = True
                    while(checkRules):
                    
                        res = input("Press any key and Enter to continue...")
                        checkRules = self.checkIsUserWantsToSeeRules(res)
                    
                    self.__m_gameData.resetCards()
                    self.__m_gameData.dealerGetsFirstPlayDeckCard()
                    self.updateAndRender()
                    
                    break
                
            #Check for winners
            if self.checkForWinners():
                
                break
     
    def updateAndRender(self):
        
        self.__m_renderGame.initRenderMatrix()
        self.__m_renderGame.addPartisipants(self.__m_gameData.getPaticipants())
        numOfSpoons = self.__m_gameData.getNumberOfSpoons()
        self.__m_renderGame.setNumberOfTableSpoons(numOfSpoons)
        dealer = (self.__m_gameData.getPaticipants())[0]
        self.__m_renderGame.updateLeftCardCounter(
            dealer.getCardsLeftInLeftDeck())
        self.__m_renderGame.updateRightCardCounter(
            dealer.getCardsLeftInRightDeck())
        self.__m_renderGame.clearScreen()
        self.__m_renderGame.renderGame()
     
    #Check if there are any spoons left on the table. If there are no 
    #spoons left, check which player has the most spoons and anounce 
    #the winner.
    def checkForWinners(self):
        
        hasWinner = False
        
        if self.__m_gameData.getNumberOfSpoons() <= 0:
            
            players = self.__m_gameData.getPaticipants()
            
            self.__m_renderGame.clearScreen()
            
            #Display all the player and how many spoons they have.
            for player in players:
                
                print(player.getName() + " has " + 
                                      str(player.getNumberOfSpoons()) + 
                                      " spoons")
                
            print("")
            
            #Get the player(s) with the most sppons
            winners = self.__m_gameData.getPlayer_s_WithTheMostSpoons()
            
            #Display the winner(s) and number of spoons
            if len(winners) > 1:
            
                print("It is a tie between:\n")
                
                for winner in winners:
                    
                    numOfSpoons = winner.getNumberOfSpoons()
                    spoonStr = ""
                    
                    if numOfSpoons > 1:
                        
                        spoonStr = "spoons"
                        
                    else:
                        
                        spoonStr = "spoon"
                    
                    print(winner.getName() + " who has " + 
                          str(numOfSpoons) + " " + spoonStr) 
                    
                hasWinner = True
                    
            else:
                
                print("The winner is: ", end = "")
                
                for winner in winners:
                    
                    numOfSpoons = winner.getNumberOfSpoons()
                    spoonStr = ""
                    
                    if numOfSpoons > 1:
                        
                        spoonStr = "spoons"
                        
                    else:
                        
                        spoonStr = "spoon"
                    
                    print(winner.getName() + " who has " + 
                          str(winner.getNumberOfSpoons()) + " " + spoonStr)
                    
                hasWinner = True
                
        return hasWinner
    
    def checkIsUserWantsToSeeRules(self, typedText):
        
        retVal = False
    
        if typedText.strip() == "--help":
            
            self.__m_renderGame.showRules()
            retVal = True
            
        return retVal
    
    def getPlayCardNumber(self, playerName, numPlayerCardsLeft):
        
        cardNum = None
        isNumber = False
        
        while not isNumber:
            
            #Check if user types "--help" and wants to see the rules.
            checkRules = True
            while(checkRules):
                
                #Render the play.
                self.updateAndRender()
            
                cardNum = input(playerName + ", please pick a card number " + 
                            "to pass on to the next player.\n")
                checkRules = self.checkIsUserWantsToSeeRules(cardNum)
            
            self.__m_renderGame.clearScreen()
            
            if (cardNum.isdigit()):
                
                cardNum = int(cardNum)
                
                if (cardNum > numPlayerCardsLeft) or (
                        cardNum < 1):
                    
                    print("\nYou must enter a positive number between 1 and " +
                      str(numPlayerCardsLeft))
                    
                else:
                
                    isNumber = True
                
            else:
                
                print("\nYou must enter a positive number between 1 and " +
                      str(numPlayerCardsLeft))
                
        return cardNum
    
    
    
    