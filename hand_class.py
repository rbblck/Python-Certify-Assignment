#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:41:37 2021

@author: robertblack
"""
from random import randint

class Hand:
    
    def __init__(self):
        
        self.__m_cards = []
        
    def getNumberOfCardsLeft(self):
        
        return len(self.__m_cards)
        
    def addCard(self, card):
        
        self.__m_cards.append(card)
        
    def getCards(self):
        
        return self.__m_cards
        
    def dicardCard(self, index):
        
        card = None
        
        if len(self.__m_cards) > 0:
        
            index -= 1
            card = self.__m_cards[index]
            del self.__m_cards[index]
        
        return card
    
    def dicardRandomCard(self):
        
        card = None
        
        if len(self.__m_cards) > 0:
        
            randCardNum = randint(0, len(self.__m_cards) -1)
            card = self.__m_cards[randCardNum]
            del self.__m_cards[randCardNum]
        
        return card
    
    def checkFourCardSameValue(self):
        
        retVal = False
        sameValue = 0
            
        for x in range(len(self.__m_cards)):
            
            card_1 = self.__m_cards[x]
            
            for i in range(len(self.__m_cards)):
                
                card_2 = self.__m_cards[i]
                
                if card_1.isSameType(card_2):
                    
                    sameValue += 1
                    
            if sameValue >= 4:
                
                retVal = True
                break
                
            sameValue = 0
            
        return retVal
            
        
    def __str__(self):
        
        cardsStr = ""
        
        for card in self.__m_cards:
            
            cardsStr += str(card)
            cardsStr += "\n"
            
        return cardsStr
    
    