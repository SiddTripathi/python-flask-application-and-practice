#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self,x: int) ->bool:
        num_palindrom = False
        str_x = str(x)
        if str_x[::] == str_x[::-1]:
            num_palindrom = True
            return num_palindrom
        else:
            return num_palindrom
    
    def isPalindrom_approach2(self,x: int) ->bool:
        num_palindrome=False
        list_x = []
        list_x.append(x)
        if list_x == list_x.reverse():
            num_palindrome=True
            return num_palindrome
        else:
            return num_palindrome
        


test = Solution()

print(test.isPalindrome(121))
print(test.isPalindrom_approach2(121))





list1 = [121]
list1.reverse()
print(list1)

