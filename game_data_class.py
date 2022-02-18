#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:07:23 2021

@author: robertblack
"""
import table_spoons_class as tsp
import particapant_factory_class as pf

class GameData:
    
    def __init__(self):
        
        self.__m_tableSpoons = None
        self.__m_participants = []
        self.__m_maxNumberOfPlayers = 8
        self.__m_handSize = 4
        
    #Getters
    def getTableSpoons(self):
        
        return self.__m_tableSpoons
    
    def getPaticipants(self):
        
        return self.__m_participants
    
    def getMaxNumParticipants(self):
        
        return self.__m_maxNumberOfPlayers
    
    def getHandSize(self):
        
        return self.__m_handSize
    
    #Setters
    def setSpoons(self, spoons):
        
        self.__m_tableSpoons = spoons
        
    def setParticipants(self, participants):
        
        self.__m_participants = participants
    
    #Game data functions
    def getNumberOfParticipants(self):
        
        return len(self.__m_participants)
    
    def getNumberOfSpoons(self):
        
        return self.__m_tableSpoons.getNumberOfSpoonsLeft()
    
    def hasReachedMaximunParticipants(self):
        
        retVal = False
        
        if (len(self.__m_participants) + 1) > self.__m_maxNumberOfPlayers:
            
            retVal = True
            
        else:
            
            retVal = False
            
        return retVal
    
    def addParticipant(self, participantName, participantType):
        
        part = pf.ParticapantFactory.createParticipant(participantName, 
                                                       participantType)
        self.__m_participants.append(part)
        
    def dealerGetsFirstPlayDeckCard(self):
        
        self.__m_participants[0].takeCardToPlay()
        
    def dealerPassCardToPlayer(self, playerIndex, cardIndex):
        
        #Dealer has already taken a card from the apprpiate deck of cards
        #and gives one of his cards to the next player.
        #Dealer is always index 0.
        card = self.__m_participants[0].passCardToPlayer(cardIndex)
        self.__m_participants[0].setCurrentPlayer(False)
        self.__m_participants[playerIndex + 1].takeCard(card)
        self.__m_participants[playerIndex + 1].setCurrentPlayer(True)
        
    def playerPassCardToDealer(self, playerIndex, cardIndex):
        
        card = self.__m_participants[playerIndex].passCardToPlayer(cardIndex)
        self.__m_participants[playerIndex].setCurrentPlayer(False)
        self.__m_participants[0].takeCardFromPlayer(card)
        self.__m_participants[0].setCurrentPlayer(True)
        self.__m_participants[0].takeCardToPlay()
        
    def playerPasCardToPlayer(self, playerIndex, cardIndex):
        
        card = self.__m_participants[playerIndex].passCardToPlayer(cardIndex)
        self.__m_participants[playerIndex].setCurrentPlayer(False)
        self.__m_participants[playerIndex + 1].takeCard(card)
        self.__m_participants[playerIndex + 1].setCurrentPlayer(True)
        
    def dealTheCards(self):
        
        for i in range(self.__m_handSize):
            
            for x in range(len(self.__m_participants)):
                
                card = self.__m_participants[0].takeCardFromDeck()
                self.__m_participants[x].takeCard(card)
                
                
        
    def initPLayingDeck(self, numberOfDecks):
        
        self.__m_participants[0].initGameCardDecks(numberOfDecks)
        
    def initTableSpoons(self, numberOfSpoons):
        
        self.__m_tableSpoons = tsp.TableSpoons(numberOfSpoons)
        
    def initCardDecks(self):
        
        #Play with 2 decks of cards if more than 4 players (recommended)
        if self.getNumberOfParticipants() > 4:
            
            self.initPLayingDeck(2)
            
        else:
            
            self.initPLayingDeck(1)
                
    def resetCards(self):
        
        #Take all the cards from the players.
        for part in self.__m_participants:
            
            part.setCardsToZero()
            
        #reset the card decks and deal card to players.
        self.initCardDecks()
        self.dealTheCards()
        
    def checkFourCardsMatch(self):
        
        paticipantName = None
        
        for i in range(len(self.__m_participants)):
            
            fourCardsSame = self.__m_participants[i].checkFourMatchingCards()
            
            if fourCardsSame:
                
                spoon = self.__m_tableSpoons.takeSpoon()
                self.__m_participants[i].takeSpoon(spoon)
                paticipantName = self.__m_participants[i]
        
        return paticipantName
    
    def getPlayer_s_WithTheMostSpoons(self):
        
        playersMostSpoons = []
        mostSpoons = 0
        
        #Get the higest number of spoons held by any player.
        for part in self.__m_participants:
            
            numberOfSpoons = part.getNumberOfSpoons();
            
            if numberOfSpoons > mostSpoons:
                
                mostSpoons = numberOfSpoons
        
        #Now check if only one player or multiple plays have this number.
        #If more than one player has the same number, then there is a tie.
        for part in self.__m_participants:
            
            if part.getNumberOfSpoons() == mostSpoons:
                
                playersMostSpoons.append(part)
                
        return playersMostSpoons
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        