from random import randint

player = input('rock(r),paper(p),scissors?(s)   ')

print(player, 'vs' )

chosen = randint(1,3)

if chosen == 1:
    
    pc = 'r'
    
elif chosen == 2:
    
    pc = 's'
    
else:
    
    pc = 'p'

print(pc)

if player == pc:
    print('Draw')
    
elif player =='r' and pc == 's':
    print('Player wins')
    
elif player =='r' and pc == 'p':
   print('Player wins')
   
elif player =='p' and pc == 's':
    print('Player wins')
    
elif player =='p' and pc == 'r':
   print('Player wins')

elif player =='s' and pc == 'r':
    print('Player wins')
    
elif player =='s' and pc == 'p':
   print('Player wins')

