#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:46:46 2021

@author: robertblack
"""
import card_class as card
import game_enums as enums
from random import shuffle, randint

class CardDeck:
    
    def __init__(self, numberOfDecks = 1):
        
        self.__m_numberOfDecks = numberOfDecks
        self.__m_cards = self.__getNewDeck()
        
    def getCards(self):
        
        return self.__m_cards
    
    def __getNewDeck(self):
        
        cardDeck = []
        
        for i in range(self.__m_numberOfDecks):
        
            for suit in enums.CARD_SUIT:
        
                for cardType in enums.CARD_TYPE:
                    
                    myNextCard = card.Card(suit, cardType)
                    cardDeck.append(myNextCard)
                
        return cardDeck
    
    def shuffleCards(self):
        
        shuffle(self.__m_cards)
        
    def orderCards(self):
        
        self.__m_cards = self.__getNewDeck()
        
    def getNumberOfCardsLeft(self):
        
        return len(self.__m_cards)
    
    def takeCardFromTopOfDeck(self):
        
        if len(self.__m_cards) > 0:
        
            return self.__m_cards.pop()
    
    def takeCardFromBottomOfDeck(self):
        
        if len(self.__m_cards) > 0:
            
            return self.__m_cards.pop()
    
    def takeRamdomCardFromDeck(self):
        
        card = None
        
        if len(self.__m_cards) > 0:
        
            randCardNum = randint(0, len(self.__m_cards) -1)
            card = self.__m_cards[randCardNum]
            del self.__m_cards[randCardNum]
        
        return card
    
    def addCardToTopOfDeck(self, card):
        
        self.__m_cards.append(card)
        
    def addCardToBottomOfDeck(self, card):
        
        self.__m_cards.insert(0, card)
        
    def addCardAnyWhereToDeck(self, card):
        
        randCardNum = randint(0, len(self.__m_cards) - 1)
        self.__m_cards.insert(randCardNum, card)
    
    def __str__(self):
        
        cardsStr = ""
        
        for crd in self.__m_cards:
            
            cardsStr += str(crd)
            cardsStr += "\n"
            
        return cardsStr