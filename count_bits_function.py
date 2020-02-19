#######################
#write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
#Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
###########################


def countBits (number):
    count = 0
    try:
        if type(int(number)) == int and int(number) >= 0:
            number = bin(int(number))[2:]
            for i in number:
                if i == str(1):
                    count = count + 1
    except:
        print("incorrect integer")

    return count