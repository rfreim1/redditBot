import urllib2
import urllib
import re
import os
import sys

##BUG: copies image url twice
    #temp fix: use set() on array to remove all duplicates

class User:

    def __init__(self, web):
        self.webpage = web
        
    images = []

    def download(self, path):
        '''Downloads all images of this reddit user into path specified'''
        #print 'downloading...'
        for i in self.images:
            print i
            ##ISSUE: When using Reddit API probably want img titles to be titles of threads
            urllib.urlretrieve(i, path+'\\'+i[19::])
        return 0


def open_url(url):
    hdr = { 'User-Agent' : 'super happy flair bot by /u/ramse42' }
    req = urllib2.Request(url, headers=hdr)
    webpage = urllib2.urlopen(req)
    #check that we http requestr is successful
    if webpage.getcode() == 200:
        return webpage.read()


def read_names(url):
    '''reads all the usernames on the first page of a reddit url'''
    html = open_url(url)
    #Skip some html so doesnt read moderator usernames
    contentHtml = re.findall('div id="siteTable".*', html)
    userLinks = re.findall('(http://www.reddit.com/user/.*?)"',
                           contentHtml[0])
    return userLinks



def get_imageLinks(uLink):
    '''Takes a reddit user link and gets all pictures submitted from that user'''
    html = open_url(uLink)
    contentHtml = re.findall('div id="siteTable".*', html)
    #with this iteration, using only regex...very hard to see if img is in aww
    #need better way to parse Html...right now just getting all imgur links
    

    #ISSUE: doesnt recognize links directly to imgur; only actually imgs
    imgLinks = [x for x in
                set(re.findall(
                    "http://i.imgur.com/\w+(?:\.jpg|\.gif|\.png)", html))]

    #add tumblr later
    #imgLinks += re.findall("http://25.media.tumblr.com/\w+/\w+(?:\.jpg|\.gif|\.png)", html)
    
    return imgLinks




if not os.path.exists(os.getcwd() + '\\images'):
    os.makedirs(os.getcwd() + '\\images')
    
submitted = [User(x + '/submitted/')
         for x in read_names('http://www.reddit.com/r/aww/') ]
submitted[2].images = get_imageLinks(submitted[2].webpage)
print submitted[2].images
submitted[2].download(os.getcwd()+"\\images")

##for x in submitted:
##    x.images = get_imageLinks(x.webpage)
##    x.download(os.getcwd()+"\\images")
    
        
        


    
