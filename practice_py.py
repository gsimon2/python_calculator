import sys
import numpy

class PracticePy:
    def __init__(self):
        list_of_strings = ['cat', 'big barn', 'race car', ' ']

        
        #self.is_pal(list_of_strings)
        #self.reverse_int(5476)
        #print(self.is_substr("home", "me"))
        #print(self.cap_string("lower case string"))

        array = numpy.random.randint(0,100, size = 10)
        array = self.insertion_sort(array)
        print(array)


    def insertion_sort(self, input):
        for index in range(1, len(input)):
            val = input[index]
            
            while index > 0 and input[index-1] > val:
                input[index] = input[index - 1]
                index = index -1

            input[index] = val
        
        return input


    def swap_nums_with_temp(self, num1, num2):
        num1 = num1 + num2
        num2 = num1 - num2
        num1 = num1 - num2
        return num1, num2

    # Capitalizing characters of a string without the .upper() or .lower() functions
    def cap_string(self, str):
        s = list(str)
        
        for index, char in enumerate(s):
            if 97 <= ord(s[index]) <= 122:
                s[index] = chr(ord(s[index]) - 32)
        str = "".join(s)
        return str



    def is_substr(self, str1, str2):
        str1 = str1.replace(" ", "") # String spaces
        str2 = str2.replace(" ", "")

        # Check for empty strings
        if not str1 or not str2:
            return False

        # Check if str2 is contained within str1 starting at any possible i index of str1
        for i in range(0,len(str1),1):
            if all( ((i+j) < len(str1)) and (str1[i+j].lower() == str2[j].lower()) for j in range(0,len(str2),1)):
               return True

        return False


    def is_pal(self, list):
        
        for string in list:
            string = string.replace(" ", "") # Strip spaces
            if not string: # Check for empty string
                continue
            
            if all( char.lower() == string[-(index+1)].lower() for index, char in enumerate(string)):
                print('{} is a palindrome'.format(string))
            else:
                print('{} is not a palindrome'.format(string))

    def reverse_int(self, num):
        temp = str(num)
        temp = temp[::-1]
        print(int(temp))
        


if __name__ == "__main__":
    prog = PracticePy()

