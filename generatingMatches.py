from Tkinter import *
from PIL import Image
import mechanize
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
from StringIO import StringIO

i=1
while i<100:
	br= mechanize.Browser()
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	print "Calling acad"
	image_response=br.open('https://academics.vit.ac.in/parent/captcha.asp')
	img=Image.open(StringIO(image_response.read()))
	imgorg=img.copy()
	imgorg.save("C:\Users\Kishore Narendran\Documents\Projects\\CaptchaBreaker\\testoutputs\Captcha"+str(i)+".bmp")
	i=i+1
