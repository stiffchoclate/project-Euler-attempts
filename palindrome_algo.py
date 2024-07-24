#Problem 4: What is the largest possible palindrome that is the product of two 3-digit numbers?


#how do i detect whether the number is a palindrome
#reads the same forward and backwards
"""it's probably a recursive solution.
all single digit numbers are pallindromes.
exs: 11, 22, 222, 323, 42121, 9876789
must consider when the number of digits is even/odd?
 """

def reversing():
    listt = [2,3,4,5]
    print(type(listt.reverse()))

def palindrome(num):
    num_list = list(str(num))
    reverse_num_list = list(reversed(num_list))
    flag = True
    ptr = 0
    length = len(num_list)
    while flag == True and ptr<= (length//2):
        if num_list[ptr] != reverse_num_list[ptr]:
            flag = False
        else:
            ptr+=1
    
    return flag

def isPalindrome(num):
    string = str(num)
    return string == string[::-1]

def largestPalindrome(digits):
    max = ""
    for x in range (digits):
        max+= "9"
    max = int(max)
    min = 10**(digits-1)
    largest = 1

    for a in range(max,min-1, -1):
        for b in range(max,min-1, -1):
            if isPalindrome(a*b) == True and a*b>largest:
                largest = a*b
            else:
                pass
    return largest


print (largestPalindrome(3))