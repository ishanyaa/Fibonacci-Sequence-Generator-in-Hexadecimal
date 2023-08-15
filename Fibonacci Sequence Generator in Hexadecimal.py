#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fibonacci_hex_generator(n):
    if n <= 0:
        return []

    fib_sequence = ["0x0", "0x1"]
    while len(fib_sequence) < n:
        next_fib = hex(int(fib_sequence[-1], 16) + int(fib_sequence[-2], 16))
        fib_sequence.append(next_fib)

    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers you want to generate: "))
fib_hex_numbers = fibonacci_hex_generator(n)
print("Fibonacci Sequence (Hexadecimal):", fib_hex_numbers)


# In[ ]:





# In[ ]:




