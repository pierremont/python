"""
In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'.
 If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.
"""
def well():
    x = ['good', 'bad', 'bad', 'bad', 'bad']
    #x = ["bad", "bad"]
    count = 0
    for i in x:
        print (i)
        if i == "good":
            count = count + 1
    #if count in range(1,3):
    if count ==1  or count == 2:
        response = 'Publish'
    elif count > 2:
        response = 'I smell a series!'
    else:
        response = 'Fail!'
    return response

print (well())

