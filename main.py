"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO
    x = x.binary_vec
    y = y.binary_vec #we need to turn x and y into vectors so we can make sure the lengths of the binary numbers are equal for multiplication
    
    pad(x,y) #want to get the same length of binary integers
    
    if len(x) == len(y) == 1: #the most simple base case
        return x*y #if both have a length 1, then you simply need to multiply the two as normal integers 
    else:
        #we want to split both vectors into 2 sections of equal length and return the integer value so that we can call our function again
        #we want to distinguish between the 2 values created for each variable x and y so we access the vector corresponding to left and right
        x_left = split_number(x)[0]
        x_right = split_number(x)[1]
        y_left = split_number(y)[0]
        y_right = split_number(y)[1]

        #now we want to change these numbers back into binary form 
        x_left = BinaryNumber(x_left)
        x_right = BinaryNumber(x_right)
        y_left = BinaryNumber(y_left)
        y_right = BinaryNumber(y_right)
        
        #we want to create a variable that is the sum of each individual variable so we can multiply these values together
        #we then want to convert these to binary numbers like the other parts of our vectors 
        x_left_right = x_left + x_right
        x_left_right = BinaryNumber(x_left_right)
        y_left_right = y_left + y_right
        y_left_right = BinaryNumber(y_left_right)
        
        #we now want to call our function 
        m = subquadratic_multiply(x_left, y_left)
        n = subquadratic_multiply(x_right, y_right)
        o = subquadratic_multiply(x_left_right, y_left_right)
        o_sum = o - n - m #we want this because o is double counting and we just want the difference WITHOUT the double counts of values
        
        #we want to convert them into binary numbers as before
        m = BinaryNumber(m)
        n = BinaryNumber(n)
        o = BinaryNumber(o)
        #now we want them to be vectors to bit-shift them
        m = m.binary_vec
        m = bit_shift(m, len(x))
        n = n.binary_vec
        n = bit_shift(n, len(x))
        o = o.binary_vec
        o = bit_shift(o, len(x)//2)
        
        #now we want to convert the numbers back to integers, sum each individual operation, and return this sum
        m = binary2int(m).decimal_val
        n = binary2int(n).decimal_val
        o = binary2int(o).decimal_val
        sum = m + n + o
        return sum
    pass
    ###

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(0), BinaryNumber(2)) == 0
    assert subquadratic_multiply(BinaryNumber(20), BinaryNumber(20)) == 400

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

