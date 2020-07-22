#!/usr/bin/env python
# coding: utf-8

# In[17]:


#ASSINGMENT NO. 3
#QUESTION NO. 1
# Calculate the sum of n number with help of while loop 

sum1 = 0

a = 1

while a <= 10:
    sum1 = sum1 + a
    a = a + 1
    
    print(sum1)
    


# In[20]:


#QUASTION NO.2
# Take a integer and find it is prime or not 
num1 = int(input("Enter your number"))
if num1>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is not a prime number")
else:
    print(num,"is not a prime number")


# In[ ]:




