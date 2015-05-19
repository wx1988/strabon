import sys

def gen_query(fpath,conf = 'strabon_iswc.conf'):
    cmd = './strabon -c %s query "%s"'
    content = open(fpath,'r').read()
    content = content.replace('\n',' ')
    content = content.replace('"','\\\\\\"')
    real_cmd = cmd%(conf, content)
    print real_cmd

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print sys.argv[1]
        gen_query(sys.argv[1])
    elif len(sys.argv) == 3:
        print sys.argv[1], sys.argv[2]
        gen_query(sys.argv[1], sys.argv[2])


