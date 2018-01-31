class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        else:
            if x < 0:
                r = int(str(x)[:0:-1])
                r = -r
            else:
                r = int(str(x)[::-1])
            if abs(r) > 2**31:
                return 0
            else:
                return r
