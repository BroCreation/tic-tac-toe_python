import random

def populate_2D_list(size):
    result = []
    for itr in range(size):
        result.append(list(range(size*itr, size*(itr+1))))
    return result

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_input(self):
        try:
            self.input  = int(input(f"Enter where you want to place {self.symbol} Symbol: "))
            if(self.input > 8 or self.input < 0):
                raise Exception("Error, Out Of Range.")
        except ValueError:
            print("Error, Incorrect Input Value.")
            self.get_input()
        except Exception as e:
            print(e)
            self.get_input()

class Bot():
    def __init__(self):
        self.symbol = 'O'

    def get_input(self):
        self.input = random.randint(0, 8)
        print(f'Bot placed {self.symbol} at {self.input} index.')
    

class Board:
    def __init__(self, size):
        self.size = size
        self.board = populate_2D_list(size)

    def __call__(self):
        for i in range(self.size):
            for j in range(self.size):
                print("|", self.board[i][j], end=" ")
            print("|")

    def assign_symbol(self, current_player):
        symbol = current_player.symbol
        input = current_player.input
        row = input // self.size
        col = input % self.size
        if(self.board[row][col] != symbols[0] and self.board[row][col] != symbols[1]):
            self.board[row][col] = symbol
        else:
            print("Can't Be Doing that.")
            current_player.get_input()
            self.assign_symbol(current_player)

    def check_board_winner(self, current_player):
        symbol = current_player.symbol
        for i in range(self.size):
            if(self.board[i][0] == symbol and self.board[i][1] == symbol and self.board[i][2] == symbol):
                return True
            elif(self.board[0][i] == symbol and self.board[1][i] == symbol and self.board[2][i] == symbol):
                return True
            elif(self.board[0][0] == symbol and self.board[1][1] == symbol and self.board[2][2] == symbol):           
                return True
            elif(self.board[0][2] == symbol and self.board[1][1] == symbol and self.board[2][0] == symbol):
                return True
        # if for loops executes all the way then return False in else
        else:
            return False


board = Board(3)
symbols = ('X', 'O')
current_player = player1 = Player(symbols[0])
opposing_player = player2 = Player(symbols[1])
computer = bot = Bot()
choice_player = ''
choices = ['bot', 'b', 'human', 'h']
is_bot = False

choice_player = str(input('Who you wanna play up against (Bot/Human): ').lower())

while(choice_player not in choices):
    print("Not Defined. (Choose 'b' for bot or 'h' for human)")
    choice_player = str(input('Who you wanna play up against (Bot/Human): ').lower())

if choice_player == 'bot' or choice_player == 'b':
    is_bot = True
    opposing_player = computer

while(True):
    board()
    current_player.get_input()
    board.assign_symbol(current_player)

    if(board.check_board_winner(current_player)):
        board()
        print(f"Congratulations Player {current_player.symbol}. You won fair and square!")
        break

    if(current_player == player1 and (opposing_player == player2 or opposing_player == computer)):
        if(is_bot):
            current_player = computer
        else:
            current_player = player2 
        opposing_player = player1
    else:
        current_player = player1 
        if(is_bot):
            opposing_player = computer
        else:
            opposing_player = player2

input('Press enter to exit(): ')
            