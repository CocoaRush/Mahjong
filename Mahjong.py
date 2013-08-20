# -*- coding: utf-8 -*-
import random

HU_CHOW_INDEX = [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24]
THIRTEEN_1 = [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]

def checkTing(tileInHand):
    numTile = 0
    count = len(tileInHand)
    for i in range(count):
        numTile += tileInHand[i]
    if numTile != 13:
        print 'please input a valid number of tile to test, should be 13 received {0}'.format(numTile)
        exit(0)
    
    for tile in range(count): #try each tile
        if tileInHand[tile] > 3:
            print 'already have 4 of this tile, no chance to get one more.'
            continue
        # print 'try{0}this time'.format(prettyTile(tile))
        checkHu(tileInHand, tile)


def checkHu(tileInHand, tile):
    # print 'new tile in hand: ', prettyTileInHand(tileInHandNew)
    # try every possibility of each possible eye
    eye = -1
    count = len(tileInHand)
    # print tileInHandNew
    for i in range(count):
        tileInHandNew = newTileInHand(tileInHand, tile)
        
        if thirteen1(tileInHandNew):
            congratulation(tile)
            return
        
        # tileInHandNew = newTileInHand(tileInHand, tile)
        if pair7(tileInHandNew):
            congratulation(tile)
            return
        
        #look for eye, which is any pair of tile. Does not restrict to 2, 5 and 8 from Wan, Bing or Tiao
        #this is the key to find different kinds of winning state
        # tileInHandNew = newTileInHand(tileInHand, tile)
        if tileInHandNew[i] < 2: 
            # print 'could not find an eye, eye is a must to win.'
            continue
        else:
            eye = i
            # print 'eye of your tile: a pair of{0}'.format(prettyTile(eye))
            # print 'the rest of tile in hand: ', prettyTileInHand(tileInHandNew)
            if hu(tileInHandNew, eye):
                congratulation(tile)


def congratulation(tile):
    print 'Good point, you are on win state and the tile missing is: {0}\n'.format(prettyTile(tile))
    # print 'the tile in your hand: {0}\n'.format(prettyTileInHand(tileInHand))
    pass


def thirteen1(tileInHand): #check 13 1
    '''
    13 1: 1W 9W 1B 9B 1T 9T East South West North White Green Red and one more any of them
    '''
    findeye = False
    for tile in THIRTEEN_1:
        if findeye:
            if tileInHand[tile] != 1:
                return False
        else:
            if tileInHand[tile] == 2:
                findeye = True
                continue
            if tileInHand[tile] != 1:
                return False
    return findeye


def pair7(tileInHand): #check 7 pairs
    pairCount = 7
    pairContent = [0 for i in range(pairCount)]
    for tile in range(len(tileInHand)):
        if tileInHand[tile] == 0:
            continue
        elif tileInHand[tile]==2:
            pairContent[pairCount-1] = tile
            pairCount -= 1
        else:
            return False
    '''
    while pairCount > 0:
        pair = getPair(tileInHand)
        if pair >= 0:
            tileInHand[pair] -= 2
            pairContent[pairCount-1] = pair
            pairCount -= 1
        else:
            break
    '''
    if pairCount == 0: #succeed in findng 7 pairs
        for i in range(7):
            print 'pair: {0}'.format(prettyTile(pairContent[i]))
        return True


def hu(tileInHand, eye): #check 1 eys with 4 combinations
    tileInHand[eye] -= 2
    comCount = 0
    comContent = [0 for i in range(12)]
    #check possible pong at most 4 times
    count = 4
    while count > 0:
        pong = getPong(tileInHand)
        if pong >= 0:
            for i in range(3): #update combination
                comContent[3*comCount+i] = pong
            comCount += 1
            tileInHand[pong] -= 3
            count -= 1
            # print 'find a pong in your tile: pong of{0}'.format(prettyTile(pong))
            # print 'the rest of tile in hand: ', prettyTileInHand(tileInHandNew)
        else:
            break #count = 0
    
    for i in range(4-comCount): #the rest possible combination
        chow = getChow(tileInHand)
        if chow >= 0:
            for i in range(3):
                comContent[3*comCount+i] = chow+i
            comCount += 1
            tileInHand[chow] -= 1
            tileInHand[chow+1] -= 1
            tileInHand[chow+2] -= 1
            # print 'find a chow in your tile: chow of{0} {1} {2}'.format(prettyTile(chow), prettyTile(chow+1), prettyTile(chow+2))
            # print 'the rest of tile in hand: ', prettyTileInHand(tileInHandNew)
    
    if comCount == 4:
        for i in range(4):
            print 'combination: {0}{1}{2}'.format(prettyTile(comContent[3*i]), prettyTile(comContent[3*i+1]), prettyTile(comContent[3*i+2]))
        print 'eye: {0}'.format(prettyTile(eye))
        return True
    return False


def newTileInHand(tileInHand, tile):
    tileInHandNew = [tileInHand[i] for i in range(len(tileInHand))]
    tileInHandNew[tile] += 1

    return tileInHandNew


def getPair(tileInHand):
    for tile in range(len(tileInHand)):
        if tileInHand[tile] >= 2:
            return tile
    return -1


def getChow(tileInHand):
    '''
    check from 0-6, 9-15, 18-24
    '''
    for tile in HU_CHOW_INDEX:
        if tileInHand[tile]>0 and tileInHand[tile+1]>0 and tileInHand[tile+2]>0:
            return tile
    return -1


def getPong(tileInHand):
    for tile in range(len(tileInHand)):
        if tileInHand[tile] >= 3:
            return tile
    return -1


def deal(length=13):
    '''
    the default number of tiles is 13
    random generation of 13 tiles
    34 different kinds, one tile each time for 13 times
    0-8:    1 ~ 9 Wan
    9-17:   1 ~ 9 Bing
    18-26:  1 ~ 9 Tiao
    27:     East
    28:     South
    29:     West
    30:     North
    31:     White
    32:     Green (fa)
    33:     Red (zhong)
    '''
    tileInHand = [0 for i in range(34)]
    numTile = 0
    while numTile < length:
        tile = random.randint(0, 26) #33/26, try 26 instead of 26 if you want to get rid of those special tiles
        if tileInHand[tile] < 4:
            tileInHand[tile] += 1
            numTile += 1
    
    return tileInHand


def prettyTileInHand(tileInHand): #pretty print
    tile = 0
    prettytile = ''
    while tile < len(tileInHand):
        count = tileInHand[tile]
        while count > 0:
            prettytile += prettyTile(tile)
            count -= 1
        tile += 1
    if prettytile == '':
        print 'do not have any tile in your hand, probably wrong input or you are ready to win'
    return prettytile


def prettyTile(tile):
    if tile>=0 and tile <=8:
        return ' {0}W '.format(tile+1)
    elif tile>=9 and tile <=17:
        return ' {0}B '.format(tile-9+1)
    elif tile>=18 and tile <=26:
        return ' {0}T '.format(tile-18+1)
    
    if tile ==  27:
        return ' Eest '
    if tile ==  28:
        return ' South '
    if tile ==  29:
        return ' West '
    if tile ==  30:
        return ' North '
    if tile ==  31:
        return ' While '
    if tile ==  32:
        return ' Green '
    if tile ==  33:
        return ' Red '
    return ' not a valid tile! '


def main():
    # tileInHand = deal()
    # tileInHand = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # tileInHand = [1, 1, 1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
    tileInHand = [3, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #dragon like tile in hand
    # tileInHand = [0, 2, 2, 0, 0, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0] #7 pair
    # tileInHand = [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1] #13 1
    print 'tile in hand: ', prettyTileInHand(tileInHand)
    checkTing(tileInHand)
    pass


if __name__ == '__main__':
    main()

