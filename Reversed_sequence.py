'''
codewars.com
Get the number n (n>0) to return the reversed sequence from n to 1.
Example : n=5 >> [5,4,3,2,1]
'''

n = input("enter n: ")

def reverse_seq(n):
    mylist = []
    for i in range(n):
        if n > 0:
            mylist.append(n)
            n = n - 1
        else:
            pass

    return mylist