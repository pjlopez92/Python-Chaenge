import os
import csv

Elections=os.path.join('election_data.csv')

with open(Elections) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        votes=[]
        percent_of_votes=[]
        rownum = 0
        for row in csv_reader:
                votes.append(row[2])
        
candids = [[i, votes.count(i)] for i in set(votes)]
names, votes_per_candid = map(list, zip(*candids))               
total_votes= str(len(votes))

for num in votes_per_candid:
        percent_of_votes.append((num*100)/int(len(votes)))
x=votes_per_candid.index(max(votes_per_candid))
winner=names[x]

def submit():
    f=open('Elections.txt','w+')
    f.write('Election Results: \n')
    f.write('Total Votes: ' + total_votes + '\n')
    y=0
    for i in names:
        f.write(i + ': '+ str(percent_of_votes[y]) + '% ('+ str(votes_per_candid[y]) + ') \n')
        y +=1
    f.write('The winner is: ' + winner + '\n')
    f.close()

print('Election Results: ')
print('Total Votes: ' + total_votes)
y=0
for i in names:
        print (i + ': '+ str(percent_of_votes[y]) + '% ('+ str(votes_per_candid[y]) + ') ')
        y +=1
print('The winner is: ' + winner)
submit()