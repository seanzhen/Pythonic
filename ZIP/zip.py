import zipfile
import argparse
import os
from os.path import *

'''
demo

with zipfile.ZipFile('1.zip') as f:
    f.extractall(path='./',pwd=b'1234')
    print('sucessfully')

parser = argparse.ArgumentParser(description='test')
parser.add_argument('-n',dest='m_name',type=str,help='your name')
options = parser.parse_args()
print('hello',options.m_name)

'''

def tryzippwd(zipfile,pwd,savep):
    try:
        zipfile.extractall(path = savep,pwd=pwd.encode('utf-8'))
        print('success, password: %s' % (pwd))
        return True
    except:
        # print(zipfile)
        print('failed, password: %s' % (pwd))
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='brute crack zip')
    parser.add_argument('-f', dest='zFile', type=str, help='The zip file path.')
    parser.add_argument('-w', dest='pwdFile', type=str, help='Password dictionary file.')
    zFilePath = None
    pwdFilePath = None
    try:
        options = parser.parse_args()
        zFilePath = options.zFile
        pwdFilePath = options.pwdFile
    except:
        print(parser.parse_args(['-h']))
        exit(0)

    if zFilePath == None or pwdFilePath == None:
        print(parser.parse_args(['-h']))
        exit(0)

    with zipfile.ZipFile(zFilePath) as z:
        with open(pwdFilePath) as f:
            for pwd in f.readlines():
                p,f = split(zFilePath)
                # print(p)
                # print(f)
                dirName = f.split('.')[0]
                dirPath = join(p,dirName)
                # print(dirPath)
                try:
                    os.mkdir(dirPath)
                except:
                    pass
                ok = tryzippwd(z,pwd.strip('\n'),dirPath)
                if ok:
                    break



