# Csapat: kirahome
import json
import main

class insertClassnameHere:
    def __init__(self):
        self._isRunning = True
        self.activeGames = main.get_games()
        self._state = 0
        with open("content.json") as f:
            self._textcontent = json.load(f)
        
        self._userInput = 0
        """
        state 0: main menu
        state 1: create game
        state 2: bet
        state 3: close game
        state 4: querry
        state 5: quit
        """

        while self._isRunning:
            if self._state == 0:
                print(self._textcontent["main"])
                while self._userInput < 1 or self._userInput > 5:
                    try:
                        self._userInput = int(input("Válasszon a fenti lehetőségek közül (1-5): "))
                    except:
                        pass
                self._state = self._userInput
            elif self._state == 1:
                self.create_game()

                self._state = 0
            
            elif self._state == 2:
                self.create_bet()

                self._state = 0
            
            elif self._state == 3:
                self.close_game()

                self._state = 0

            elif self._state == 5:
                print("Kilépés...")
                break

            self._userInput = 0

    
    def create_game(self):
        gameCreator = ""
        gameName = ""
        gamePlayers = []
        gameEvents = []

        while not gameCreator:
            gameCreator = input("Játékvezető: ")
        
        while not gameName:
            gameName = input("Játékvnév: ")
        
        while True:
            value = input("Játékosnév (vagy 'end' a folytatáshoz): ")
            if value == "end":
                break
            elif value != "":
                gamePlayers.append(value)

        while True:
            value = input("Események (vagy 'end' a folytatáshoz): ")
            if value == "end":
                break
            elif value != "":
                gameEvents.append(value)
        
        main.game_start(gameCreator, gameName, gamePlayers, gameEvents)
    
    def create_bet(self):
        better = ""
        bet = -1
        while not better:
            better = input("Fogadó neve: ")
        
        self.activeGames = main.get_games()

        print("Aktív játékok:")
        for i, game in enumerate(self.activeGames):
            print(f"{i} - {game.gameName}")
        
        while bet < 0 or bet > len(self.activeGames)-1:
            try:
                bet = int(input("Válasszon egy Játékot (szám): "))
            except:
                pass
        
        print(better)
        print(self.activeGames[bet])

    def close_game(self):
        creator = ""
        gname = -1

        while not creator:
            creator = input("Játékkészítő neve: ")
        
        print("Aktív játékok:")
        for i, game in enumerate(self.activeGames):
            print(f"{i} - {game.gameName}")
        
        while gname < 0 or gname > len(self.activeGames)-1:
            try:
                gname = int(input("Válasszon egy Játékot (szám): "))
            except:
                pass
        
        gname = self.activeGames[gname].gameName

        main.exit_game(creator, gname)


            
        
interface = insertClassnameHere()
