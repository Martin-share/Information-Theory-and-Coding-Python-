'''
Descripttion: 
version: 
Author: Martin
FilePath: \Martin_Code\Python\信息论\bmp_huffman.py
Date: 2022-06-27 12:08:28
LastEditTime: 2022-07-01 10:46:28
'''

import math
from PIL import Image

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
def get_image_list_count(image_list):
    '''
    统计字符出现频率,返回一个字典和字符相应概率
    '''
    chars = []
    ret = []
    ret2 = []
    for char in image_list:
        #print(char)
        if char in chars:
            continue
        else:
            chars.append(char)
            ret.append((char, image_list.count(char)/len(image_list))) #直接计算相应字符的个数
    # print(chars)
    # print('ret',ret)
    for item in ret:
        ret2.append(item[1])
    # print('ret2',ret2)
    print('成功得到像素的字典和字符相应的概率')  
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
    print('成功构建Huffman树')
    return queue[0]

# 根据Huffman树，从下向上编码，返回哈夫曼的平均码长
def huffman_encoding(nodes, root,):
    average_code_length=0
    for node in nodes:
        temp_node = node     #递归的，改变的temp_node
        while temp_node != root:
            if temp_node.is_left(): # 判断是不是父节点的左节点
                node.sign_str = '0' + node.sign_str
            else:
                node.sign_str = '1' + node.sign_str
            temp_node = temp_node.father

    print('成功构建Huffman编码')

# 编码整个文本编码，返回编码结果
def encode_str(image_list, nodes,run_list,max_bin_len):
    '''编码整个文本编码，返回编码结果,并写入mul_encode.txt'''
    mul_str = ''
    mul_list = []
    for item in run_list:
        temp_list = []
        i=0
        for node in nodes:
            if item[0] == node.name:    # 字符匹配
                temp_list.append(node.sign_str)
                temp_list.append(item[1]-1)
                mul_list.append(temp_list)
            i+=1
    # print(mul_list)
    for item in mul_list:
        mul_str += item[0]
        mul_str += bin(item[1]).replace('0b','').rjust(max_bin_len,'0')
        #print(mul_str)
    with open(r'E:\Martin_Code\Python\信息论\mul_encode.txt','w') as fp:
        fp.write(mul_str)
    print('成功用Huffman和游程编码，并保存到mul_encode.txt')
    return mul_list,mul_str

# 解码整个字符串
def decode_str(mul_list, nodes):
    '''解码整个字符串,返回结果'''
    final_list = []
    for item in mul_list:  #从头开始解码
        for node in nodes:  #遍历节点列表
            if node.sign_str==item[0]:
                tmp = item[1]+1
                while(tmp>0):     
                    final_list.append(node.name)
                    tmp-=1
                break    
    with open(r'E:\Martin_Code\Python\信息论\after.txt','w') as fp:
        for item in final_list:
            fp.write(str(item))
    print('成功解码并写入after.txt')
    return final_list

# 求信源的的熵
def get_H(pi_list):
    '''求信源的的熵'''
    H = 0
    for i in range(len(pi_list)):
        H += pi_list[i] * math.log(pi_list[i], 2) * (-1)

    #print('信源熵：',H)
    return H

# 求平均码长
def get_average_length(run_list,nodes):
    average_length=1

    return average_length

# 获得图像的像素列表
def get_image_list(path):
    # print(path)
    im = Image.open(path)
    kuan = im.size[0]     #宽度，为后续等长码编码做准备
    max_bin_len = math.ceil(math.log(kuan,2))     #等长码用几位二进制
    #print(max_bin_len)
    try:
        image_list = list(x[0] for x in im.getdata()) #横着读
    except:
        image_list = list(im.getdata()) #横着读
    # print(image_list)
    with open(r'E:\Martin_Code\Python\信息论\before.txt','w') as fp: #存原图的像素点
        for item in image_list:
            fp.write(str(item))
    print('原图像的像素被存到before.txt')       
    # image_list = [127,127,127,127,127,121,123,123]
    # # kuan = 4
    # max_bin_len = 2

    '''游程编码，返回二维列表[['a',2]]'''
    run_list = []
    i=1
    index=1
    while(index<len(image_list)):
        if(index==(len(image_list)-1)): #读取到最后
            #最后两个相同
            if(image_list[index-1]==image_list[index]):
                if i==pow(2,max_bin_len):
                    #超出了
                    temp_list1 =[]
                    temp_list2 =[]
                    temp_list1.append(image_list[index-1])
                    temp_list1.append(i)
                    temp_list2.append(image_list[index])
                    temp_list2.append(1)
                    run_list.append(temp_list1)
                    run_list.append(temp_list2)
                else:
                    temp_list =[]
                    temp_list.append(image_list[index-1])
                    temp_list.append(i+1)
                    run_list.append(temp_list)
            #最后两个不同
            else:                          
                temp_list1 =[]
                temp_list2 =[]
                temp_list1.append(image_list[index-1])
                temp_list1.append(i)
                temp_list2.append(image_list[index])
                temp_list2.append(1)
                run_list.append(temp_list1)
                run_list.append(temp_list2)
            break
        # 非最后，要判断是否超出二进制表示的最大数
        # 如果一行全同
        elif i==pow(2,max_bin_len):
            temp_list =[]
            temp_list.append(image_list[index-1])
            temp_list.append(i)
            run_list.append(temp_list)
            i=1
            index+=1
        # 不同则截断
        elif(image_list[index-1]!=image_list[index]):
            temp_list =[]
            temp_list.append(image_list[index-1])
            temp_list.append(i)
            run_list.append(temp_list)
            i=1
            index+=1
        else:#相同继续累加
            i+=1
            index+=1

        #print(run_list)
    
    # print(run_list)
    print('成功得到像素列表和游程编码表')
    # 判断最多有几个连续值，缩小码长
    # 如果直接8位，注释掉return 之前的
    max_num = 0
    for item in run_list:
        if item[1]>max_num:
            max_num = item[1]
            
        else:
            continue
    # 不用8位
    #print(max_num)
    if max_num < kuan:
        max_bin_len = math.ceil(math.log(max_num,2))     #等长码用几位二进制
    print('max_bin_len',max_bin_len)
    return image_list,run_list,max_bin_len

# 比对解码结果是否正确
def compare(path,final_list,image_list):
    if (final_list!=image_list):
        print('两次不一致')
    else:
        print('两次一致')
        # 生成图像
        im = Image.open(path)
        size_a = im.size[0]  #原图像宽
        size_b = im.size[1]  #原图像高
        print(size_a,size_b)
        pic = Image.new(mode='L',size=(size_a,size_b)) 
        # pim = im.load()
        idex = 0
        #print(final_list[0],final_list[1])
        for i in range(size_b):
            for j in range(size_a):
                pic.putpixel([j,i],final_list[idex]) #
                #print(final_list[idex])
                idex+=1
        pic.show()
        pic.save(r'E:\Martin_Code\Python\信息论\after_lennag.bmp')
        print('图像被还原after_lennag.bmp')


def main(path):
    
    # 得到像素列表和游程编码列表,等长码用几位二进制
    image_list,run_list,max_bin_len = get_image_list(path)
    #print('run_list',run_list)
    
    # 统计字符出现频率,返回一个字典和概率
    char_count_dict,pi_list = get_image_list_count(image_list)
    # print('char_count_dict',char_count_dict)
    # 用频率构建叶子节点，返回节点对象列表
    nodes = create_nodes(char_count_dict)
    # 构建哈夫曼树，返回根节点
    root = create_huffman_tree(nodes)
    # 哈夫曼编码，
    huffman_encoding(nodes, root)
    # nodes.sort(key=lambda item:item.name)
    # for node in nodes:
    #     print(node.name,node.sign_str)
    # 对文本编码
    mul_list,mul_str = encode_str(image_list, nodes,run_list,max_bin_len)
    #print('mul_list',mul_list)
    #print('mul_str',mul_str)
    # 解码
    final_list = decode_str(mul_list, nodes)
    # print('final_list',final_list)
    # final_list->final_str
    final_str = ''
    for item in final_list:
        final_str +=str(item)
    # 生成图片并比较
    compare(path,final_list,image_list)

    H = get_H(pi_list)
    average_length = get_average_length(run_list,nodes)
    print('H',H)
    print('average_length',average_length)
    efficiency = '{:.2%}'.format(H/average_length)
    return image_list,nodes,mul_str,final_str,efficiency

if __name__ == '__main__':
    # 得到像素列表和游程编码列表,等长码用几位二进制
    path = 'E:/Martin_Code/Python/信息论/before_lennag1.bmp'
    print(path)

    image_list,run_list,max_bin_len = get_image_list(path)
    #print('run_list',run_list)
    print('max_bin_len',max_bin_len)
    # 统计字符出现频率,返回一个字典和概率
    char_count_dict,pi_list = get_image_list_count(image_list)
    # print('char_count_dict',char_count_dict)
    # 用频率构建叶子节点，返回节点对象列表
    nodes = create_nodes(char_count_dict)
    # 构建哈夫曼树，返回根节点
    root = create_huffman_tree(nodes)
    # 哈夫曼编码，
    huffman_encoding(nodes, root)
    # nodes.sort(key=lambda item:item.name)
    # for node in nodes:
    #     print(node.name,node.sign_str)
    # 对文本编码
    mul_list,mul_str = encode_str(image_list, nodes,run_list,max_bin_len)
    #print('mul_list',mul_list)
    #print('mul_str',mul_str)
    # 解码
    final_list = decode_str(mul_list, nodes)
    # print('final_list',final_list)
    
    # 生成图片并比较
    compare(path,final_list,image_list)

    H = get_H(pi_list)
    average_length = get_average_length(run_list,nodes)
    print('H',H)
    print('average_length',average_length)
