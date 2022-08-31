from game import GameObj


def start():
    name1 = input("first Player, enter your Name: ")
    name2 = input("now you, second One: ")
    game = GameObj(name1, name2)
    while not game.check_if_full():
        game.display_field()
        game.get_input_of_player()
        game.set_players()
        if game.check_winner():
            print(game.players["player_"+str(game.current_player)]._name+" won")
            game.display_field()
            break
        game.end_round()


if __name__ == '__main__':
    start()
