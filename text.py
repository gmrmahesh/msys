import urllib
import urllib.request
req = urllib.request.Request("https://www.redbus.in/info/contactus")
response = urllib.request.urlopen(req)
the_page = response.read()

numbers=re.findall("[0-9-]{7}[0-9-]+",str(the_page),re.I)
for n in numbers:
    print(n)
