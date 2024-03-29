### board ###

from piece import Piece

class Board:
    
    def __init__(self,state):
        self.state=state
        self.plist=list()
        
    def __init__(self):
        self.state=[["  " for i in range(7)] for i in range(9)]
        self.plist=list()
        self.reset_board()

    def reset_board(self):
        self.plist=list()
        for y in range(9):
            for x in range(7):
                self.state[y][x]="  "
        # white pieces
        self.add_piece(Piece((1,8),"w4"))
        self.add_piece(Piece((2,8),"w3"))
        self.add_piece(Piece((4,8),"w3"))
        self.add_piece(Piece((5,8),"w4"))
        self.add_piece(Piece((2,7),"w2"))
        self.add_piece(Piece((3,7),"w3"))
        self.add_piece(Piece((4,7),"w2"))
        # black pieces
        self.add_piece(Piece((1,0),"b4"))
        self.add_piece(Piece((2,0),"b3"))
        self.add_piece(Piece((4,0),"b3"))
        self.add_piece(Piece((5,0),"b4"))
        self.add_piece(Piece((2,1),"b2"))
        self.add_piece(Piece((3,1),"b3"))
        self.add_piece(Piece((4,1),"b2"))
        # barragoons
        self.add_piece(Piece((0,4),"xx"))
        self.add_piece(Piece((1,3),"xx"))
        self.add_piece(Piece((1,5),"xx"))
        self.add_piece(Piece((2,4),"xx"))
        self.add_piece(Piece((6,4),"xx"))
        self.add_piece(Piece((5,3),"xx"))
        self.add_piece(Piece((5,5),"xx"))
        self.add_piece(Piece((4,4),"xx"))
        

    def add_piece(self,piece):
        self.state[piece.pos[1]][piece.pos[0]]=piece.type
        self.plist.append(piece)

    def delete_piece(self,piece):
        for i in range(len(self.plist)-1):
            if(self.plist[i]==piece):
                del(self.plist[i])
        self.state[piece.pos[1]][piece.pos[0]]="  "

    def get_moves(self,player):
        moves=list()
        for i in range(len(self.plist)-1):
            if(self.plist[i].type[0]=="w"):
                if(self.plist[i].type[1]=="2"):
                    if((self.plist[i].pos[0])+1<6):
                        if(self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]),"w2"),self.plist[i]))
                    if(self.plist[i].pos[0]-1>-1):
                        if(self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]),"w2"),self.plist[i]))
                    if(self.plist[i].pos[1]+1<9):
                        if(self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+1),"w2"),self.plist[i]))
                    if(self.plist[i].pos[1]-1>0):
                        if(self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-1),"w2"),self.plist[i]))
                    
                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[1]-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ol" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="th" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  "):
                                moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-2),"w2"),self.plist[i]))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[1]+2<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="or" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="th" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  "):
                                moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+2),"w2"),self.plist[i]))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="od" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  ") and
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]),"w2"),self.plist[i]))
                    if(self.plist[i].pos[0]-1>-1 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ou" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  ") and
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]),"w2"),self.plist[i]))

                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),"w2"),self.plist[i]))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),"w2"),self.plist[i]))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[1]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rd" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  ") and
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),"w2"),self.plist[i]))
                    if(self.plist[i].pos[0]-1>-1 and self.plist[i].pos[1]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ru" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  ") and
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"w2"),self.plist[i]))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="lr" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"w2"),self.plist[i]))
                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ll" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),"w2"),self.plist[i]))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rr" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),"w2"),self.plist[i]))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[1]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="rl" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),"w2"),self.plist[i]))

                    # taking
                    
                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[1]-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ol" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="th" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]!="  " or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]!="tt" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]!=player+"2" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]!=player+"3" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-2),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0],self.plist[i].pos[1]-2),self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]])))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[1]+2<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="or" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="th" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]!="  " or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]!="tt" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]!=player+"2" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]!=player+"3" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+2),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0],self.plist[i].pos[1]+2),self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]])))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="od" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  ") and
                            (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]!="  " or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]!="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]!=player+"2" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]!=player+"3" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]),self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2])))
                    if(self.plist[i].pos[0]-1>-1 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ou" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  ") and
                            (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]!="  " or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]!="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]!=player+"2" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]!=player+"3" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]),self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2])))

                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1])))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1])))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[1]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rd" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  ") and
                            (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1])))
                    if(self.plist[i].pos[0]-1>-1 and self.plist[i].pos[1]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ru" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  ") and
                            (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1])))
                    if(self.plist[i].pos[1]+1<7 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="lr" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1])))
                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ll" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1])))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rr" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1])))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[1]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="rl" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),"w2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1])))
                
                elif(self.plist[i].type[1]=="3"):
                    if((self.plist[i].pos[0])+2<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]),"w3"),self.plist[i]))
                    if((self.plist[i].pos[0])-2>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]),"w3"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="th") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+2),"w3"),self.plist[i]))
                    if((self.plist[i].pos[1])-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="th") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-2),"w3"),self.plist[i]))
                               
                    if((self.plist[i].pos[0])+1<7 and self.plist[i].pos[1]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),"w3"),self.plist[i]))
                    if((self.plist[i].pos[0])-1>-1 and self.plist[i].pos[1]+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"w3"),self.plist[i]))
                    if(self.plist[i].pos[0]-1>-1 and self.plist[i].pos[1]-1<9):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"w3"),self.plist[i]))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[1]+1<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt")and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),"w3"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-3>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),"w3"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"w3"),self.plist[i]))
                    if((self.plist[i].pos[0])-3>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),"w3"),self.plist[i]))
                    if((self.plist[i].pos[0])+3<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"w3"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"w3"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"w3"),self.plist[i]))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"w3"),self.plist[i]))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"w3"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"w3"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),"w3"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"w3"),self.plist[i]))
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"w3"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"w3"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"w3"),self.plist[i]))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),"w3"),self.plist[i]))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"w3"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),"w3"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]+1),"w3"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"w3"),self.plist[i]))
                    if((self.plist[i].pos[1])-2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"w3"),self.plist[i]))

                    # take
                    
                    if((self.plist[i].pos[1])-3>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and
                           (self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]!="  " or
                            self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]!="w2" or
                            self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]!="w3" or
                            self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]])))
                    if((self.plist[i].pos[1])+3<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tv") and
                           (self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]!="  " or
                            self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]!="w2" or
                            self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]!="w3" or
                            self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]])))
                    if((self.plist[i].pos[0])-3>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]!="  " or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]!="w2" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]!="w3" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]),self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3])))
                    if((self.plist[i].pos[0])+3<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]!="  " or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]!="w2" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]!="w3" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]),self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3])))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="w2" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="w3" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1])))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="w2" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="w3" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1])))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="w2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="w3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2])))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="w2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="w3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2])))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="w2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="w3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2])))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="w2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="w3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2])))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="w2" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="w3" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1])))
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="w2" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="w3" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1])))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="w2" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="w3" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1])))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="w2" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="w3" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1])))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="w2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="w3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2])))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="w2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="w3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2])))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]!="w2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]!="w3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2])))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]!="w2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]!="w3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]+1),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2])))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="w2" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="w3" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1])))
                    if((self.plist[i].pos[1])-2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="w2" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="w3" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="w4")):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"w3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1])))
                
                if(self.plist[i].type[1]=="4"):
                     if((self.plist[i].pos[1])-3>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])-3>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])+3<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"w4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"w4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"w4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"w4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]+1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])-2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"w4"),self.plist[i]))
                
                    if((self.plist[i].pos[1])-4>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]-4][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-4),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+4<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]+4][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+4),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])-4>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-4]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-4),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])+4<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+4]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+4),"w4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-3>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-3),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="th") and 
                           (self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+3),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])-3>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]-1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])+3<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="tt") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]+1),"w4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]-3>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]-1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]+3<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="th") and
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]+1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+3),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])-3>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-3),"w4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-3>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-3),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+3),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])+3<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]-1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[0])-3>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]-1),"w4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]+3<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="or" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]-1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]-3>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]+1),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+3),"w4"),self.plist[i]))
                    if((self.plist[i].pos[1])-3<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-3),"w4"),self.plist[i]))

                    
            if(self.plist[i].type[0]=="b"):
                if(self.plist[i].type[1]=="2"):
                    if((self.plist[i].pos[0])+1<6):
                        if(self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]),"b2"),self.plist[i]))
                    if(self.plist[i].pos[0]-1>-1):
                        if(self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]),"b2"),self.plist[i]))
                    if(self.plist[i].pos[1]+1<9):
                        if(self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+1),"b2"),self.plist[i]))
                    if(self.plist[i].pos[1]-1>0):
                        if(self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-1),"b2"),self.plist[i]))
                    
                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[1]-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ol" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="th" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  "):
                                moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-2),"b2"),self.plist[i]))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[1]+2<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="or" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="th" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  "):
                                moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+2),"b2"),self.plist[i]))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="od" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  ") and
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]),"b2"),self.plist[i]))
                    if(self.plist[i].pos[0]-1>-1 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ou" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  ") and
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]),"b2"),self.plist[i]))

                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),"b2"),self.plist[i]))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),"b2"),self.plist[i]))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[1]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rd" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  ") and
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),"b2"),self.plist[i]))
                    if(self.plist[i].pos[0]-1>-1 and self.plist[i].pos[1]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ru" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  ") and
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"b2"),self.plist[i]))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="lr" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"b2"),self.plist[i]))
                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ll" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),"b2"),self.plist[i]))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rr" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),"b2"),self.plist[i]))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[1]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="rl" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  "):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),"b2"),self.plist[i]))

                    # taking
                    
                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[1]-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ol" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="th" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]!="  " or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]!="tt" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]!=player+"2" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]!=player+"3" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-2),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0],self.plist[i].pos[1]-2),self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]])))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[1]+2<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="or" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="th" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]!="  " or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]!="tt" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]!=player+"2" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]!=player+"3" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+2),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0],self.plist[i].pos[1]+2),self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]])))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="od" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  ") and
                            (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]!="  " or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]!="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]!=player+"2" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]!=player+"3" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]),self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2])))
                    if(self.plist[i].pos[0]-1>-1 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ou" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  ") and
                            (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]!="  " or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]!="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]!=player+"2" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]!=player+"3" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]),self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2])))

                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1])))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1])))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[1]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rd" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  ") and
                            (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1])))
                    if(self.plist[i].pos[0]-1>-1 and self.plist[i].pos[1]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ru" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  ") and
                            (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1])))
                    if(self.plist[i].pos[1]+1<7 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="lr" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1])))
                    if(self.plist[i].pos[1]-1>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ll" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1])))
                    if(self.plist[i].pos[1]+1<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rr" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!="tt" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1])))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[1]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="rl" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  ") and
                            (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!="tt" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]!=player+"4")):
                                moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),"b2"),self.plist[i],
                                         "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1])))
                
                elif(self.plist[i].type[1]=="3"):
                    if((self.plist[i].pos[0])+2<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]),"b3"),self.plist[i]))
                    if((self.plist[i].pos[0])-2>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]),"b3"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="th") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+2),"b3"),self.plist[i]))
                    if((self.plist[i].pos[1])-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="th") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-2),"b3"),self.plist[i]))
                               
                    if((self.plist[i].pos[0])+1<7 and self.plist[i].pos[1]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-1),"b3"),self.plist[i]))
                    if((self.plist[i].pos[0])-1>-1 and self.plist[i].pos[1]+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"b3"),self.plist[i]))
                    if(self.plist[i].pos[0]-1>-1 and self.plist[i].pos[1]-1<9):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+1),"b3"),self.plist[i]))
                    if(self.plist[i].pos[0]+1<7 and self.plist[i].pos[1]+1<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt")and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+1),"b3"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-3>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),"b3"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"b3"),self.plist[i]))
                    if((self.plist[i].pos[0])-3>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),"b3"),self.plist[i]))
                    if((self.plist[i].pos[0])+3<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"b3"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"b3"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"b3"),self.plist[i]))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"b3"),self.plist[i]))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"b3"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"b3"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),"b3"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"b3"),self.plist[i]))
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"b3"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"b3"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"b3"),self.plist[i]))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),"b3"),self.plist[i]))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"b3"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),"b3"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]+1),"b3"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"b3"),self.plist[i]))
                    if((self.plist[i].pos[1])-2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"b3"),self.plist[i]))

                    # take
                    
                    if((self.plist[i].pos[1])-3>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and
                           (self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]!="  " or
                            self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]!="b2" or
                            self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]!="b3" or
                            self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]])))
                    if((self.plist[i].pos[1])+3<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tv") and
                           (self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]!="  " or
                            self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]!="b2" or
                            self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]!="b3" or
                            self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]])))
                    if((self.plist[i].pos[0])-3>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]!="  " or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]!="b2" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]!="b3" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]),self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3])))
                    if((self.plist[i].pos[0])+3<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]!="  " or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]!="b2" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]!="b3" or
                            self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]),self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3])))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="b2" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="b3" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1])))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="b2" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="b3" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1])))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="b2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="b3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2])))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="b2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="b3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2])))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="b2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="b3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2])))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="b2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="b3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2])))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="b2" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="b3" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1])))
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="b2" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="b3" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1])))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="b2" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="b3" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1])))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="b2" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="b3" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1])))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="b2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="b3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2])))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="b2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="b3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2])))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]!="  " or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]!="b2" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]!="b3" or
                            self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2])))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]!="  " or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]!="b2" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]!="b3" or
                            self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]+1),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]+1),self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2])))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="  " or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="b2" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="b3" or
                            self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1])))
                    if((self.plist[i].pos[1])-2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="  " or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="b2" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="b3" or
                            self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]!="b4")):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"b3"),self.plist[i],
                                          "take", Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1])))
                if(self.plist[i].type[1]=="4"):
                     if((self.plist[i].pos[1])-3>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])-3>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-3),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])+3<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"b4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+3),"b4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]+1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"b4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-2>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-2),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+2),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])+2<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])-2>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]-1),"b4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]+2<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+2,self.plist[i].pos[1]-1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]-2>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-2,self.plist[i].pos[1]+1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+2<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+2),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])-2<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-2),"b4"),self.plist[i]))
                
                    if((self.plist[i].pos[1])-4>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]-4][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-4),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+4<9):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="tv") and 
                           self.state[self.plist[i].pos[1]+4][self.plist[i].pos[0]]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+4),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])-4>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-4]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]-4),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])+4<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="th") and 
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+4]=="  "):
                            moves.append((Piece((self.plist[i].pos[0],self.plist[i].pos[1]+4),"b4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-3>-1 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-3),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="th") and 
                           (self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+3),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])-3>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]-1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])+3<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="tt") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]+1),"b4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]-3>-1):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="lu" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-2]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]-1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]+3<7):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="ld" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="th") and
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="or" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+2]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]+1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ll" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+3),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])-3>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="lr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-3),"b4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-3>-1 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]-3),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]]=="tv") and 
                           (self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]]=="tt") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]+3),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])+3<7 and (self.plist[i].pos[1])+1<9):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="or" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+3]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]-1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[0])-3>-1 and (self.plist[i].pos[1])-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-2]=="th") and 
                           (self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-3]=="tt") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]-1),"b4"),self.plist[i]))
                    
                    if((self.plist[i].pos[1])-1>-1 and self.plist[i].pos[0]+3<7):
                        if((self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="ru" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="or" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+1]=="th") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="or" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+2]=="th") and 
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]+3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+3,self.plist[i].pos[1]-1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+1<9 and self.plist[i].pos[0]-3>-1):
                        if((self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="rd" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="ol" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-1]=="th") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]=="ol" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-2]=="th") and 
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]-3]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-3,self.plist[i].pos[1]+1),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])+3<9 and self.plist[i].pos[0]+1<7):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="rr" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]+1]=="tt") and 
                           (self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]+1][self.plist[i].pos[0]+1]=="tv") and 
                           (self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="  " or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="od" or
                           self.state[self.plist[i].pos[1]+2][self.plist[i].pos[0]+1]=="tv") and 
                           self.state[self.plist[i].pos[1]+3][self.plist[i].pos[0]+1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]+1,self.plist[i].pos[1]+3),"b4"),self.plist[i]))
                    if((self.plist[i].pos[1])-3<9 and self.plist[i].pos[0]-1>-1):
                        if((self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="rl" or
                           self.state[self.plist[i].pos[1]][self.plist[i].pos[0]-1]=="tt") and 
                           (self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]-1][self.plist[i].pos[0]-1]=="tv") and 
                           (self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="  " or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="ou" or
                           self.state[self.plist[i].pos[1]-2][self.plist[i].pos[0]-1]=="tv") and 
                           self.state[self.plist[i].pos[1]-3][self.plist[i].pos[0]-1]=="  "):
                            moves.append((Piece((self.plist[i].pos[0]-1,self.plist[i].pos[1]-3),"b4"),self.plist[i]))
        
        return (moves)
