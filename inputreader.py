def readGoal(text):
    return text.strip('\n').split(',')


def readknowledge(text):

    return text.strip('\n').split(',')


def readRules(text):

    R = text.split('\n')
    R = [(elem.split('=>')[0].split('+'), elem.split('=>')[1]) for elem in R]

    return R


def inputreader(c=True, file='file'):

    with open(file+'.txt') as f:
        inputdata = f.read()
        data = inputdata.split('\n\n')

        if c:
            return data[0], data[1]
        else:
            return data[0], data[1], data[2]
