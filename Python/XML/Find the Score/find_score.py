import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    attr_number = len(node.attrib)
    return attr_number + sum(get_attr_number(child) for child in node)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))