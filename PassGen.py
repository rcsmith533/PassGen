import random

noun = ['cat','dog','elephant','monkey','zebra']
adjectives = ['sticky','dumb','orange','red','yellow','small','large']

def genPass():
    # n is lenth of desired password
    ranNoun = noun[random.randint(0,len(noun)-1)]
    num = random.randint(0,999)
    ranAdj = adjectives[random.randint(0,len(adjectives)-1)]
    password = ranAdj + ranNoun.capitalize() + str(num)
    return password

def menu():
    print('1) Generate a password\n2) Add a noun\n3) Add an adjective')
    
def addNoun(l):
    if l in noun:
        print(l, 'is already in the list of nouns')
    else:
        noun.append(l)

def addAdj(l):
    if l in adjectives:
        print(l, 'is already in the list of adjectives')
    else:
        adjectives.append(l)

menu()
addNoun('cat')
addAdj('dumb')
