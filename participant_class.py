#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:33:01 2021

@author: robertblack
"""
import hand_class as hnd
from os import name, system

class Participant:
    def __init__(self, name = "name"):
        
        self._m_name = name
        self._m_hand = hnd.Hand()
        self._m_spoons = []
        self._m_currentPlayer = False
        
    #Getters.
    def getName(self):
        
        return self._m_name
    
    def isCurrentPlayer(self):
        
        return self._m_currentPlayer
    
    def getCards(self):
        
        return self._m_hand.getCards()
    
    def getNumOfCards(self):
        
        return len(self._m_hand.getCards())
        
    def takeCard(self, card):
        
        self._m_hand.addCard(card)
        
    def getCardsLeft(self):
        
        return self._m_hand.getNumberOfCardsLeft()
        
    def setCurrentPlayer(self, currentPlayer):
        
        self._m_currentPlayer = currentPlayer
        
    def takeSpoon(self, spoon):
        
        self._m_spoons.append(spoon)
        
    def discardSpoon(self):
        
        return self._m_spoons.pop()
    
    def getNumberOfSpoons(self):
        
        return len(self._m_spoons)
    
    def checkFourMatchingCards(self):
        
        return self._m_hand.checkFourCardSameValue()
    
    def setCardsToZero(self):
        
        self._m_hand = hnd.Hand()
        
    #Function to lear the console.
    #Numlines is an optional argument used only as a fall-back.
    def clearScreen(self, numlines=100):
    
        if name == "posix":
            
            # Unix/Linux/MacOS/BSD/etc
            system('clear')
            
        elif name in ("nt", "dos", "ce"):
            
            # DOS/Windows
            system('CLS')
        else:
            
            # Fallback for other operating systems.
            print('\n' * numlines)
    
    def __str__(self):
        
        return "My name is: " + self._m_name + " and I am a participant"
    