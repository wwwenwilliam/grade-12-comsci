from Board import Board
from Computer import Computer
from Interface import Messager
from Interface import Button
from Interface import Menu
from Scoreboard import Scoreboard
from PlayerInfo import PlayerInfo
from Interface import Keyboard

gameState = 0 #-1-menu, 0-start screen, 1-ship placement, 2-play
playerBoard = Board(550, 0)
computerBoard = Board(0, 0)
computer = Computer(playerBoard)
player = PlayerInfo()

turn = True #True-player, False-comp
menuState = None #0-help, 1-scores, 2-exit

turnMessager = Messager(200, 550)
sinkMessager = Messager(450, 50)
bottomRightButton = Button(500, 510, 200, 80)

title = None
menu = Menu(710, 510, 330, 80, [Button(710, 510, 100, 80, "?"), Button(810, 510, 130, 80, "SCORES"), Button(940, 510, 100, 80, "EXIT")])
instructions = []

scoreboard = Scoreboard()


def reset():
    #resets all variables to start state
    global gameState, playerBoard, computerBoard, turn, computer, turnMessager, sinkMessager, bottomRightButton, scoreboard, player, menu, menuState
    playerBoard = Board(550, 0)
    computerBoard = Board(0, 0)
    computer = Computer(playerBoard)
    playerBoard.createRandomBoard()
    computerBoard.createRandomBoard()
    
    bottomRightButton.setMessage("READY")
    turnMessager.setMessage("PLACE YOUR SHIPS")
    sinkMessager.setMessage("")
    turn = True
    player.score = 0
    player.name = ""
    
    gameState = 0
    
def openFile(file):
    outList = []
    try:
        with open(file, "r") as f:
            for ln in f:
                outList.append(ln.strip())
    except IOError:
        print("{} not found".format(file))
        return None
    return outList

def setup():
    global playerBoard, computerBoard, title, instructions
    size(1050, 600)
    textAlign(CENTER, CENTER)
    
    #setup board
    Board.setDimensionsFromFile("boardsetup.txt")
    
    #instructions
    instructions = openFile("instructions.txt")
    if instructions == None:
        instructions = ["instructions not found"]
    
    #generate boards
    playerBoard.createRandomBoard()
    computerBoard.createRandomBoard()
    
    #setup graphics
    title = loadImage("battleshiplogo.png")
    font = loadFont("Impact.vlw")
    textFont(font, 32)
    
    #scoreboard.clearScores() #######BE CAREFUL WHEN UNCOMMENTING
    
    
def draw():
    #no logic in here, only graphics
    global gameState, playerBoard, computerBoard, turnMessager, sinkMessager, bottomRightButton, scoreboard, player, menu, menuState, title, instructions
    background(0)
    

    if gameState == -1:
        #menu was clicked
        menu.drawMenu()
        if menuState[1] == 0:
            #help
            fill(255)
            textSize(20)
            for i in range(len(instructions)):
                text(instructions[i], 500, 25*i+25)
        elif menuState[1] == 1:
            #scores
            scoreboard.displayScores(300, 0)
            text("Your High Score:", 850, 50)
            text(str(scoreboard.findScore(player)), 850, 100)
            text("Your Current Score:", 850, 150)
            text(str(player.score), 850, 200)
    
    if gameState == 0:
        #add some title picture
        imageMode(CENTER)
        image(title, 525, 100)
        
        #display player name
        fill(255)
        textSize(40)
        text("ENTER YOUR NAME:", 350, 300)
        textAlign(BASELINE, CENTER)
        player.displayName(550, 300)
        textAlign(CENTER, CENTER)
        
        text("CLICK ANYWHERE TO BEGIN", 500, 400)
        
        #menu
        menu.drawMenu()
        
        
    elif gameState == 1:
        #draw boards
        playerBoard.drawBoard()
        playerBoard.drawShips()
        
        computerBoard.drawBoard()
        #computerBoard.drawShips()
        
        #draw message
        turnMessager.printMessage(40)
        
        #draw button
        bottomRightButton.drawButton()
        menu.drawMenu()
        
    elif gameState == 2:
        #draw boards
        playerBoard.drawBoard()
        playerBoard.drawShips()
        playerBoard.drawHits()
        
        computerBoard.drawBoard()
        computerBoard.drawShips()
        computerBoard.drawHits()
        
        #draw any messages
        turnMessager.printMessage(40)
        sinkMessager.printMessage(40)
        
        #draw button
        bottomRightButton.drawButton()
        menu.drawMenu()
        
        
def keyPressed():
    global gameState, player
    if gameState == 0:
        #player should enter name in the menu
        player.name = Keyboard.keyIn(player.name)
        
def mousePressed():
    global gameState, playerBoard, computerBoard
    
    if gameState == 1:
        #only for moving ships
        playerBoard.mouseClickedCheck()
        
def mouseWheel(event):
    global gameState, menuState, scoreboard
    
    if gameState == -1 and menuState[1] == 1:
        scoreboard.incrementStart(event.getCount())

def mouseReleased():
    #most logic should go in here
    global gameState, playerBoard, computerBoard, turn, computer, turnMessager, sinkMessager, bottomRightButton, scoreboard, player, menu, menuState
    
    #menu takes priority for clicks
    if menu.click() != None:
        #saves the gameState when moving to menu
        if gameState == -1:
            if menuState[1] == menu.click():
                gameState = menuState[0]
            else:
                menuState[1] = menu.click()
        else:
            menuState = [gameState, menu.click()]
            gameState = -1
        #resets scoreboard display whenever menu button is clicked
        scoreboard.resetStart()
        
        #exit for exit button
        if menuState[1] == 2:
            exit()
        
    elif gameState == -1:
        if menuState[1] == 0:
            #help screen
            pass
        elif menuState[1] == 1:
            #scores screen
            pass
    
    elif gameState == 0 and menu.click() == None and player.name != "":
        #set buttons message to "Ready" before going to gameState = 1
        bottomRightButton.setMessage("READY")
        turnMessager.setMessage("PLACE YOUR SHIPS")
        gameState = 1
        
    elif gameState == 1:
        #player places piece
        playerBoard.mouseReleasedCheck()
        
        if bottomRightButton.isClicked():
            #moves to next state
            bottomRightButton.setMessage("RESET")
            turnMessager.setMessage("PLAYER'S TURN")
            gameState = 2
        
        
    elif gameState == 2:
        if bottomRightButton.isClicked():
            #reset button
            reset()
        if not computerBoard.checkLoss() or playerBoard.checkLoss():
            if turn:
                #player clicks for their turn
                sinkMessager.setMessage("")
                if computerBoard.clickToFire(sinkMessager):
                    player.score += 1
                    turnMessager.setMessage("COMPUTER'S TURN")
                    
                    if computerBoard.checkLoss():
                        turnMessager.setMessage("PLAYER WINS")
                        #update scoreboard
                        scoreboard.addScore(player)
                        scoreboard.updateFile()
                        
                    turn = not(turn)
                    
            else:
                #player clicks anywhere to pass AI's turn
                computer.makeMove()
                
                turnMessager.setMessage("PLAYER'S TURN")
                
                if playerBoard.checkLoss():
                    turnMessager.setMessage("COMPUTER WINS")
                    
                turn = not(turn)

        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
