import math

class Solution():
    def sort3intergers(num):
        l = []
        for i in range(3):
            num = input('please enter an interger\n')
            l.append(num)
        l.sort(reverse = True) #从大到小排序
        print(l)

s = Solution()
s.sort3intergers()
