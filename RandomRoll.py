import random

def RollDie():
    modifier = input("is there a modifier?  ")
    roll = random.randint(1,20)
    print "you rolled a %r" %roll
    added = roll + modifier
    print "with your mod your result is %r " %added
    return added
result = RollDie()

textresult= {
    -4:'this is a -4',
    -3:'this is a -3',
    -2:'this is a -2',
    -1:'this is a -1',
    0:'this is a 0',
    1:'this is a 1',
    2:'this is a 2',
    3:'this is a 3',
    4:'this is a 4',
    5:'this is a 5',
    6:'this is a 6',
    7:'this is a 7',
    8:'this is a 8',
    9:'this is a 9',
    10:'this is a 10',
    11:'this is a 11',
    12:'this is a 12',
    13:'this is a 13',
    14:'this is a 14',
    15:'this is a 15',
    16:'this is a 16',
    17:'this is a 17',
    18:'this is a 18',
    19:'this is a 19',
    20:'this is a 20',
    21:'this is a 21',
    22:'this is a 22',
    23:'this is a 23',
    24:'this is a 24'
}

print textresult[result]