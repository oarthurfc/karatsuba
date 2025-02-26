# Project: Multiplication of Large Numbers with Karatsuba  

## Project Description  

This project implements the **Karatsuba algorithm**, an efficient method for multiplying large numbers. Unlike the traditional approach, which has a complexity of **O(n^2)**, Karatsuba reduces the number of multiplications to **O(n^{\log_2 3}) ≈ O(n^{1.585})**, making it faster for large inputs.  

### Algorithm Logic  

Given two numbers X and Y, the algorithm splits them in half:  

**📌 \(X = A * 10^m + B\)**  

**📌 \(Y = C * 10^m + D\)**  

The multiplication of X by Y can be expressed as:  

**📌 \(X * Y = AC * 10^{2m} + ((A+B)(C+D) - AC - BD) * 10^m + BD\)**  

Where:  

- 🔹 **m**: The position where the split occurs (Number size / 2)  
- 🔹 **AC**: Multiplication of the most significant terms  
- 🔹 **BD**: Multiplication of the least significant terms  
- 🔹 **(A+B)(C+D) - AC - BD**: Cross multiplication  

The algorithm continues dividing recursively until X and Y are small enough to be multiplied directly.  

## Code Explanation  
The implementation of the Karatsuba algorithm is done in the following Python code:  

1. **User Input**  

   ```python
   bigNumOne = int(input("Write the first big number: "))
   bigNumTwo = int(input("Write the second big number: "))
   ```  

   - Requests two large integer numbers from the user and stores them in `bigNumOne` and `bigNumTwo`.  

2. **Function Definition**  

   ```python
   def karatsuba(X, Y):
   ```  

   - Defines the recursive function that implements the Karatsuba algorithm.  

3. **Base Case: Direct Multiplication**  

   ```python
   if X < 10 or Y < 10:
       return X * Y
   ```  

   - If the numbers have only one digit, it returns the direct multiplication.  

4. **Determining the Split Point**  

   ```python
   n = max(len(str(X)), len(str(Y)))
   half = n // 2
   ```  

   - Determines the maximum number of digits in the numbers and divides by half to separate them.  

5. **Splitting the Numbers**  

   ```python
   A = X // (10 ** (half))  # Left half of X
   B = X % (10 ** (half))   # Right half of X
   C = Y // (10 ** (half))  # Left half of Y
   D = Y % (10 ** (half))   # Right half of Y
   ```  

   - Splits `X` and `Y` into their left (most significant) and right (least significant) parts.  

6. **Recursion to Calculate Subproducts**  

   ```python
   AC = karatsuba(A, C)
   BD = karatsuba(B, D)
   ad_plus_bc = karatsuba(A + B, C + D) - AC - BD
   ```  

   - Recursively computes the multiplications of the number pairs.  

7. **Combining the Results**  

   ```python
   return AC * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + BD
   ```  

   - Returns the final result by combining the subproducts.  

8. **Executing the Function and Displaying the Result**  

   ```python
   print("The result is", karatsuba(bigNumOne, bigNumTwo))
   ```  

   - Calls the function with the input values and prints the result.  

## How to Run the Project  

### Requirements  

- 🐍 Python 3.x installed  

### Running the Code  

1. 📥 Clone this repository:  
   ```sh
   git clone https://github.com/oarthurfc/karatsuba.git
   cd karatsuba
   ```  
2. ▶️ Run the main script:  
   ```sh
   python main.py
   ```  
3. 🔢 Enter two large numbers when prompted.  

## Asymptotic Complexity  

| Case         | Complexity      |  
|-------------|----------------|  
| ⚡ Best case | \(O(1)\)       |  
| ⚡ Average case | \(O(n^{1.585})\) |  
| ⚡ Worst case | \(O(n^{1.585})\) |  

The algorithm reduces the number of multiplications from **O(n^2)** to **O(n^{\log_2 3}) ≈ O(n^{1.585})**, making it significantly faster for large numbers.  

## Function Control Flow  

![karatsuba-control-flow](https://github.com/oarthurfc/karatsuba/blob/main/karatsuba-control-flow.png)  

## Cyclomatic Complexity  

The cyclomatic complexity (M) is calculated as:  
📊 \(M = E - N + 2P\)  
Where:  

- 🔹 **E** = Number of graph edges  
- 🔹 **N** = Number of graph nodes  
- 🔹 **P** = Connected components (1 in this case)  

Resulting in:  
M = 15 - 12 + 2(1) = 5  

## References  

- 📚 [Karatsuba Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Karatsuba_algorithm)  
- 📚 [Complexity Analysis - Big O](https://www.bigocheatsheet.com/)  
- 📽️ [How can we multiply large integers quickly?](https://youtu.be/yWI2K4jOjFQ?si=KGkO7kpgvUNugZTK)  
