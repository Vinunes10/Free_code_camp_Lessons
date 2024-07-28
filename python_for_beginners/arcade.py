def arc():

    def choose_game():

        print("Welcome to the arcade!")

        while True:
            game = input("\nPlease choose a game:\n1 for rock, paper and scissors\n2 for guess my number\n\nType x to exit\n")
            if game.lower() in ["1", "2", "x"]:
                break
        
        if game == "1":
            from rps import rps

            jogo = rps()

            jogo()

            choose_game()

        if game == "2":
            from guess_my_number import gmn

            jogo = gmn()

            jogo()

            choose_game()

        if game.lower == "x":
            return
        
    return choose_game

if __name__ == "__main__":
    player1 = arc()

    player1()