#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:15:29 2021

@author: robertblack
"""
import game_enums as ens
import dealer_class as dlr
import player_class as ply
import participant_class as prt

class ParticapantFactory:
    
    @staticmethod
    def createParticipant(name, typeParticipant):
        
        if typeParticipant == ens.PARTICIPANT.DEALER:
            
            return dlr.Dealer(name)
            
        elif typeParticipant == ens.PARTICIPANT.PLAYER:
            
            return ply.Player(name)
            
        else:
            
            return prt.Participant(name)