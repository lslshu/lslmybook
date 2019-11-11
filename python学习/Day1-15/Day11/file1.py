"""
从文本文件中读取数据

Date: 2019-11-11
"""


import time


def main():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('致橡树.txt', encoding ='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('致橡树.txt',encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()

#报错UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 4: illegal multibyte sequence
#解决办法：with open(fname, encoding='utf-8') as data_file，即以encoding='utf-8'方式读文件。