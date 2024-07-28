
from random import choice

from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def rps():
    games = 0
    player_wins = 0
    machine_wins = 0

    def play_rps():
        nonlocal games
        nonlocal player_wins
        nonlocal machine_wins

        while True:
            player_choice = input("\nChoose between:\n1 for rock\n2 for paper\n3 for scissors\n")
            if player_choice in ["1", "2", "3"]:
                break

        machine_choice = int(choice("123"))

        player_choice = int(player_choice)

        def choose_winner(player, machine):
            nonlocal player_wins
            nonlocal machine_wins

            if player == 1 and machine == 3:
                player_wins += 1
                return "Player Wins 😎"
            elif player == 2 and machine == 1:
                player_wins += 1
                return "Player Wins 😎"
            elif player == 3 and machine == 2:
                player_wins += 1
                return "Player Wins 😎"
            elif player == machine:
                return "This is a Tie 😑"
            else:
                machine_wins += 1
                return "Machine Wins 🤖"
            
        games += 1

        print(f"You choose {str(RPS(player_choice)).replace("RPS.", "")}\n")
        print(f"The machine choose {str(RPS(machine_choice)).replace("RPS.", "")}\n")

        print(f"{choose_winner(player_choice, machine_choice)}\n")

        print(f"Games Played: {games}")
        print(f"Player Wins: {player_wins}")
        print(f"Machine Wins: {machine_wins}\n")

        while True:
            play_again = input("Play again? (y/n)\n")
            if play_again.lower() not in ["y", "n"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            play_rps()
        else:
            print("\nThank you for playing!\n")
            return
        
    return play_rps

if __name__ == "__main__":
    jogo1 = rps()

    jogo1()
            
        
