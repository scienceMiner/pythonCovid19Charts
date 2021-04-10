'''
Created on 1 Apr 2020

@author: ethancollopy
'''
def add(a,b):
    return a+b

def addFixedValue(a):
    y = 5
    return y + a

s = 'The value of x is ' + repr(add(4,5))
    
  
i = 1
for i in range(1, 10):
    if i <= 5 :
        print ('Smaller or equal than 5.\n')
    else:
        print ('Larger than 5.\n')
        
        
print(s)
      
print (addFixedValue(1))

