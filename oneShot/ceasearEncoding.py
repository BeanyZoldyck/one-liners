possChars='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~';offset=int(input("Offset: "));method=input("E to encode, D to decode: ").upper();print(''.join([(possChars)[[(possChars).index(i),([t for t,n in enumerate(possChars) if n == i][1])][method!='E']+((3**(method=='E')*offset)-2*offset)] for i in input("Text to operate:\n")]))
#doesn't work with spaces because of this short story:
story = '''In my intro to Python class I took, I had been coding in python for over 4 years,
so I challenged myself to do the assignments in ~1 line, but when I submitted the version that worked with spaces,
it didn't "meet qualifications" (wanted abc->xyz, would give abc->yzA or something, still worked with spaces though)
pretty stupid so I had ot change it to get full pooints'''
