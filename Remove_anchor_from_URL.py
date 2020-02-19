'''
Complete the function/method so that it returns the url with anything after the anchor (#) removed.
# returns 'www.codewars.com'
remove_url_anchor('www.codewars.com#about')

# returns 'www.codewars.com?page=1'
remove_url_anchor('www.codewars.com?page=1')
'''

def remove_anchor(url):
    head, sep, tail = url.partition("#")
    return head

print(remove_anchor("www.codewars.com?page=1"))






