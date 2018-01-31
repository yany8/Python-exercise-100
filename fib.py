class Solution():
    def fib(self, n):
        if n==1 or n==2:
            return 1
        a = 1
        b = 1
        for i in range(n-2):
            res = a + b
            a, b = b, a+b
        print(res)

s = Solution()
s.fib(588)
