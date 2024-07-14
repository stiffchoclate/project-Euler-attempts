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
    terms = []

    for a in range(1,min+1):
        for b in range(1, max+1):
            terms.append(a*b)
    for each in terms[::-1]:
        if isPalindrome(each) == True:
            return each


print (largestPalindrome(3))