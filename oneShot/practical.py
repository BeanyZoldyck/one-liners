def sortDict(dic):
    '''sorts dictionary by values {'b':2,'a':1,'d':4,'c':3}->{'a':1,'b':2','c':3,d':4}'''
    return {{j:i for i, j in dic.items()}[i]:i for i in sorted(dic.values())}
