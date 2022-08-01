f = open('loh.txt')
n = f.readline()
km = 0 #счетчик для Моргенштерна 
ke = 0 #счетчик для Егора Крида
for i in range(len(n)): 
    if n[i] == 'M':
        km += 1
    elif n[i] == 'E':
        ke += 1 
if km > ke: #сравниваем значения счётчиков
    print('M', km)
else:
    print('E', ke)
f.close()



        
        
