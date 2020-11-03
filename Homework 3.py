#!/usr/bin/env python
# coding: utf-8

# In[1]:


#3-25 6.
num1,num2,num3,num4,num5=eval(input('Enter five numbers separated by commas:'))

sum=num1+num2+num3+num4+num5
Average=sum/5

print('sum,avaerage')


# In[4]:


print(sum,Average)


# In[5]:


#4-14 1 
a=-888
b=100
c=10
d=2
e=0.5
print(abs(a))
print(max(a,b,c,d,e))
print(min(a,b,c,d,e))
print(pow(c,d))
print(round(7.5))
print(round(6.5))
print(int(123.456))
print(round(123.456,2))


# In[7]:


#2
import math
a=math.fabs(-123.45)
print(a)

b=math.ceil(8.8)
print(b)

c=math.floor(8.8)
print(c)

d=math.exp(1)
print(d)


# In[3]:


#4-15 3.
m=math.tan(0)
print(m)

n=math.tan(2*math.pi)
print(n)

q=math.radians(360)
print(q)


# In[4]:


#4-16 4.
x='Apple i'+str(8)
print(x)

y=ord('Z')
print(y)

z=chr(100)
print(z)


# In[ ]:


#5-36 1 (a)
score=eval(input('Enter you score'))
if score>=60:
    score+=10
print('You score is %d(score)')


# In[ ]:





# In[ ]:




