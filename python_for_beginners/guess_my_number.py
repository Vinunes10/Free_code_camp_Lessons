
from random import choice

def gmn():
    games = 0
    player_wins = 0
    machine_wins = 0

    def play_gmn():
        nonlocal games
        nonlocal player_wins
        nonlocal machine_wins

        while True:
            player_choice = input("Guess a number between 1, 2 or 3: ")
            if player_choice in ["1", "2", "3"]:
                break
        
        machine_choice = int(choice("123"))

        player_choice = int(player_choice)

        def choose_winner(player, machine):

            nonlocal player_wins
            nonlocal machine_wins

            if player_choice == machine_choice:
                player_wins += 1
                return "Player Wins 😎"
            else:
                machine_wins += 1
                return "Machine Wins 🤖"

        games += 1

        print(f"\nYou choose {player_choice}")
        print(f"The machine choose {machine_choice}\n")

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
            play_gmn()
        else:
            print("\nThank you for playing!\n")
            return
        
    return play_gmn

if __name__ == "__main__":
    jogo1 = gmn()

    jogo1()