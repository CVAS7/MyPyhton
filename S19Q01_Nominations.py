[suresh@localhost Practice]$ cat S19Q01_Nominations.py
""""

S19Q01
Write a Python program that takes a file name as its argument. 
This file [ nominations.txt ] contains the nominations for a sports event.
- What are the games that have nominations ?
- Print the list of players playing each game 
     in the ascending order of their names.
- Print the list of players who are playing more than one game.
- Print the list of players who are playing only one game.

"""
FH = open('nominations.txt','r')
all_lines = FH.readlines()
#print all_lines
nom,store= {},{}
lgames,lnames,cri,foot,bas,onegame,moregame = [],[],[],[],[],[],[]
def countoccurrences(store, value):
    try:
        store[value] = store[value] + 1
    except KeyError as e:
        store[value] = 1
    return
for i in all_lines:
    line = i.split('-')
#    print line[0],line[1].strip()
    nom[line[0]] = line[1].strip()
    if line[1].strip() == 'Cricket':
        cri.append(line[0].strip())
    if line[1].strip() == 'Football':
        foot.append(line[0].strip())
    if line[1].strip() == 'Basketball':
        bas.append(line[0].strip())
    lnames.append(line[0].strip())
    lgames.append(line[1].strip())
sgames = set(lgames)
snames = set(lnames)
#print nom
#print 'Players playing Cricket:',sorted(cri)
#print 'Players playing Football:',sorted(foot)
#print 'Players playing Basketball:',sorted(bas)
#print lnames
#print lgames
#print snames
#print sgames
print 'Games that have nominations are below' 
print 'SerialNumber, Games Nominated'
lsgames = list(sgames)
for i in xrange(0,len(lsgames)):
    print i+1,' '*(len('SerialNumber,')-4),',',lsgames[i]
print 'List of players playing each game in ascending order'
print 'Names:'
for i in sorted(list(snames)):
    print i
for data in lnames:
    countoccurrences(store, data)
for k, v in store.iteritems():
    if v > 1:
        moregame.append(k)
    else:
        onegame.append(k)
print 'Players playing Cricket:',sorted(cri)
print 'Players playing Football:',sorted(foot)
print 'Players playing Basketball:',sorted(bas)
print "Player playing more than one Game:"
for i in moregame:
    print i
print "Player playing one Game:"
for i in onegame:
    print i
