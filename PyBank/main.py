import os
import csv

from datetime import datetime
Budget_csv=os.path.join('budget_data.csv')

with open(Budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    Header=next(csv_reader)
    datelist=[]
    amount=[]
    increase=[]
    rownum=0
    for row in csv_reader:
        datelist.append(row[0])
        amount.append(int(row[1]))
        rownum+=1
        if rownum>=2:
            x=(amount[-1])-(amount[-2])
            increase.append(x)

def submit():
    f=open('Analysis.txt','w+')
    f.write('Financial Analysis: \n')
    f.write('The total of months is: ' + result + '\n')
    f.write('The total amount is: '  + total_amount + '\n')
    f.write('The average change is: '  + changes_average + '\n')
    f.write('The Greates increase was: ' + str(max(increase)) + ' in ' + datelist[datemax] + '\n')        
    f.write('The Greates increase was: ' + str(min(increase)) + ' in ' + datelist[datemin] + '\n')
    f.close()
    

datelist2 = list(dict.fromkeys(datelist)) 
result=str(len(datelist2))
total_amount=str(sum(amount))
changes=(amount[-1])-(amount[0])
num_of_changes=(len(amount)-1)                
changes_average=str(float(changes/num_of_changes))
datemax=increase.index(max(increase)) + 1
datemin=increase.index(min(increase))+1
print('Financial Analysis:')
print('The total of months is: ' + result)
print('The total amount is: ' + total_amount)
print('The average change is: ' + changes_average)
print('The Greates increase was: ' + str(max(increase)) + ' in ' + datelist[datemax])        
print('The Greates increase was: ' + str(min(increase)) + ' in ' + datelist[datemin])
submit()






