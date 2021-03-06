# -*- coding: utf-8 -*-

'''
Word Pattern
============

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains
lowercase letters separated by a single space.
'''


class Solution(object):
    '''算法思路：

    用两个哈希表存储

    此题和《205 Isomorphic Strings》类似，都是一一对应
    '''
    def wordPattern(self, pattern, str):
        str = str.split(' ')
        if len(pattern) - len(str):
            return False

        t1, t2 = {}, {}
        for i, char in enumerate(pattern):
            if char not in t1 and str[i] not in t2:
                t1[char], t2[str[i]] = str[i], char
            elif not (char in t1 and
                    str[i] in t2 and
                    t1[char] == str[i] and
                    t2[str[i]] == char):
                return False
        return True


class Solution(object):
    '''算法思路：

    一一映射的个数 == parrtern 的个数 == str 的个数
    '''
    def wordPattern(self, pattern, str):
        str = str.split(' ')

        if len(pattern) != len(str):
            return False

        return len(
            set(zip(pattern, str))) == len(set(pattern)) == len(set(str))


s = Solution()
print s.wordPattern('jquery', 'jquery')
