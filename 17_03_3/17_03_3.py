import sys
import re


def mkstr(line):
    line = re.sub(r'_([^_]+)_', r'<em>\g<1></em>', line)
    line = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)',
                  r'<a href="\g<2>">\g<1></a>', line)
    return line


lines = [line.strip() for line in sys.stdin]
blocks = []
inline = False
for line in lines:
    if inline:
        if line != '':
            blocks[-1].append(line)
        else:
            inline = False
    else:
        if line != '':
            blocks.append([])
            blocks[-1].append(line)
            inline = True
for block in blocks:
    if block[0][0] == '*':
        print('<ul>')
        for line in block:
            print('<li>' + mkstr(line[1:].lstrip()) + '</li>')
        print('</ul>')
    elif block[0][0] == '#':
        lv = block[0].index(' ')
        print('<h%d>' %
              (lv,) + mkstr(block[0].replace('#', ' ').lstrip()) + '</h%d>' % (lv,))
    else:
        for i, line in enumerate(block):
            line = mkstr(line)
            if i == 0:
                print('<p>', end='')
            if i == len(block) - 1:
                print(line + '</p>')
            else:
                print(line)
