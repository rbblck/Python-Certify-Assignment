#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:38:56 2021

@author: robertblack
"""
import participant_class as pc

class Player(pc.Participant):
    
    def __init__(self, name = "name"):
        
        pc.Participant.__init__(self, name)
        
    def passCardToPlayer(self, cardIndex):
                
        return self._m_hand.dicardCard(cardIndex)
        
    def __str__(self):
        
        return "My name is : " + self._m_name + " and I am a player"