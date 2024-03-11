### main ###

from board import Board
from piece import Piece

current_player = 'w'

def print_board(state):
        for y in range(9):
            for x in range(7):
                print(state[y][x],end="")
            print()
        
if __name__ == "__main__":
    print(" * Starting...")
    b = Board()
    print("Position:")
    print_board(b.state)
    print("Actions for "+ current_player +":")
    print(b.get_moves(current_player))
    print(" * End")
