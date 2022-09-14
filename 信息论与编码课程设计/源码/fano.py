'''
Descripttion: 
version: 
Author: Martin
FilePath: \Martin_Code\Python\信息论\fano.py
Date: 2022-06-27 16:44:42
LastEditTime: 2022-07-01 16:00:03
'''
import math

class Node: 
    def __init__(self, sign_str,name,pi):
        self.sign_str = sign_str
        self.name = name
        self.pi = pi
        self.flag = 0

# 统计字符出现频率,返回一个字典和字符相应的概率
def get_text_count(text):
    '''
    统计字符出现频率,返回一个字典和字符相应概率
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
            ret.append((char, text.count(char)/len(text))) #直接计算相应字符的个数
    # print(chars)
    # print('ret',ret)
    tmp_ret =ret
    ret.sort(key = lambda item:item[1])     #根据概率从小到大排序
    for item in ret:
        ret2.append(item[1])
    # print('ret2',ret2)
    #返回从小到大
    ret2.sort()
    return ret,ret2

# 创造节点
def crate_nodes(char_count_list):
    return [Node('',item[0],item[1]) for item in char_count_list]

def fano_encode2(nodes,pi_list,position):
    pass
# fano编码
def fano_encode(nodes,pi_list,positon):
    if len(pi_list) <= 1:
        return 0
    # 最佳分组位置
    mini_difference = 1
    find_position = 1
    for i in range(len(pi_list)):
        sum1 = 0
        sum2 = 0
        for i in range(i+1):
            sum1 += pi_list[i]
        for j in range(i+1,len(pi_list)):
            sum2 += pi_list[j]
        difference = abs(sum1 - sum2)
        if difference < mini_difference:
            mini_difference = difference
            find_position = i+1
            # print(find_position)
    print(find_position)
    # 编码
    for i in range(len(pi_list)):
        if nodes[i+positon].flag==0: #可写入
            if i < find_position:
                nodes[i+positon].sign_str = nodes[i+positon].sign_str+ '0'
                print(i+positon,nodes[i+positon].sign_str)
            else:
                nodes[i+positon].sign_str = nodes[i+positon].sign_str+ '1'
                print(i+positon,nodes[i+positon].sign_str)
            if len(pi_list)==2:  #最终值
                nodes[i+positon].flag=1
                print(i+positon,'之1')
    # 编码分组
    leftgroup = []
    rightgroup = []
    for i in range(find_position):
        leftgroup.append(pi_list[i])
    for i in range(find_position, len(pi_list)):
        rightgroup.append((pi_list[i]))

    # 递归编码
    fano_encode(nodes,leftgroup,0+positon)
    fano_encode(nodes,rightgroup,find_position+positon)

# 编码整个文本编码，返回编码结果
def encode_str(text,char_count_list,nodes):
    '''编码整个文本编码，返回编码结果'''
    ret = ''
    
    for char in text:
        for node in nodes:
            if node.name == char:
                    ret += node.sign_str
                    break
    
    return ret    

# 解码整个字符串
def decode_str(fan_str,char_count_list,nodes):
    '''解码整个字符串'''
    ret = ''
    while fan_str != '':
        for item in nodes:
            if item.sign_str in fan_str and fan_str.index(item.sign_str)==0: #从头开始
                ret+=item.name
                fan_str = fan_str[len(item.sign_str):]
                break
    return ret

# 求信源的的熵
def get_H(pi_list):
    '''求信源的的熵'''
    H = 0
    for i in range(len(pi_list)):
        H += pi_list[i] * math.log(pi_list[i], 2) * (-1)

    #print('信源熵：',H)
    return H

# 求平均码长
def get_average_code_length(nodes):
    '''求平均码长'''
    ret = 0
    for item in nodes:
        ret += len(item.sign_str)*item.pi
    print('ret',ret)
    return ret

def main(text):
    '''返回编码结果，译码结果，编码效率'''
    char_count_list,pi_list = get_text_count(text)
    #print('char_count_list',char_count_list)
    #print('pi_list',pi_list)
    nodes = crate_nodes(char_count_list)
    fano_encode(nodes,pi_list,0)
    # 打印fano字符对应的编码
    # for item in nodes:
    #     print(item.name,item.sign_str)
    fano_str = encode_str(text,char_count_list,nodes)
    #print('fan_str',fano_str)
    final_str = decode_str(fano_str,char_count_list,nodes)
    #print('final_str',final_str)
    H = get_H(pi_list)
    average_code_length = get_average_code_length(nodes)
    efficiency = '{:.2%}'.format(H/average_code_length)
    print('fano编码结果:',fano_str)
    print('fano译码结果:',final_str)
    print('fano编码效率:',efficiency)
    return nodes,fano_str,final_str,efficiency

if __name__ == '__main__':
    text = "2020210593"
    char_count_list,pi_list = get_text_count(text)
    print('char_count_list',char_count_list)
    #print('pi_list',pi_list)
    nodes = crate_nodes(char_count_list)
    fano_encode(nodes,pi_list,0)
    # 打印fano字符对应的编码
    for item in nodes:
        print(item.name,item.sign_str)
    fano_str = encode_str(text,char_count_list,nodes)
    print('fan_str',fano_str)
    final_str = decode_str(fano_str,char_count_list,nodes)
    print('final_str',final_str)
    H = get_H(pi_list)
    print('H',H)
    average_code_length = get_average_code_length(nodes)
    efficiency = '{:.2%}'.format(H/average_code_length)
    print('fano编码结果:',fano_str)
    print('fano译码结果:',final_str)
    print('fano编码效率:',efficiency)
