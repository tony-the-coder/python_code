#Import the tools to open the page
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
#Deal with any possible SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#Get a URL from the user
url = input("Enter a URL: ")
#If a URL with less than three characters was entered user the test page to run the script
if len(url)< 3:
    url = 'http://py4e-data.dr-chuck.net/comments_551233.xml'
print("Retrieving:", url)
#Opens and reads the page
addr = urllib.request.urlopen(url, context=ctx).read()
more = str(len(addr))
print("Retrieving:",more, "characters")
tree = ET.fromstring(addr)
#Finds the item named count in the XML tree and sets it to list. The count is a couple of levels down. 
list = tree.findall('.//count')
#Testing loop with the name field
#other_list = tree.findall('./name')
print("Count:", str(len(list)))
total = 0
#Loops through the list to find the item named count and converts them from text to integers so that they can be summed.
for item in list:
    numbers = int(item.text)
    total += numbers
    #print(numbers)
print("Sum:", total)
