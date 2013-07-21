from Tkinter import *
import Image, ImageTk
import mechanize
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
from StringIO import StringIO

br= mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
print "Calling acad"
image_response=br.open('https://academics.vit.ac.in/parent/captcha.asp')
img=Image.open(StringIO(image_response.read()))
imgorg=img.copy()
#img=Image.open("C:\Windows\Temp\Captcha.bmp")
pix = img.load()
print img.size
temp=0;
for y in range(0, 129, 1):
    for x in range(0, 24, 1):
        temp=pix[y,x]
        if(x!=0 and x!=24):
            if(pix[y,x+1]==0 and temp==1 and pix[y,x-1]==0):
                pix[y,x]=0

start=[]
end=[]
end.append(0)
k=0
i=0
d=0
c=[]
for d in range(0,6,1):
    start.append(0)
    end.append(0)
    flag=0
    for y in range(end[k-1], 129, 1):
        c.append(0)
        for x in range(0,24,1):
            if(pix[y,x]==1):
                c[i]=c[i]+1
        if(c[i]>4 and i!=0 and flag==0):
            start[k]=i
            print "D:"+str(d)+"\tS:"+str(i-1)
            flag=1
        if(c[i]<4 and flag==1):
            if(i-start[k]>6):
                end[k]=i
                print "D:"+str(d)+"\tE:"+str(i)
                break
            else:
                flag=0
        d=d+1
        i=i+1
    k=k+1

imgorg.save("C:\Users\Kishore Narendran\Documents\Projects\CaptchaBreaker\\testoutputs\Original.bmp")
img.save("C:\Users\Kishore Narendran\Documents\Projects\CaptchaBreaker\\testoutputs\Stripped.bmp")
print str(start) + '\n' + str(end)
for r in range(0, 6, 1):
    tempimg=img.copy()
    temppix=tempimg.load()
    for y in range(0, 129, 1):
        for x in range(0, 24, 1):
            if(y>end[r] or y<start[r]):
                temppix[y,x]=0
    tempimg.save("C:\Users\Kishore Narendran\Documents\Projects\CaptchaBreaker\\testoutputs\img"+str(r)+".bmp")

print "All Done! :D"
