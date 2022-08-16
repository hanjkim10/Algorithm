alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in alp:
    word = word.replace(i, 'a')
print(len(word))