#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def message():
    keys='abcefghijklmnopqrstuvwxyz !'
    value=keys[-1]+keys[0:-1]
    encryptDict=dict(zip(keys,value))
    decryptDict=dict(zip(value,keys))
    msg=input("Enter the message: ")
    mode=input("Enter the type: Encode(E) or Decode(D): ")
    if mode.upper()=='E':
        newmesg=''.join([encryptDict[letter] for letter in msg.lower()])
    elif mode.upper()=='D':
        newmesg=''.join([decryptDict[letter] for letter in msg.lower()])
    else:
        print(" Please enter E or D: ")
    return newmesg
print(message())


# In[ ]:




