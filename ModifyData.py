def __OptimizeDayData(data):
    for i in range(len(data)):
        day=''
        for j in data[i]:
            x=ord(j)
            if x>1775 and x<1786:
                day+=str(x-1776)
            elif day!='':
                break
            if len(day)>=2:
                break
        data[i]=day
    return data


def OptimizeDayData(data):
    dayData=__OptimizeDayData(list(map(lambda x:x['day'],data)))
    x=0
    for i in range(len(data)):
        data[i]['day']=dayData[i]
    return data
