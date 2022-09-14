'''
Descripttion: 
version: 
Author: Martin
FilePath: \Martin_Code\Python\信息论\Huffman.py
Date: 2022-06-27 12:08:28
LastEditTime: 2022-07-01 15:08:44
'''
import math
# 节点类
class Node: 
    def __init__(self, sign_str,name,pi):
        self.left = None
        self.right = None
        self.father = None
        self.sign_str = sign_str
        self.name = name
        self.pi = pi

    def is_left(self):
        return self.father.left == self
    def is_right(self):
        return self.father.right == self

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
    for item in ret:
        ret2.append(item[1])
    print('ret2',ret2)
    return ret,ret2

# 创建叶子节点,返回节点对象列表
def create_nodes(char_count_dict):
    '''创建叶子节点,返回节点对象列表'''
    return [Node('',item[0],item[1]) for item in char_count_dict]    

# 创建Huffman树,返回根节点
def create_huffman_tree(nodes):
    '''创建Huffman树,返回根节点'''
    queue = nodes[:]

    while len(queue) > 1:
        queue.sort(key=lambda item: item.pi) #队列排序，由小到大
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node('','',node_left.pi + node_right.pi)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)

    queue[0].father = None
    return queue[0]

# 根据Huffman树，从下向上编码，返回平均码长
def huffman_encoding(nodes, root,pi_list,text):
    average_code_length=0
    for node in nodes:
        temp_node = node     #递归的，改变的node
        while temp_node != root:
            if temp_node.is_left(): # 判断是不是父节点的左节点
                node.sign_str = '0' + node.sign_str
            else:
                node.sign_str = '1' + node.sign_str
            temp_node = temp_node.father
    
    for node in nodes:
       # print(node.sign_str,node.pi)
        average_code_length+=len(node.sign_str)*node.pi
    # print('average_code_length',average_code_length)
    return average_code_length

# 编码整个文本编码，返回编码结果
def encode_str(text, nodes):
    '''编码整个文本编码，返回编码结果'''
    ret = ''
    for char in text:
        for node in nodes:
            if char == node.name:
                ret += node.sign_str
    
    return ret

# 解码整个字符串
def decode_str(huffman_str, nodes):
    '''解码整个字符串'''
    ret = ''
    while huffman_str != '':
        for node in nodes: # 遍历节点列表，如果字符串有编码，则解码，保证从头开始解码
            if node.sign_str in huffman_str and huffman_str.index(node.sign_str) == 0:
                #ret += node.name                          #字节才有decode，int->str->byte->str,
                ret += node.name                           #不encode时用
                huffman_str = huffman_str[len(node.sign_str):]

    return ret

# 求信源的的熵
def get_H(pi_list):
    '''求信源的的熵'''
    H = 0
    for i in range(len(pi_list)):
        H += pi_list[i] * math.log(pi_list[i], 2) * (-1)

    #print('信源熵：',H)
    return H

def main(text):
    '''返回编码结果，译码结果，编码效率'''
    # text = text.encode('utf-8')
    char_count_dict,pi_list = get_text_count(text)
    H = get_H(pi_list)
    nodes = create_nodes(char_count_dict)
    root = create_huffman_tree(nodes)
    average_code_length = huffman_encoding(nodes, root,pi_list,text)
    huffman_str = encode_str(text, nodes)
    final_str = decode_str(huffman_str, nodes)
    efficiency = '{:.2%}'.format(H/average_code_length)
    print('Huffman编码结果:' + huffman_str)
    print('Huffman译码结果:' + final_str)
    print('Huffman编码效率:',efficiency)
    return nodes,huffman_str,final_str,efficiency

if __name__ == '__main__':
    text = "2020210593"
    # text = text.encode('utf-8')

    # 统计字符出现频率,返回一个列表（字典）和概率
    char_count_dict,pi_list = get_text_count(text)
    print('pi_list',pi_list)
    H = get_H(pi_list)
    print('char_count_dict:',char_count_dict)
    print('H:',H)
    # print(type(char_count_dict[0][0]))
    # 用频率构建叶子节点，返回节点对象列表
    nodes = create_nodes(char_count_dict)

    # 构建哈夫曼树，返回根节点
    root = create_huffman_tree(nodes)
    
    # 哈夫曼编码，返回平均码长
    average_code_length = huffman_encoding(nodes, root, pi_list,text)
    #for item in nodes:
    #    print(item.name,item.sign_str)
    # 对文本编码
    huffman_str = encode_str(text, nodes)
    # 对文本解码
    final_str = decode_str(huffman_str, nodes)
    efficiency = '{:.2%}'.format(H/average_code_length)
    print('Huffman编码结果:',huffman_str)
    print('Huffman译码结果:',final_str)
    print('Huffman编码效率:',efficiency)
