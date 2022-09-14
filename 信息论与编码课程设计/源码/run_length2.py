
'''
Descripttion: 
version: 
Author: Martin
FilePath: \Martin_Code\Python\信息论\run_length2.py
Date: 2022-06-27 14:52:00
LastEditTime: 2022-07-02 10:51:53
'''
from base64 import decode
from cmath import log
import math
# 统计字符出现频率,返回01字符相应的概率
def get_text_count(text):
    pi_list = []
    pi_list.append(text.count('0')/len(text))
    pi_list.append(text.count('1')/len(text))
    return pi_list

def encode_str(bin_str,max_bin_length):
    '''游程编码，返回编码结果'''
    print(bin_str)
    ret = ''
    # 默认0游程开始编
    # 检验开头是否为0
    if bin_str[0] == '1':
        #是1先写个0
        ret+=(bin(0)[2:]).rjust(max_bin_length,'0')
    
    # 连续值进行游程编码
    sum = 1
    i = 1
    while i<len(bin_str):
        # 边界
        if i == len(bin_str):
            #最后两个数相同
            if bin_str[i]==bin_str[i-1]:
                sum+=1
                i+=1
                ret+=(bin(sum)[2:]).rjust(max_bin_length,'0')
                    #print(2,sum)
            else:
                ret+=(bin(sum)[2:]).rjust(max_bin_length,'0')
                ret+=(bin(1)[2:]).rjust(max_bin_length,'0')
        elif bin_str[i]==bin_str[i-1]:
            sum+=1
            i+=1
        else:
            ret+=(bin(sum)[2:]).rjust(max_bin_length,'0')
            sum=1
            i+=1
            # ret+=(bin(sum)[2:]).rjust(max_bin_length,'0')
                #print(1,sum)
    if bin_str[len(bin_str)-1] != bin_str[len(bin_str)-2]:
        ret+=(bin(1)[2:]).rjust(max_bin_length,'0')
    else:
        ret+=(bin(sum)[2:]).rjust(max_bin_length,'0')
    # print('ret',ret)
    return ret

def decode_str(run_length_str,max_bin_length):
    '''游程解码'''
    ret = ''
    print(run_length_str)
    while(run_length_str!=''):
        if run_length_str=='':
            break
        temp = run_length_str[:max_bin_length]
        #print(int(temp,2))
        print(temp)
        temp_int = int(temp,2)
        while(temp_int>0):
            ret += '0'
            temp_int-=1
        run_length_str = run_length_str[max_bin_length:]
        if run_length_str=='':
            break
        temp = run_length_str[:max_bin_length]
        #print(int(temp,2))
        temp_int = int(temp,2)
        while(temp_int>0):
            ret += '1'
            temp_int-=1
        run_length_str = run_length_str[max_bin_length:]
    # print(ret)
    # 转ascii
    ret2 = ''
    print('ret',ret)
    while(ret!=''):
        temp = ret[:8]
        print('temp',temp)
        ret = ret[8:]
        ret2 += chr(int(temp,2))
        print('ret2',ret2)
    #print(ret2)
    return ret2

def get_max_bin_length(bin_str):
    # 返回最大二进制等长码长度
    print(bin_str)
    max_bin_length = 0
    sum = 1
    i = 1
    while i<len(bin_str):
        # 边界
        if i == len(bin_str)-1:
            #最后两个数相同
            if bin_str[i]==bin_str[i-1]:
                sum+=1
                i+=1
                if max_bin_length<sum:
                    max_bin_length = sum
                    #print(2,sum)
            else:
                if max_bin_length<sum:
                    max_bin_length = sum
                    break
                else:break
        elif bin_str[i]==bin_str[i-1]:
            sum+=1
            i+=1
        else:

            if max_bin_length<sum:
                max_bin_length = sum
                #print(1,sum)
            sum=1
            i+=1
    #print(max_bin_length)
    max_bin_length = math.ceil(math.log(max_bin_length,2))
    for i in range(max_bin_length):
        if pow(2,i) == max_bin_length:
        # 2的幂
            max_bin_length+=1
            break
    print(max_bin_length)
    return max_bin_length

def main(text):
    bin_str = ''
    for ch in text :
        #print(bin(ord(ch))[2:])
        bin_str += bin(ord(ch))[2:].rjust(8,'0')
    pi_list = get_text_count(bin_str)
    print('pi_list',pi_list)
    #统计最大二进制数位
    ##bin_str = '1100110'
    max_bin_length = get_max_bin_length(bin_str)
    # 编码
    run_length_str = encode_str(bin_str,max_bin_length)
    # 解码
    final_str = decode_str(run_length_str,max_bin_length)
    H = 0
    for i in range(len(pi_list)):
        H += pi_list[i] * math.log(pi_list[i], 2) * (-1)
    average_code_length = len(run_length_str)/len(bin_str)
    print(average_code_length)
    efficiency = '{:.2%}'.format(H/average_code_length)
    print('游程编码结果:',run_length_str)   
    ##print('游程编码结果:',char_count_list)   
    print('游程译码结果:',final_str)
    print('游程编码效率:',efficiency)
    return run_length_str,final_str,efficiency

if __name__ == '__main__':
    #main('abavac')
    text = '2020210593aaaaaabbbbdaeqtjklczxjioxzxjl'
    bin_str = ''
    for ch in text :
        #print(bin(ord(ch))[2:])
        print(ch)
        bin_str += bin(ord(ch))[2:].rjust(8,'0')
        print(bin_str)
    pi_list = get_text_count(bin_str)
    print('pi_list',pi_list)
    #统计最大二进制数位
    #bin_str = '1100110'
    max_bin_length = get_max_bin_length(bin_str)
    # 编码
    run_length_str = encode_str(bin_str,max_bin_length)
    # 解码
    final_str = decode_str(run_length_str,max_bin_length)
    H = 0
    for i in range(len(pi_list)):
        H += pi_list[i] * math.log(pi_list[i], 2) * (-1)
    average_code_length = len(run_length_str)/len(bin_str)
    print(average_code_length)
    efficiency = '{:.2%}'.format(H/average_code_length)
    print('游程编码结果:',run_length_str)   
    ##print('游程编码结果:',char_count_list)   
    print('游程译码结果:',final_str)
    print('游程编码效率:',efficiency)
