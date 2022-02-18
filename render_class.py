#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 11:39:53 2021

@author: robertblack
"""
from os import name, system, path

class Render:
    
    def __init__(self):
        
        self.__m_renderMatrix = self.createRenderMatrix()
        self.__m_playersCoords = self.getPlayerCoords()
        self.__m_cardDeckCords = self.getCardDeckCoords()
        self.__m_tableCoords = self.getTableCoords()
        self.__m_tableSpoonCoords = self.getTableSpoonsCoords()
        
    #Getters
    def getRenderMatrix(self):
        
        return self.__m_renderMatrix
    
    def createRenderMatrix(self):
        
        renderMatrix = []
        
        for row in range(40):
            
            rowList = []
            
            for cols in range(90):
                
                rowList.append(' ')
                
            renderMatrix.append(rowList)
            
        return renderMatrix
    
    def initRenderMatrix(self):
        
        #ResetTheRenderMatrix.
        self.__m_renderMatrix = self.createRenderMatrix()
        
        #Add the table.
        xCoord = self.__m_tableCoords[0]
        yCoord = self.__m_tableCoords[1]
        xDim = xCoord + 11
        yDim = yCoord + 7
        
        for y in range(yCoord, yDim, 1):
            
            for x in range(xCoord, xDim, 1):
                
                #Add the corners.
                if x == xCoord or x == (xDim - 1):
                    
                    if y == yCoord or y == (yDim - 1):
                
                        self.__m_renderMatrix[y][x] = '+'
                        
                #Add top and bottom edges.
                if x > xCoord and x < (xDim - 1):
                    
                    if y == yCoord or y == (yDim - 1):
                
                        self.__m_renderMatrix[y][x] = '-'
                        
                #Add the left and right table edges.
                if x == xCoord or x == (xDim - 1):
                    
                    if y > yCoord and y < (yDim - 1):
                        
                        self.__m_renderMatrix[y][x] = '|'
                        
        #Add the card decks
        leftX_Coords = self.__m_cardDeckCords[0][0]
        leftY_Coords = self.__m_cardDeckCords[0][1]
        leftX_Dim = leftX_Coords + 7
        leftY_Dim = leftY_Coords + 6
        rightX_Corrds =  self.__m_cardDeckCords[1][0]
        rightY_Coords =  self.__m_cardDeckCords[1][1]
        rightX_Dim = rightX_Corrds + 7
        rightY_Dim = rightY_Coords + 6
        defaultLeftRightCardCount = "00"
        leftTopTitle = "Left"
        rightTopTitle = "Right"
        leftAndRightBottomTitle = "Deck"
        
        for y in range(leftY_Coords, leftY_Dim + 1, 1):
            
            for x in range(leftX_Coords, rightX_Dim, 1):
                
                #Add the corners.
                if x == leftX_Coords or x == ((leftX_Dim - 1) - 2) or x == (
                        rightX_Corrds + 2) or x == (rightX_Dim - 1):
                    
                    if y == (leftY_Coords + 1) or y == (leftY_Dim - 1):
                
                        self.__m_renderMatrix[y][x] = '+'
                        
                #Add top and bottom edges.
                if (x > leftX_Coords and x < ((leftX_Dim - 1) - 2)) or (x > (
                        rightX_Corrds + 2) and x < (rightX_Dim - 1)):
                    
                    if y == (rightY_Coords + 1) or y == (rightY_Dim - 1):
                
                        self.__m_renderMatrix[y][x] = '-'
                        
                #Add the left and right table edges.
                if x == leftX_Coords or x == ((leftX_Dim - 1) - 2) or x == (
                        rightX_Corrds + 2) or x == (rightX_Dim - 1):
                    
                    if y > (rightY_Coords + 1) and y < (rightY_Dim - 1):
                        
                        self.__m_renderMatrix[y][x] = '|'
                        
                #Add the filling.
                if x > leftX_Coords and x < ((leftX_Dim - 1) - 2) or x > (
                        rightX_Corrds + 2) and x < (rightX_Dim - 1):
                    
                    if y > (rightY_Coords + 1) and y < (rightY_Dim - 1):
                        
                        self.__m_renderMatrix[y][x] = 'X'
                        
                #Add the top left title.
                if y == leftY_Coords and x - leftX_Coords >= 0 and (
                        x - leftX_Coords) < len(leftTopTitle):
                    
                    self.__m_renderMatrix[y][x] = leftTopTitle[x - leftX_Coords]
                    
                #Add the top right title.
                if y == rightY_Coords and x - (rightX_Corrds + 2) >= 0 and (
                        x - (rightX_Corrds + 2)) < len(rightTopTitle):
                    
                    self.__m_renderMatrix[y][x] = rightTopTitle[
                        x - (rightX_Corrds + 2)]
                    
                #Add the bottom left title.
                if y == leftY_Dim and x - leftX_Coords >= 0 and (
                        x - leftX_Coords) < len(leftAndRightBottomTitle):
                    
                    self.__m_renderMatrix[y][x] = leftAndRightBottomTitle[
                        x - leftX_Coords]
                    
                #Add the bottom right title.
                if y == rightY_Dim and x - (rightX_Corrds + 2) >= 0 and x - (
                        rightX_Corrds + 2) < len(leftAndRightBottomTitle):
                    
                    self.__m_renderMatrix[y][x] = leftAndRightBottomTitle[
                        x - (rightX_Corrds + 2)]
                    
                #Add default left card counter.
                if y == (leftY_Coords + 3) and (x - (leftX_Dim - 2)) >= 0 and (
                        x - (leftX_Dim - 2)) < len(defaultLeftRightCardCount):
                    
                    self.__m_renderMatrix[y][x] = defaultLeftRightCardCount[
                        x - (leftX_Dim - 2)]
                    
                #Add default right card counter.
                if y == (rightY_Coords + 3) and (x - rightX_Corrds) >= 0 and (
                        x - rightX_Corrds) < len(defaultLeftRightCardCount):
                    
                    self.__m_renderMatrix[y][x] = defaultLeftRightCardCount[
                        x - rightX_Corrds]
                
    def updateLeftCardCounter(self, amount):
        
        amt = amount
        amountStr = str(amt)
        
        if len(amountStr) < 2:
            
            s = "0" + amountStr
            amountStr = s
            
        leftX_Coords = self.__m_cardDeckCords[0][0]
        leftY_Coords = self.__m_cardDeckCords[0][1]
        leftX_Dim = leftX_Coords + 7
        leftY_Dim = leftY_Coords + 6
            
        for y in range(leftY_Coords, leftY_Dim + 1, 1):
            
            for x in range(leftX_Coords, leftX_Dim, 1):
        
                #Update left card counter.
                if y == (leftY_Coords + 3) and (x - (leftX_Dim - 2)) >= 0 and (
                        x - (leftX_Dim - 2)) < len(amountStr):
                    
                    self.__m_renderMatrix[y][x] = amountStr[x - (
                        leftX_Dim - 2)]
                    
    def updateRightCardCounter(self, amount):
        
        amt = amount
        amountStr = str(amt)
        
        if len(amountStr) < 2:
            
            s = "0" + amountStr
            amountStr = s
            
        rightX_Corrds =  self.__m_cardDeckCords[1][0]
        rightY_Coords =  self.__m_cardDeckCords[1][1]
        rightX_Dim = rightX_Corrds + 7
        rightY_Dim = rightY_Coords + 6
        
        for y in range(rightY_Coords, rightY_Dim + 1, 1):
            
            for x in range(rightX_Corrds, rightX_Dim, 1):
            
                #Update right card counter.
                if y == (rightY_Coords + 3) and (x - rightX_Corrds) >= 0 and (
                        x - rightX_Corrds) < len(amountStr):
                    
                    self.__m_renderMatrix[y][x] = amountStr[x - rightX_Corrds]
                    
    def addPartisipants(self, participants):
        
        for i in range(len(participants)):
            
            titleStr = ""
            
            if i == 0:
                
                titleStr += "Dealer - " +  participants[i].getName()
                
            else:
                
                titleStr += "Player " + str(
                    i + 1) + " - " + participants[i].getName()
                
            if participants[i].isCurrentPlayer():
                
                titleStr += " #"
                
            xCoord = self.__m_playersCoords[i][0]
            yCoord = self.__m_playersCoords[i][1]
            xDim = xCoord + 24
            yDim = yCoord + 7
            
            for y in range(yCoord, yDim + 1, 1):
            
                for x in range(xCoord, xDim + 1, 1):
            
                    #Add the title.
                    if y == yCoord and x - xCoord >= 0 and (x - xCoord) < len(titleStr):
                        
                        self.__m_renderMatrix[y][x] = titleStr[x - xCoord]
                        
                    #Add card information
                    cards = participants[i].getCards()
                    
                    for z in range(len(cards)):
                        
                        #Add card info.
                        cardStr = ""
                        
                        if participants[i].isCurrentPlayer():
                            
                            cardStr = str(z + 1) + " - " + str(cards[z])
                            
                        else:
                            
                            cardStr = str(z + 1) + " - #Playing Card#"
                        
                        if y == ((yCoord + 2) + z) and x - xCoord >= 0 and (x - xCoord) < len(cardStr):
                            
                            self.__m_renderMatrix[y][x] = cardStr[x - xCoord]
                            
                    #add the spoon
                    if y == (yCoord + 2) and x == (xCoord + 22):
                        
                        self.__m_renderMatrix[y][x] = "O"
                        
                    if y == (yCoord + 3) and x == (xCoord + 22):
                        
                        self.__m_renderMatrix[y][x] = "|"
                        
                    if y == (yCoord + 4) and x == (xCoord + 22):
                        
                        self.__m_renderMatrix[y][x] = "|"
                        
                    #Add spoon number.
                    numOfSpoons = participants[i].getNumberOfSpoons()
                    numSpoonStr = str(numOfSpoons)
                    
                    if y == (yCoord + 4) and x == (xCoord + 23):
                       
                        self.__m_renderMatrix[y][x] = numSpoonStr
                        
    def setNumberOfTableSpoons(self, numberOfSpoons):
        
        xCoord = self.__m_tableSpoonCoords[0]
        yCoord = self.__m_tableSpoonCoords[1]
        xDim = xCoord + 7
        yDim = yCoord + 3
        
        for i in range(numberOfSpoons):
            
            for y in range(yCoord, yDim + 1, 1):
                
                for x in range(xCoord, xDim + 1, 1):
                    
                    #add the spoon
                    if y == yCoord and x == (xCoord + i):

                        self.__m_renderMatrix[y][x] = "O"
                        
                    if y == (yCoord + 1) and x == (xCoord + i):
                     
                        self.__m_renderMatrix[y][x] = "|"
                        
                    if y == (yCoord + 2) and x == (xCoord + i):
                    
                        self.__m_renderMatrix[y][x] = "|"
            
    def getPlayerCoords(self):
        
        #Dealer = 0, Player 2 - 8 = (1 - 7)
        playerCoordsList = [
            [27, 32],
            [27, 5],
            [1, 7],
            [53, 7],
            [1, 16],
            [53, 16],
            [1,25],
            [53, 25]]
        
        return playerCoordsList
    
    def getCardDeckCoords(self):
        
        #Left = 0 to Right = 1
        cardDeckCoordsList = [
            [27, 24],
            [41, 24]]
        
        return cardDeckCoordsList
    
    def getTableCoords(self):
        
        tablekCoordsList = [32, 15]
        
        return tablekCoordsList
    
    def getTableSpoonsCoords(self):
         
        tablekSpoonsCoordsList = [34, 17]
        
        return tablekSpoonsCoordsList
    
    def renderGame(self):
        
        for y in range(40):
            
            for x in range(75):
                
                if x == (75 - 1):
                
                    print(self.__m_renderMatrix[y][x])
                    
                else:
                
                    print(self.__m_renderMatrix[y][x], end = "")
                    
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

    def showRules(self):
        
        #Find the path to the words text file appropriate to the 
        #current operating system.
        absPathToFile = path.dirname(path.abspath( __file__ ))
        absPathToFile += path.sep
        absPathToFile += "rules_of_spoons.txt"
        
        showRules = True
        
        while showRules:
        
            try:
            
                #Open the file and the game rules.
                rulesFile = open(absPathToFile, "r")
                
                self.clearScreen()
                   
                for line in rulesFile:
                
                    print(line)
                   
                rulesFile.close()
               
            except IOError:
                
                self.clearScreen()
               
                closeRules = input("Can not open the rules file at the " +
                                   "moment, sorry for any inconvenience.\n" +
                                   "Please type '--resume' to continue with " +
                                   "the game.")
            
            while True:
                
                closeRules = input("Please type '--resume' to continue with the " +
                               "game:   ")
    
                if closeRules.strip() == "--resume":
                    
                    showRules = False
                    break
                
                else:
                    
                    self.clearScreen()
                    print("\nI did not understand your input, please try again.\n")   
            
        
        self.clearScreen()
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        