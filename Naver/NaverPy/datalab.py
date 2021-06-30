from datetime import datetime, timedelta


age_range = [0 , 
    list(range(13)), list(range(13, 19)), list(range(19,25)),
    list(range(25, 30)), list(range(30, 35)), list(range(35, 40)), 
    list(range(40, 45)), list(range(45, 50)), list(range(50, 55)),
    list(range(55, 60)), list(range(60, 150))
]

def to_timedelta(s : str) :
    tmp = 0
    day = 0
    month = 0
    year = 0
    for c in s :
        if c.isdigit() :
            tmp = tmp * 10 + int(c)
        if c == 'd' :
            day += int(tmp)
            tmp = 0
        if c == 'm' :
            month += int(tmp)
            tmp = 0
        if c == 'y' :
            year += int(tmp)
            tmp = 0
    return timedelta(day+(year*12+month)*30)

class DLTrendparam(dict) :
    '''
        For Datalab Trend Search Parameter
    '''
    def __init__(self) :
        now_date = datetime.now()
        self['startDate'] = (now_date - timedelta(days=1)).strftime('%Y-%m-%d')
        self['endDate'] = now_date.strftime('%Y-%m-%d')
        self['timeUnit'] = 'date'
        self['keywordGroups'] = []

    def AddKeywordGroup(self, title, keywords) :
        new_group = {
            'groupName' : title,
            'keywords' : keywords
        }
        temp = self['keywordGroups']
        temp.append(new_group)
        self['keywordGroups'] = temp
    def SetPeriodPrev(self, fromDT : datetime, period) :
        self['startDate'] = (fromDT - to_timedelta(period)).strftime('%Y-%m-%d')
        self['endDate'] = fromDT.strftime('%Y-%m-%d')
    
    def SetPeriodNext(self, fromDT, period) :
        self['startDate'] = fromDT.strftime('%Y-%m-%d')
        self['endDate'] = (fromDT + to_timedelta(period)).strftime('%Y-%m-%d')
    
    def SetAgeRange(self, agefrom, ageto) :
        for i in range(1, 12) :
            if agefrom in age_range[i] :
                agefrom = i
                break
        for i in range(i, 12) :
            if ageto in age_range[i] :
                ageto = i
                break
        self['ages'] = list(map(lambda x: str(x), range(agefrom, ageto + 1)))
        
    def SetDevice(self, device) :
        self['device'] = device
    def SetGender(self, gender) :
        self['gender'] = gender