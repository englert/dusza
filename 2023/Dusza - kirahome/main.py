# Csapat: kirahome

from dataclasses import dataclass


def game_start(creator: str, game_name: str, people: list, events: list):
    with open("jatekok.txt", "a") as f:
        f.writelines(f"{creator};{game_name};{len(people)};{len(events)}\n")
        for person in people:
            f.writelines(f"{person}\n")
        for event in events:
            f.writelines(f"{event}\n")

@dataclass
class activegames:
    gameCreator: str
    gameName: str
    gamePlayers: list
    gameEvents: list

def get_games():
    currentGames = []
    with open("jatekok.txt", "r") as f:
        data = [v.strip() for v in f.readlines()]
        for i, value in enumerate(data):
            if ";" in value:
                values = value.split(";")
                currentGames.append(activegames(values[0], values[1], data[i+1:i+int(values[2])+1], data[int(values[2])+i+1:i+int(values[3])+int(values[2])+1]))
        return currentGames


@dataclass
class betting:
    player: str
    score: int = 100

adatok = []

def bet(name: str):
    if name not in adatok:
        adatok.append(betting(name))
        for i in adatok:
            if i.player == name:
                return i.score

    else:
        for i in adatok:
            if i.player == name:
                return i.score

activegames2 = get_games()
def exit_game(creator_name, game_name):
    with open("eredmenyek.txt", "a") as f:
        for asfd in activegames2:
            print(asfd, creator_name, game_name, sep="/n")
            if creator_name == asfd.gameCreator and game_name == asfd.gameName:
                f.write(game_name)
            



print(bet("peter"))
