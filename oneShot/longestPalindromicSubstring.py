s=input("word: ");t = (lambda x: x[list(map(lambda r: len(r),x)).index(max(list(map(lambda r: len(r),x))))])([[s[i[0]:i[0]+l] for l in range(len(s)-i[0]+1) if (l and not any([s[i[0]:i[0]+l][j]!=s[i[0]:i[0]+l][-1-j] for j in range(len(s[i[0]:i[0]+l])//2)]))][-1] for i in enumerate(s)])
print(t)
