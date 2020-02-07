def count_bits ():
    number = input("enter ")
    count = 0
    try:
        if type(int(number)) == int and int(number) >= 0:
            print("correct integer and positive")
            number = bin(int(number))[2:]
            print(number)
            for i in number:
                if i == str(1):
                    count = count + 1
        else:
            print("integer, but negative")
    except:
        print("incorrect integer")

    if count !=0:
        return count
   

y = count_bits()
print (y)