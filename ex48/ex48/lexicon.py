import re

verb = ('go', 'stop', 'kill', 'eat')
noun = ('door', 'bear', 'princess', 'cabinet')
stop = ('the', 'in', 'of', 'from', 'at', 'it')
dire = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')

# stuff = raw_input('input string or sth with space:')

def scan(stuff):
    res = []
    words = stuff.split()
    for word in words:
        tmp = []
        if word in verb:
            tmp = ('verb', '%s' % word)
        elif word in noun:
            tmp = ('noun', '%s' % word)
        elif word in dire:
            tmp = ('direction', '%s' % word)
        elif word.isdigit():
            word = int(word)
            tmp = ('number', '%d' % word)
        elif word in stop:
            tmp = ('stop', '%s' % word)
        else:
            tmp = ('error', '%s' % word)

        res.append(tmp)

    return res

test1 = scan("go north 23  344569 the")
for test in test1:
    print test