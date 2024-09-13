from datetime import datetime, time

def subtrSec(dateBigger,dateLess):
    
    subtr = dateBigger - dateLess
    subtrSec = (subtr.days*24*3600)+(subtr.seconds)
    
    return subtrSec
    
    
date1 = datetime.now()
date2 = datetime(2023,8,4)

subtr=subtrSec(date1,date2)

#print(subtr)
