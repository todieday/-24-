f = open('loh.txt')
n = f.readline()
km = n.count('M') #считаем кол-во М в строке
ke = n.count('E') #считаем кол-во Е в строке 
if km > ke: #сравниваем эти значения
    print('M', km)
else:
    print('E', ke)
f.close()
