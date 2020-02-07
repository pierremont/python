
def check_odd(number):
    if 1 <= number <= 100:
        #checks if the number is even
        if (int(number) % 2 ) != 0:
            print('Weird')
        else:
            if 2 <= number <= 5:
                print("Not Weird")
            if 6 <= number <= 20:
                print("weird")
            if number > 20:
                print ("not weird")

print(check_odd(22))



'''
Given an integer,, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20 , print Weird
If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer,

Constraints: 1 <= n <= 100
Output Format: Print Weird if the number is weird; otherwise, print Not Weird.

'''

