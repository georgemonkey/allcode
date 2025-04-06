import csv
import datetime
import time

def fun1(named):
    
    with open('test.csv','a',newline='' ) as f:
        thewriter=csv.writer(f)
        datetime_object = datetime.datetime.now()
        thewriter.writerow([named,datetime_object])
        

        

"""
if named in open('test.csv','a',newline='').read():
            thewriter.writerow([named])
        else:
            print("False")
    csv_file=csv.reader(open ('test.csv','r'))

    for row in csv_file:
        if named==row[0]:
            x=0
        else:    
            with open('test.csv','w',newline='' ) as f:
                thewriter=csv.writer(f)
                thewriter.writerow([named])
"""
    

