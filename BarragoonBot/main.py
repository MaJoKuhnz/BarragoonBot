### main ###

from board import Board
from piece import Piece
from random import randint

current_player = 'b'
g=100
max_m=10000
wins=0

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
        for i in range(g):
                print("Game " + str(i+1))
                current_player = 'b'
                b.reset_board()
                b.delete_piece(Piece((4,7),"w2"))
                b.add_piece(Piece((4,6),"w2"))
                j=0
                while(1):
                        m=b.get_moves(current_player)
                        if(len(m)==0):break
                        if(max_m<j):
                                current_player='d'
                                break
                        if(current_player=='w'):current_player='b'
                        else:current_player='w'
                        j+=1
                        cm=m[randint(0,len(m)-1)]
                        if(len(cm)>2):
                                b.delete_piece(cm[1])
                                b.add_piece(cm[0])
                                b.delete_piece(cm[3])
                                while(1):
                                        r=randint(0,15)
                                        x,y=randint(0,6),randint(0,8)
                                        if(b.state[y][x]!="  "):continue
                                        if(r==0):
                                                b.add_piece(Piece((x,y),"xx"))
                                                break
                                        if(r==1):
                                                b.add_piece(Piece((x,y),"tt"))
                                                break
                                        if(r==2):
                                                b.add_piece(Piece((x,y),"th"))
                                                break
                                        if(r==3):
                                                b.add_piece(Piece((x,y),"tv"))
                                                break
                                        if(r==4):
                                                b.add_piece(Piece((x,y),"or"))
                                                break
                                        if(r==5):
                                                b.add_piece(Piece((x,y),"ol"))
                                                break
                                        if(r==6):
                                                b.add_piece(Piece((x,y),"ou"))
                                                break
                                        if(r==7):
                                                b.add_piece(Piece((x,y),"od"))
                                                break
                                        if(r==8):
                                                b.add_piece(Piece((x,y),"rr"))
                                                break
                                        if(r==9):
                                                b.add_piece(Piece((x,y),"rl"))
                                                break
                                        if(r==10):
                                                b.add_piece(Piece((x,y),"ru"))
                                                break
                                        if(r==11):
                                                b.add_piece(Piece((x,y),"rd"))
                                                break
                                        if(r==12):
                                                b.add_piece(Piece((x,y),"ll"))
                                                break
                                        if(r==13):
                                                b.add_piece(Piece((x,y),"lr"))
                                                break
                                        if(r==14):
                                                b.add_piece(Piece((x,y),"ld"))
                                                break
                                        if(r==15):
                                                b.add_piece(Piece((x,y),"lu"))
                                                break
                if(current_player=='d'):
                        print("draw after 10000 moves")
                        wins+=0
                elif(current_player=='b'):
                        wins+=1
                        print("win by white")
                else:
                        wins-=1
                        print("win by black")
                
                
                        
        print("Win rate: "+str(wins/g))
        print(" * End")
