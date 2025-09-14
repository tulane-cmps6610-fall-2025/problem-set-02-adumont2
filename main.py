"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time
import sys
import tabulate

# Increase recursion limit for large inputs
sys.setrecursionlimit(10000)

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

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y
    
def quadratic_multiply(x, y):
    """
    Multiplies two BinaryNumber objects using the grade-school recursive algorithm.
    """
    # Base case for recursion
    if x.decimal_val < 2 or y.decimal_val < 2:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    # Pad the binary vectors to be the same, even length
    x_vec, y_vec = pad(x.binary_vec, y.binary_vec)
    n = len(x_vec)
    
    # Split the numbers into high and low bits
    a, b = split_number(x_vec)
    c, d = split_number(y_vec)
    
    # Make 4 recursive calls
    ac = quadratic_multiply(a, c)
    ad = quadratic_multiply(a, d)
    bc = quadratic_multiply(b, c)
    bd = quadratic_multiply(b, d)
    
    # Combine the results
    term1 = bit_shift(ac, n)
    term2 = bit_shift(BinaryNumber(ad.decimal_val + bc.decimal_val), n // 2)
    
    final_result = BinaryNumber(term1.decimal_val + term2.decimal_val + bd.decimal_val)
    return final_result

def subquadratic_multiply(x, y):
    """
    Multiplies two BinaryNumber objects using the Karatsuba-Ofman algorithm.
    """
    # Base case for recursion
    if x.decimal_val < 10 or y.decimal_val < 10:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    # Pad the binary vectors to be the same, even length
    x_vec, y_vec = pad(x.binary_vec, y.binary_vec)
    n = len(x_vec)

    # Split the numbers into high and low bits
    a, b = split_number(x_vec)
    c, d = split_number(y_vec)
    
    # Make 3 recursive calls
    z2 = subquadratic_multiply(a, c)
    z0 = subquadratic_multiply(b, d)
    
    sum_ab = BinaryNumber(a.decimal_val + b.decimal_val)
    sum_cd = BinaryNumber(c.decimal_val + d.decimal_val)
    z1 = subquadratic_multiply(sum_ab, sum_cd)
    
    # Combine the results
    term1 = bit_shift(z2, n)
    middle_term_val = z1.decimal_val - z2.decimal_val - z0.decimal_val
    term2 = bit_shift(BinaryNumber(middle_term_val), n // 2)
    
    final_result = BinaryNumber(term1.decimal_val + term2.decimal_val + z0.decimal_val)
    return final_result

## Feel free to add your own tests here.
def test_multiply():
    # Corrected original test
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)).decimal_val == 4
    
    # Our additional tests
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)).decimal_val == 4
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(15)).decimal_val == 150
    assert subquadratic_multiply(BinaryNumber(10), BinaryNumber(15)).decimal_val == 150
    assert quadratic_multiply(BinaryNumber(123), BinaryNumber(456)).decimal_val == 123 * 456
    assert subquadratic_multiply(BinaryNumber(12345), BinaryNumber(6789)).decimal_val == 12345 * 6789
    print("All tests passed!")


# Professor's timing functions
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
    
def compare_multiply():
    res = []
    # Test with numbers of increasing size
    for n in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        print(f"Timing for n = {n}...")
        x = BinaryNumber(n)
        y = BinaryNumber(n)
        
        # Stop running the quadratic one for huge inputs as it takes too long
        if n > 100000:
            qtime = float('inf')
        else:
            qtime = time_multiply(x, y, quadratic_multiply)

        subqtime = time_multiply(x, y, subquadratic_multiply)
        res.append((n, qtime, subqtime))
            
    print_results(res)


def print_results(results):
    print("\n")
    print("Comparison of Multiplication Algorithm Runtimes (in ms)")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'Quadratic O(n^2)', 'Subquadratic O(n^1.585)'],
            floatfmt=".3f",
            tablefmt="github"))

if __name__ == "__main__":
    test_multiply()
    compare_multiply()    
    

