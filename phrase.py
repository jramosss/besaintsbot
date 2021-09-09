from db.db import phrases as phrases
from datetime import datetime

def getDateStr ():
    today = datetime.today().date()
    month = today.month
    day = today.day
    strmonth = str(month)
    strday = str(day)
    if month < 10:
        strmonth = '0' + strmonth
    if day < 10:
        strday = '0' + strday

    return strmonth + '-' + strday
        

def getPhrase ():
    date = getDateStr()
    for p in phrases:
        if p["date"] == date:
            return p["text"] + ' ' + p["author"] + '.'