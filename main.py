from inputreader import inputreader, readGoal, readRules, readknowledge
from chainage_avant import chainageAvant
from chainage_ariere import chainageAriere

f = input('file name(without the extension): ')

while input('play: ').lower() == 'yes':

    if input('quel type de chainage(Av/Ar): ') == 'Av':
        K, R = inputreader(file=f)
        K, R = readknowledge(K), readRules(R)
        print(chainageAvant(R, K))
    else:
        K, R, G = inputreader(c=False, file=f)
        K, R, G = readknowledge(K), readRules(R), readGoal(G)
        print(chainageAriere(G, K, R))

print('goodbye!')
