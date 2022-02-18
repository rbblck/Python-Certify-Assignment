#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:47:28 2021

@author: robertblack
"""
class Card:
    
    def __init__(self, suitEnum, typeEnum):
        
        self.__m_suit = suitEnum
        self.__m_type = typeEnum
        
    #Getters
    def getSuit(self):
        
        return self.__m_suit
    
    def getType(self):
        
        return self.__m_type
    
    def isEqualTo(self, card):
        
        eCardSuit = card.getSuit()
        eCardType = card.getType()
        
        cardEq = False
        
        if (self.__m_suit == eCardSuit and self.__m_type == eCardType):
            
            cardEq = True
            
        return cardEq
    
    def isSameType(self, card):
        
        eCardType = card.getType()
        
        cardEq = False
        
        if (self.__m_type == eCardType):
            
            cardEq = True
            
        return cardEq
    
    def __str__(self):
        
        cardType = self.__m_type.value
        cardSuit = self.__m_suit.value
        
        return str(cardType) + " of " + str(cardSuit)