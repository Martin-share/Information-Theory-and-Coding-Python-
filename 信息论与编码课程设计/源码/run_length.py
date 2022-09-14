'''
Descripttion: 
version: 
Author: Martin
FilePath: \Martin_Code\Python\信息论\run_length.py
Date: 2022-06-27 14:52:00
LastEditTime: 2022-07-01 09:41:26
'''
import math
# 统计字符出现频率,返回一个字典和字符相应的概率
def get_text_count(text):
    '''
    统计字符出现频率,返回字符相应概率
    '''
    chars = []
    ret = []
    ret2 = []
    for char in text:
        #print(char)
        if char in chars:
            continue
        else:
            chars.append(char)
            ret.append((char, text.count(char))) #直接计算相应字符的个数
    # print(chars)
    # print('ret',ret)
    for item in ret:
        ret2.append(item[1]/len(text))
    # print('ret2',ret2)
    return ret2

def encode_str(text):
    '''游程编码，返回二维列表[['a',2]]'''
    char_count_list = []
    i=1
    index=1
    max_num = 1
    while(index<len(text)):
        if(index==(len(text)-1)):
            if(text[index-1]==text[index]):#最后两个相同
                temp_list =[]
                temp_list.append(text[index-1])
                temp_list.append(i+1)
                char_count_list.append(temp_list)
            else:                          #最后两个不同
                temp_list1 =[]
                temp_list2 =[]
                temp_list1.append(text[index-1])
                temp_list1.append(i)
                if i>max_num:
                    max_num = i
                temp_list2.append(text[index])
                temp_list2.append(1)
                char_count_list.append(temp_list1)
                char_count_list.append(temp_list2)
            break
        if(text[index-1]!=text[index]):
            temp_list =[]
            temp_list.append(text[index-1])
            temp_list.append(i)
            char_count_list.append(temp_list)
            if i>max_num:
                max_num = i
            i=1
            index+=1
        else:
            i+=1
            index+=1
    print('max_num',max_num)
    print('print_char_count_list',char_count_list)
    ret = ''
    max_num = math.ceil(math.log(max_num,2))
    for i in range(max_num):
        if pow(2,i) == max_num:
        # 2的幂
            max_num+=1
            break
    for item in char_count_list:
        #ret += bin(ord(item[0]))[2:].rjust(7,'0')
        ret +=bin(ord(item[0]))[2:]
        ret += bin(item[1])[2:].rjust(max_num,'0')
    print('ret',ret) 
    return ret,char_count_list

def decode_str(char_count_list):
    '''游程解码'''
    length = len(char_count_list)
    ret = ''
    for item in char_count_list:
        for i in range(item[1]):
            ret+=item[0]
    # print('ret',ret)
    return ret

def main(text):
    char_count_list = encode_str(text)
    final_str = decode_str(char_count_list)
    temp = ''
    for i in char_count_list:
        for j in i:
            temp+=str(j)
    print('游程编码结果:',temp)
    #print('游程编码结果:' ,char_count_list)
    print('游程译码结果:' ,final_str)
    return char_count_list,final_str
 
if __name__ == '__main__':
    text = '10'
    pi_list = get_text_count(text)
    print('pi_list',pi_list)
    run_str,char_count_list = encode_str(text)
    print('run_str',run_str)
    print('char_count_list',char_count_list)
    final_str = decode_str(char_count_list)
    print('final_str',final_str)
    temp = ''
    for i in char_count_list:
        for j in i:
            temp+=str(j)
            
    print('游程编码结果:',run_str)   
    #print('游程编码结果:',char_count_list)   
    print('游程译码结果:',final_str)
    H = 0
    for i in range(len(pi_list)):
        H += pi_list[i] * math.log(pi_list[i], 2) * (-1)
    average_code_length = len(run_str)/(len(text)*7)
    efficiency = '{:.2%}'.format(H/average_code_length)
    print('游程译码效率:',efficiency)

