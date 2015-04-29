#!/usr/bin/env python


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):

        num_with_index = enumerate(num, start=1)

        _hash = {}
        for index, n in num_with_index:
            _hash[n] = index

        for i in xrange(len(num)):
            gap = target - num[i]

            if gap in _hash and i+1 != _hash[gap]:
                return i+1, _hash[gap]


        return (None, None)


def main():

    num = [3,2,4]
    target = 6

    sol = Solution()
    print sol.twoSum(num, target)

if __name__ == "__main__":

    main()

