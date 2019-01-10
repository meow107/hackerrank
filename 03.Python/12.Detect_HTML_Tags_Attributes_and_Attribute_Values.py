from html.parser import HTMLParser

class BPhoneHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print (tag)
        for attr in attrs:
            print ("-> %s > %s" % (attr[0], attr[1]))
   
    def handle_startendtag(self,tag, attrs):
        print (tag)
        for attr in attrs:
            print ("-> %s > %s" % (attr[0], attr[1]))
def print_tags(html_string):
    parser = BPhoneHTMLParser()
    parser.feed(html_string)


s = ""
n = int(input())
for i in range(n):
    s += input()
print_tags(s)