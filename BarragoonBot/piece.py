### piece ###

#
# w2
# w3
# w4
#
# b2
# b3
# b4
#
# xx no way
# or one way right
# ol one way left
# od one way down
# ou one way up
#
# th two way horizontal
# tv two way vertical
#
# rr right turn right
# rl right turn left
# ru right turn up
# rd right turn down
#
# lr left turn right
# ll left turn left
# lu left turn up
# ld left turn down
#
# tt all turns
#

class Piece:

    def __init__(self,pos,typ):
        self.pos=pos
        self.type=typ
