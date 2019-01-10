import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    count_atribs = 0
    for element in node.iter():
        count_atribs += len(element.attrib)
    return count_atribs


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


