import re
def get_color(css_string):
    patern = '(\#[0-9A-Fa-f]{3,6})[;),]'
    matches = re.findall(r'%s' % patern, css_string)
    return matches

end_matches = []

n = int(input())
for i in range(n):
    end_matches += get_color(input())

print('\n'.join(end_matches))

