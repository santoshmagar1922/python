# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hello santosh")

print('hello santosh')

x=5
y=1.5
z="hello from python"

# I am single line comment 

'''
i am inside multiple commnent
i am again inside multiple commnent

'''



'''
list
- Collection of elements.
- support different type of element
- support repeatation of elements
- List are mutuble
- can be defined using [] brackets

'''

x = [12,12, 23.6, "santosh", 's',12, 34, 56,"hi"]
type(x)

len(x)

x[0]
x[5]

x[-1]
x[-2]
x[-3]

# slicing of the list

x[3:5]
x[1:8]
x[0:3]

# customization

print(x[0])

x[0]=13

print(x[0])


x.insert(2, 2324)
print(x)


# removes element by taking element
x.remove(13)
print(x)


# removes element by index and return element
x.pop(3)

print(x)

x.append("adding")

print(x)

####################

x2=[1,2,3]

x+x2

x2*5

#############################

'''
tuple:
- collection of values
- allows elements of different types
- supports repeatation of elements
- can be defined using () brackets
- immutable

'''


y=(1,2,3,4,5, "hi", "hello")

type(y)

len(y)

y[0]
y[-1]

y[3:5]

y[0:1]

# cant do this as its immutable
y[0] = 123

y


k="hello from python"

k[0]

k[0:6]


################

'''
Dictionary :
- collection of key-values
- Defined using {} brackets
- does not support repeatation
- its mutable     
    

'''


w={"name":"santosh", "salary":23000, "city":"Pune", "name":"sant"}

w["name"]
w["salary"]

print(w)

w["salary"] = 80000


w.pop("city")

print(w)


#####################################

'''
Set :
- can be defined using {} brackets
- do not support repetation and its unordered
- used for set theory like union/ intersection


'''


d={4,5,6,1,2,30}

h={1,2,3,4,5,6,1,2,40,40}

print(h)


d.union(h)

d.intersection(h)


############################


data="I love my india"


data= data.split()

" ".join(data)

###############################

a= input("enter first number:")
b= input("enter second number:")
c=int(a)+int(b)

print(c)


################################

'''
BMI calculator:
    
    w = weight in kg
    h = height in cm
    
Formula => BMI = w/(h*h) where height in meters

'''

w= input("enter weight in Kg :")
h= input("enter height in cm :")

h=int(h)/100
bmi= int(w)/(h*h) 

print(bmi)



####################################

for i in range(5):
    print("hello")
    
    
    
for i in range(5):
    print("hello",i)
    
for i in range(3,12):
    print("hello python is awesome", i)    

for i in range(3,12,2):
    print("hello python is awesome", i)    

for i in range(12,3,-1):
    print("hello python is awesome", i)    
    
    
    
    
temp=[23,24,23,25,26,23,12,13]    
for i in temp:
    if i>23:
        print(i)
        
        
#List comprehension
        
x = [i for i in temp if i > 23]        
print(x)        

##########

#List words greater than 7 character 

data="Pune is a sprawling city in the western Indian state of Maharashtra. It was once the base of the Peshwas (prime ministers) of the Maratha Empire, which lasted from 1674 to 1818. It's known for the grand Aga Khan Palace, built in 1892 and now a memorial to Mahatma Gandhi, whose ashes are preserved in the garden. The 8th-century Pataleshwar Cave Temple is dedicated to the Hindu god Shiva."
print(data)

data = data.split()

x = [i for i in data if len(i) >= 7] 

print(x)

########

x = 5
while x<50:
    print("Python is easy")
    x+=2
    

####################

# Number Guessing game

answer = 5

while True:
    guess = int(input("Guess Num: "))
    if guess==answer:
        print("you won")
        break
    else:
        print("Try again")
        
        


#########################

print(help(list))


x=[2,5,3,7]
sorted(x)            
    
y=["i","India","My", "Love"]
sorted(y)            
    
sorted(y, key=len)            
    
    
###########################


def myFun():
    print("hello")
    return None    
    
    
myFun()



def myFun2(a,b):
    print("hello")
    c=a+b
    return c    
    
    
myFun2(2,5)


# Default second parameters

def myFun3(a,b=5):
    '''
    This is my function with default params
    
    '''
    print("hello")
    c=a+b
    return c    
    
    
myFun3(10)
myFun3(10,20)


print(help(myFun3))
print(myFun3.__doc__)


######################

y = lambda x:x+5

y(4)


#######################


data=[2,5,6,7,8,5,4,6]

def myFun4(x):
    y=x+4
    y=y/2
    return y


data2 = [myFun4(i) for i in data]
data3 = list(map(myFun4, data))


data4= map(lambda x:(x+4)/2, data)
data4= list(data4)


#################################

'''

this applies to field / method (starts with)

default public

_ protected

__ private

'''



class A:
    x=5
    __y=12
    _p=5
    
    def myFun(self):
        print("I am method of A")


class B(A):
    d=45
    
    def myFun2(self):
        print("I am method of B")
        print(self._p)
        print(self.__y)




###################################

import Code2

Code2.x
Code2.myFun()

Code2.myFun2(3,4)

w= Code2.A()
w.p
w.q
w.myFun3()


#OR alias

import Code2 as cd

cd.x
cd.myFun()


###############################

'''

scipy = scientific computation, statistical anaysis
numpy = mathematical computation


pandas = Data import/ export, Data cleaning, Data manipulation, Data Analysis, 
Data visualaization, basic statistical Analysis



matplotlib, seaborn = data visualizaiton

scikit-learn (sklearn) = supervised and Unsupervised ML algo implementations feature enginering,
 selection

trnsorflow, pytorch = Advance ML and DL, they support GPU computing

keras = Deep Learning

scikit-image (skimage),  PIL = Image processing
openCV = very powerful computer vision package

NLTK, gensim, spaCy  = NLP

###########

Flask, Djnago = Web app
tkinter, pyqt = Desktop App develpoment
pyspark = apache spark integration for big fata handling


'''


































