#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:00:44 2021

@author: robertblack
"""
from enum import Enum

class CARD_VALUE(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    
class CARD_TYPE(Enum):
    ACE = "Ace"
    TWO = "Two"
    THREE = "Three"
    FOUR = "Four"
    FIVE = "Five"
    SIX = "Six"
    SEVEN = "Seven"
    EIGHT = "Eight"
    NINE = "Nine"
    TEN = "Ten"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"
    
class CARD_SUIT(Enum):
    HEARTS = "Hearts"     #red colour
    SPADES = "Spades"     #black colour
    DIAMONDS = "Diamonds"   #red colour
    CLUBS = "Clubs"      #black colour
    
class PARTICIPANT(Enum):
    DEALER = 1    #red colour
    PLAYER = 2    #black colour