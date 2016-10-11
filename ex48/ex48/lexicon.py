
verb = ('go', 'stop', 'kill', 'eat')
noun = ('door', 'bear', 'princess', 'cabinet')
dire = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')

stuff = raw_input('input string or sth with space:')

def scan(stuff):
    res = []
    words = stuff.split()
    for word in words:
        if word in verb:
            tmp = ('verb', '%r' % word)
        elif word in noun:
            tmp = ('noun', '%r' % word)
        elif word in dire:
            tmp = ('direction', '%r' % word)
        elif typeof(word) == int:
            tmp = ('num', '%r' % word)
        else:
            tmp = ('error', '%r' % word)

        res.append(tmp)

    return res
