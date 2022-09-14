'''
Descripttion: 
version: 
Author: Martin
FilePath: \Martin_Code\Python\信息论\signal.py
Date: 2022-06-27 22:00:17
LastEditTime: 2022-07-01 08:38:45
'''
import math

# 统计字符的概率
def get_text_count(text):
    '''统计字符出现频率,返回一个字典和字符相应概率'''
    chars = []
    ret = []
    ret2 = []
    for char in text:
        #print(char)
        if char in chars:
            continue
        else:
            chars.append(char)
            ret.append((char, text.count(char)/len(text))) #直接计算相应字符的概率
    ret.sort(key=lambda item:item[1])
    print('ret',ret)
    #计算熵
    H=0
    for item in ret:
        H += item[1] * math.log(item[1], 2) * (-1)
    #计算平均码长
    p = 1
    for item in ret:
        p *= pow(item[1],text.count(item[0]))
        #print(p)
    print('p',p)
    average_sign_length = math.ceil(-1*math.log(p,2))
    print('average_sign_length',average_sign_length)
    char_dict = {}
    temp = 0
    for item in ret:
        char_dict[item[0]] = (temp, temp+item[1])
        temp+=item[1]
    
    print('char_dict',char_dict)
    return char_dict,average_sign_length,H
 
# 编码，返回字符串(左端点)
def encoder(text, char_dict):
    # 根据字符和字典进行编码，返回区间左端点的值
    left = 0
    right = 1
    for s in text:
        span_length = right - left
        right = left + span_length * char_dict[s][1]  # 右端点+区间长度*
        left = left + span_length * char_dict[s][0]  #这个放下面，否则会left，right不是同时变
        #print(left)
    ##print('left',left)
    # print(type(left)) # float
    return left

# 解码
def decoder(singal_str, char_dict, len_text):
    text = []
    #print(char_dict)
    while len_text:
        for k, v in char_dict.items():
            if v[0] <= singal_str < v[1]:      # 在对应区间内
                print(v[0],v[1])
                text.append(k)
                range = v[1] - v[0]        #在对应区间求子区间
                singal_str -= v[0]         #
                singal_str /= range        #
                break
        len_text -= 1
    ret = ''
    for item in text:
        ret+=item
    return ret

# float转bin 
def ten2bin(singal_str,average_sign_length):
    ret = ''
    while(average_sign_length!=0):
        singal_str = singal_str*2
        if singal_str>1:
            ret+='1'
            singal_str-=1
        else:
            ret+='0'
        average_sign_length-=1
    print(ret)
    return ret
 
def main(text):

    # 返回字典和相应的区间
    char_dict,average_sign_length,H = get_text_count(text)
    print('H',H)
    # 编码，返回字符串(float)
    singal_str = encoder(text, char_dict)
    print('singal_str',singal_str)
    # 编码后的字符串转2进制
    singal_bin_str = ten2bin(singal_str,average_sign_length)
    
    final_str = decoder(singal_str, char_dict, len(text))
    print('final_str',final_str)
    efficiency = '{:.2%}'.format(H/average_sign_length*len(text))
    print('算数编码结果:',singal_bin_str)
    print('算数译码结果:',final_str)
    print('算数编码效率:',efficiency)
    return singal_bin_str,text,efficiency

if __name__ == '__main__':
    text = "gtrhytjyttt"
    # 返回字典和相应的区间
    char_dict,average_sign_length,H = get_text_count(text)
    print('H',H)
    # 编码，返回字符串(float)
    singal_str = encoder(text, char_dict)
    print('singal_str',singal_str)
    # 编码后的字符串转2进制
    singal_bin_str = ten2bin(singal_str,average_sign_length)
    
    final_str = decoder(singal_str, char_dict, len(text))
    print('final_str',final_str)
    efficiency = '{:.2%}'.format(H/average_sign_length*len(text))
    print('算数编码结果:',singal_bin_str)
    print('算数译码结果:',final_str)
    print('算数编码效率:',efficiency)
    #print(type(singal_bin_str),type(final_str),type(efficiency))