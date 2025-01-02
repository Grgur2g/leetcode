class Solution:
    def nthUglyNumber(self, n: int) -> int:
        lista=[0]*n
        lista[0]=1
        a = b = c = 0
        for i in range(1,n):
            lista[i]=min(lista[a]*2,lista[b]*3,lista[c]*5)
            if lista[a]*2==lista[i]:a+=1
            if lista[b]*3==lista[i]:b+=1
            if lista[c]*5==lista[i]:c+=1
        return lista[n-1]
    


# Example 1:

# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

# Example 2:

# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
