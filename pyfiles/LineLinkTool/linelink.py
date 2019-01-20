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
    """去掉字符串中的所有空格和换行"""
    S = ''.join(S.split(' '))
    return ''.join(S.split('\n'))

def linebreak_del(S):
    """
    1. 将'-\n'去掉
    2. 将换行符替换为空格
    """
    S = ''.join(S.split('-\n'))
    return ' '.join(S.split('\n'))

def text_processing(S, userInput):
    if userInput == 2:
        S_wd = linebreak_del(S)
    else:
        S_wd = whitespace_del(S)
    return S_wd
        


if __name__ == '__main__':
    
    userInput = input('''Press the main language of your passage
(1 for zh-hans(defult) and 2 for English):\n
Warning: it is not suitable for either cmd or IDLE, environment Anoconda is OK to run this.''')
    
    userInput = int(userInput)
    
    while True:
        S = input('Enter the Passage: ')
        S = strQ2B(S)
        if S == '.':
            break
        
        S_wd = text_processing(S, userInput)
        
        pyperclip.copy(S_wd)
        
    print('Thanks for using!')   
   
