import pandas as pd
import numpy as np
flag = True
lis =[]

while(flag):
    
    start = int(input('What is the initial price of the stock : '))
    inpt  = int(input('How many days would you like to simulate : '))
    ini = int(start)
    listo = []
    
    for i in range(inpt):
        start = start +(start * np.random.uniform(0.2,-0.2))
        listo.append(start)
 
    
    increment = 0
    decrement = 0
    same = 0

    for x, y in zip(listo[0::], listo[1::]):
    
        if x == y:
            same += 1
        elif x < y:
            increment += 1
        elif x > y:
            decrement += 1    

    print('After ' , inpt, 'days', listo[-1], 'is the new stock price.')
    print('The stock price increased',increment, 'time(s), decreased ', decrement ,' time(s), and \n stayed the same', same,' time(s).')
    
    
    
    tpl = (ini,inpt,listo[-1])
    lis.append(tpl)
    
    choice = str(input('Would you like to perform another simulation (yes/no)?'))
    
    if choice == 'yes':
        flag = True
    elif choice == 'no':
        flag = False
    else:
        print('wrong choice')

        
df = pd.DataFrame(lis, columns = ['Initial price' ,'Number of days simulated', 'Final price'])
df.to_csv('stocks.csv')