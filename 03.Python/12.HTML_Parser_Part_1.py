# with html parser - python3
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start : %s" % tag)
        for attr in attrs:
            print("-> %s > %s" %(attr[0], attr[1]))
    def handle_endtag(self, tag):
        print ("End   : %s" %tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty : %s" % tag)
        for attr in attrs:
            print("-> %s > %s" %(attr[0], attr[1]))

def print_tags(html_string):
    parser = MyHTMLParser()
    parser.feed(html_string)

n = int(input())
s_html = ""
for i in range(n):
    s_html += input()
print_tags(s_html)

# with regex way- not complete, because I must go now :(
# import re
# def print_tags(html_string):
#     start_patern = '<(\w+)>'
#     start_matches = re.findall(r'%s' % start_patern, html_string)
#     for match in start_matches:
#         print ("Start : %s" % match)

#     end_patern = '</(\w+)\s*>'
#     end_matches = re.findall(r'%s' % end_patern, html_string)
#     for match in end_matches:
#         print("End : %s" % match)

# n = int(input())
# for i in range(n):
#     print_tags(input())

