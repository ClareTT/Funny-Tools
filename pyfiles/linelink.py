# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 17:23:52 2018

用于将文献中copy过来的格式杂乱的文字，实现去掉回车、全角转半角的功能
并将转换完成的文字copy到剪切板上
检测到'.'即结束运行

@author: llwang
"""

import pyperclip

def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全角空格直接转换            
            inside_code = 32 
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring

def strB2Q(ustring):
    """半角转全角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 32:                                 #半角空格直接转化                  
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:        #半角字符（除空格）根据关系转化
            inside_code += 65248

        rstring += chr(inside_code)
    return rstring

def whitespace_del(S):
    """去掉字符串中的所有空格"""
    output_s = ''
    return output_s.join(S.split('\n'))

if __name__ == '__main__':
    while True:
        S = input('Enter the Passage: ')
        if S == '.':
            break
        S_wd = whitespace_del(S)
        output = strQ2B(S_wd)
        
        pyperclip.copy(output)
        
    print('Thanks for using!')     
   