#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:18:28 2021

@author: robertblack
"""
from random import randint

import spoon_class as spn

class TableSpoons:
    
    def __init__(self, numberOfSpoons = 0):
        
        self.__m_spoons = self.__addSpoons(numberOfSpoons)
        
    def __addSpoons(self, numberOfSpoons):
        
        spoons = []
        
        for i in range(numberOfSpoons):
        
            spoon = spn.Spoon()
            spoons.append(spoon)
                
        return spoons
    
    def getNumberOfSpoonsLeft(self):
        
        return len(self.__m_spoons)
    
    def takeSpoon(self):
        
        spoon = None
        
        if len(self.__m_spoons) > 0:
        
            randNum = randint(0, len(self.__m_spoons) -1)
            spoon = self.__m_spoons[randNum]
            del self.__m_spoons[randNum]
        
        return spoon
    
    def addSpoon(self, spoon):
        
        randNum = randint(0, len(self.__m_spoons) - 1)
        self.__m_spoons.insert(randNum, spoon)
        
    def __str__(self):
        
        return str(self.__m_numSpoons) + " sppons on the table."