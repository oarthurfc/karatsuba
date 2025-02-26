
bigNumOne = int(input("Write the first big number: "))
bigNumTwo = int(input("Write the second big number: "))

def karatsuba(X, Y):
    if X < 10 or Y < 10: # Stop condition
        return X * Y 
    else:
        n = max(len(str(X)), len(str(Y)))
        half = n // 2
        A = X // (10 ** (half)) #Left half of X
        B = X % (10 ** (half)) #Right half of X
        C = Y // (10 ** (half)) #Left half of Y
        D = Y % (10 ** (half)) #Right half of X
        AC = karatsuba(A, C)
        BD = karatsuba(B,D)
        ad_plus_bc = karatsuba(A+B, C+D) - AC - BD
        return AC * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + BD

print("The result is", karatsuba(bigNumOne, bigNumTwo))