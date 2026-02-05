#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


#methods for searching and sorting of lists 

numbers = [10, 11, 13, 7, 1, 2, 3, 4, 5, 6, 8]

if 4 in numbers:
    print("found")
    
    



# In[5]:


numbers = [10, 11, 13, 7, 1, 2, 3, 4, 5, 6, 8]

numbers.sort()


# In[6]:


numbers


# In[7]:


#time complexity of the algorithm
#space complexity of the algorithm


pairs = [(2, 'b'), (1, 'a'), (2, 'c')]

pairs.sort() #pass the methods


# In[8]:


pairs


# In[9]:


#functions 


#custom functions 
#problem - solution for problem - solution is the defination - def is the function 


def greeting():
    print("hello, world")


# In[10]:


greeting()


# In[16]:


#function 2 (parameters )

def calculator(a, b): #parameters 
    
    add = a + b #command 1
    #command 2 
    
    print(add)


# In[19]:


calculator(5, 4)


# In[23]:


def greeting(name): #input name
    print(f"hello, {name}!") #output statement 


# In[24]:


greeting("abhi")


# In[31]:


def average(numbers): #user parameter 
    total = sum(numbers)
    
    average = total/len(numbers)
    
    maximum = max(numbers)
    
    return total, average, maximum #return statements 


# In[35]:


numbers = [1, 2, 3, 4, 5]

tot, avg, maxi = average(numbers) # total, average, maximum


# In[36]:


tot, avg, maxi 


# In[39]:


#default parameters 

def power(base, exp = 3): #user parameter and 1 default para 
    return base ** exp 


# In[40]:


output = power(2)
print(output)


# In[41]:


#keyword arguments 


def describe(animal_type, animal_name, age = 0):
    print(f"my pet is a {animal_type}, named {animal_name}, age {age}!") #output statement 


# In[45]:


describe("dog", "oreo", 3) #keyword arguments 


# In[49]:


describe(animal_name = "oreo", age = 3, animal_type = "dog")


# In[50]:


#varible length arguments 

help(list)


# In[64]:


#varible length arguments (*args)


def total(*numbers): #*args
    
    total = 0 
    for num in numbers:
        total += num
    return total


# In[65]:
total = total(1,2,3,4,5)
print(total)



# In[66]: 


#keyword varible-length arguments (**kwargs)

#docstrings and documentation


def build_profile(first, last, **user_info):
    
    profile = {'first': first, 'last': last}
    
    for key, value in user_info.items():
        profile[key] = value
        
    return profile

    


# In[67]:


user = build_profile("abhi", "red", location = 'danala', age = '28', unit = 'software now')


# In[68]:


print(user)


# In[71]:


#docstrings and documentation #for multiple lines of information

#comments #short (one word, two words  comments)

def calc_area(length, width):
    
    """
    this function calculates the area of a rectangle.
    
    it expects two parameter called length and width.
    
    parameters:
    length is floating point input
    width is floating point input
    
    output:
    
    example: cal_area(5,4)
    20
    """
    
    rect = length * width
    
    return rect 
    





# In[72]:


print(calc_area.__doc__)


# In[73]:


#functions use "local and global varibles"

#recursive functions 

#csv files, and image files 

#apply pandas, pillow libraries to slove mutiple tasks 


# In[75]:


# #two algorithms 

# #encryption aglorithm and decryption algorithm

# user 1 - how are you? #original message

# #hackers, companies stealing your data, rouge organizations

# input (original message) - encryption algorithm - hides the messag - output (hidden message)


# user 2 - hidden message 

# input (hidden message) - decryption algo - output (original message)





# In[76]:


ord('a') #abc #97, 98, 99

original message = abc 
#encrypt aglo

hidden message = 979899

#decrypt algo

original message = abc 

#shift key


# In[86]:


#origianl message = 'a'
ord('a') + 10 


# In[88]:


chr(107)    


# In[89]:


hidden message = 'k'


# In[113]:


def encrypt(text, shift):
    """
    encrypt text by shifting each letter
    
    example:
    """
    
    result = ""
    
    for char in text:
        ascii_value = ord(char)
        
        shift_value = ascii_value - shift #5
        
        encrypted_char = chr(shift_value)
        
        result += encrypted_char
        
    return result 
        
        


# In[115]:


encrypted_message = encrypt("hello", 5)
print(encrypted_message)


# In[120]:


def decrypt(text, shift):
    
    result = ""
    
    for char in text:
        
        if char.isalpha():
            
            ascii_value = ord(char)

            shift_value = ascii_value + shift #5 #algorithm 

            decrypted_char = chr(shift_value)

            result += decrypted_char

    return result


# In[121]:


decrypt("mjqqt", 5)


# In[ ]:


original message = "fsdfDFGDBBb"


# In[122]:


help(str)


# In[ ]:


string = "hello"

for s in string:
    print(ord(s)) #original ascii_values 


# In[94]:


104
101
108
108
111

list1 = [109, 106, 113, 113, 116] #shift_key = 5


104, 101


# In[95]:


for num in list1:
    print(chr(num))


# In[96]:





# In[131]:


#encryption algorithm and decrypt algo

# user 1 (original message) - encrypt algo - hidden message (user 2)

# user 2 (hidden message) - decrypt algo - original message 


# ASCII logic 


ord('c') #a,b,c = 97, 98, 99 

shift = 5

#97 + 5 = 102, 103, 104

chr(104) #f, g, h 


# In[132]:


102, 103, 104

shift = 5 

#102 - 5 = 97, 98, 99

chr(97) #a,b,c 


# In[ ]:


#utf-8

