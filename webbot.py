import urllib2
import re


def read_names(url):
    '''reads all the usernames on the first page of a reddit url'''
    hdr = { 'User-Agent' : 'super happy flair bot by /u/spladug' }
    req = urllib2.Request(url, headers=hdr)
    webpage = urllib2.urlopen(req)
    #check that we http requestr is successful
    if webpage.getcode() == 200:
        html = webpage.read()
        x1 = re.findall('div id="siteTable.*', html)
        x = re.findall('http://www.reddit.com/user/(.*?)"', x1[0])
        return x[1::]
        
        


print read_names('http://www.reddit.com/r/aww/')
    
