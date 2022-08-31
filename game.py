from playground import PlayGround
from player import TTTPlayer


def get_input(is_field_input, input_text="Enter your Value:"):
    output = 0
    if is_field_input:
        while output < 1 or output > 4:
            output = int(input(input_text))
        return output
    return input(input_text)


class GameObj:
    def __init__(self, player1_name, player2_name):
        self.players["player_1"] = TTTPlayer(player1_name)
        self.players["player_2"] = TTTPlayer(player2_name)
        self.players["player_1"]._mark = 'x'
        self.players["player_2"]._mark = 'o'
        self.playground = PlayGround()

    def get_input_of_player(self):
        correct_input = False
        while not correct_input:
            self.row = get_input(True, "Enter your row. ") - 1
            self.col = get_input(True, "Enter your col. ") - 1
            if self.playground.field[self.row][self.col] == ' ':
                correct_input = True
            else:
                print("Please, choose an Empty Field.")

    def display_field(self):
        print("-------")
        print("|"+self.playground.field[0][0]+"|"+self.playground.field[0][1]+"|"+self.playground.field[0][2]+"|")
        print("|"+self.playground.field[1][0]+"|"+self.playground.field[1][1]+"|"+self.playground.field[1][2]+"|")
        print("|"+self.playground.field[2][0]+"|"+self.playground.field[2][1]+"|"+self.playground.field[2][2]+"|")
        print("-------")

    def get_player_name(self, which_player):
        return self.players["player_" + str(which_player)].get_name()

    def check_winner(self):
        board = self.playground.field
        mark = self.players["player_"+str(self.current_player)]._mark
        someone_won = ((board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or  # for row1

                (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or  # for row2

                (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or  # for row3

                (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or  # for Colm1

                (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or  # for Colm 2

                (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or  # for colm 3

                (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or  # diagonal 1

                (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark))  # diagonal 2
        if someone_won:
            return mark
        return someone_won

    def check_if_full(self):
        for row in range(len(self.playground.field)):
            for col in range(len(self.playground.field[row])):
                if self.playground.field[row][col] == ' ':
                    return False
        return True

    def set_players(self):
        self.playground.field[int(self.row)][int(self.col)] = self.players["player_" + str(self.current_player)]._mark

    def end_round(self):
        if self.current_player == 2:
            self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 2
        self.row = "NO_ROW_CURRENTLY"
        self.col = "NO_COL_CURRENTLY"
        print("Your Turn, " + self.players["player_"+str(self.current_player)]._name + ":")

    players = {"player_1": {}, "player_2": {}}
    current_player = 1
    play_ground = {}
    row = "NO_ROW_CURRENTLY"
    col = "NO_COL_CURRENTLY"
