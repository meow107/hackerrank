from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data:
            patern = '\n'
            matches = re.findall(r'%s' % patern, data)
            if matches:
                print (">>> Multi-line Comment \n%s" % data)
            else:
                print (">>> Single-line Comment \n%s" % data)


    def handle_data(self,data):
        if len(data) > 0 and data != "\n":
            print(">>> Data \n%s" % data)

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


