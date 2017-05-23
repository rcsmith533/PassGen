import random

noun = ('cat','dog','elephant','monkey','zebra')
adjectives = ('sticky','dumb','orange','red','yellow','small','large')

def genPass():
    # n is lenth of desired password
    ranNoun = noun[random.randint(0,len(noun)-1)]
    ranAdj = adjectives[random.randint(0,len(adjectives)-1)]
    password = ranAdj + ranNoun.capitalize()
    return password

# def add(l):
    
for i in range(5):
    print(genPass())
