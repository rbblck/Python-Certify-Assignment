#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:45:18 2021

@author: robertblack
"""
import participant_class as pc
import card_deck_class as dek
from random import shuffle

class Dealer(pc.Participant):
    
    def __init__(self, name = "name"):
        
        pc.Participant.__init__(self, name)
        
        self.__m_leftCardDeck = None
        self.__m_rightCardDeck = None
        self.__m_numberOfDecks = 0
        self.__m_numberOfTotalCards = 0
        self.__m_rightDeck = True
        
        self.setCurrentPlayer(True)
        
    def getCardsLeftInLeftDeck(self):
        
        return self.__m_leftCardDeck.getNumberOfCardsLeft()
    
    def getCardsLeftInRightDeck(self):
        
        return self.__m_rightCardDeck.getNumberOfCardsLeft()
        
    def takeCardFromDeck(self):
        
        #Take the card from the appropriate deck of cards.
        if self.__m_leftCardDeck.getNumberOfCardsLeft() == 0:
            
            self.__m_rightDeck = True
            self.__m_rightDeck.shuffleCards()
            
        elif self.__m_rightCardDeck.getNumberOfCardsLeft() == 0:
            
            self.__m_rightDeck = False
            self.__m_leftCardDeck.shuffleCards()
            
        if self.__m_rightDeck:
            
            deltCard = self.__m_rightCardDeck.takeCardFromTopOfDeck()
            
        else:
            
            deltCard = self.__m_leftCardDeck.takeCardFromTopOfDeck()
            
        return deltCard
    
    def takeCardToPlay(self):
        
        #Take from the appropriate deck of cards.
        if self.__m_leftCardDeck.getNumberOfCardsLeft() == 0:
            
            self.__m_rightDeck = True
            self.__m_rightDeck.shuffleCards()
            
        elif self.__m_rightCardDeck.getNumberOfCardsLeft() == 0:
            
            self.__m_rightDeck = False
            self.__m_leftCardDeck.shuffleCards()
            
        if self.__m_rightDeck:
            
            deckCard = self.__m_rightCardDeck.takeCardFromTopOfDeck()
            
        else:
            
            deckCard = self.__m_leftCardDeck.takeCardFromTopOfDeck()
            
        #Add card to dealers hand.
        self._m_hand.addCard(deckCard)
    
    def passCardToPlayer(self, cardIndex):
        
        #Pass the picked card to the next player
        return self._m_hand.dicardCard(cardIndex)
    
    def takeCardFromPlayer(self, card):
        
        #Give the card to the appropriate deck
        if self.__m_leftCardDeck.getNumberOfCardsLeft() == 0:
            
            self.__m_rightDeck = True
            self.__m_rightDeck.shuffleCards()
            
        elif self.__m_rightCardDeck.getNumberOfCardsLeft() == 0:
            
            self.__m_rightDeck = False
            self.__m_leftCardDeck.shuffleCards()
            
        if self.__m_rightDeck:
            
            self.__m_leftCardDeck.addCardToTopOfDeck(card)
            
        else:
            
            self.__m_rightCardDeck.addCardToTopOfDeck(card)
    
    def initGameCardDecks(self, numberOfDecks = 1):
        
        #Play with 2 decks of cards if more than 4 players (recommended)
        self.__m_leftCardDeck = dek.CardDeck(numberOfDecks)
        self.__m_rightCardDeck = dek.CardDeck(0)
        self.__m_numberOfDecks = numberOfDecks
        self.__m_numberOfTotalCards = self.__m_leftCardDeck.getNumberOfCardsLeft()
        self.__m_numberOfTotalCards += self.__m_rightCardDeck.getNumberOfCardsLeft()
        
        #Shuffle the cards
        self.__m_leftCardDeck.shuffleCards()
        
    def __str__(self):
        
        return "My name is : " + self._m_name + " and I am the dealer."
    
    
