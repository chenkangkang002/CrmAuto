'''
文件处理-提取数据
'''
import csv
import random

import xlrd


def get_txt(file_name='./data_text.txt',x='0'):
    '''
    解析txt文件，获取文件数据
    :param file_name: 文件路径
    :param x: 数据选择参数，默认0，随机，其他列表
    :return: x='0'为一维列表，其他为数据行组成的二维列表
    '''
    with open(file_name, 'r+', encoding='utf-8') as file:
        lines = file.readlines()    #读取文件所有数据
        #循环取出数据并放在一个新的list里面
        datas = []
        file_len = len(lines)
        if x == '0':    #随机
            rand = random.randint(0, file_len - 1)
            # lines[rand].replace('n', '')
            datas = lines[rand].split()
        else:   #数字列表,全部输出
            for line in lines:
                # line.replace('n','')
                datas.append(line.split())
        return datas

# file_path = r'E:\PyCharm2020(64bit)\py_workspace\ecshop\data\data_text.txt'
# datas = get_txt(file_path)
# print(datas)

def get_csv(file_name='./data_csv.csv'):
    '''解析csv文件，获取文件数据'''
    with open(file_name, 'r+', encoding='utf-8') as file:
        data_csv = csv.reader(file)
        datas = []
        for data in data_csv:
            datas.append(data)
        return datas

def get_excel(file_name='./data_excel.xls',sheet=0):
    '''解析excel文件，获取文件数据'''
    data = xlrd.open_workbook(file_name) #获取整个表格的信息
    sheets = data.sheet_by_index(sheet)
    # print('sheets',sheets)
    # # sheets = data.sheet_by_name(sheet)  #获得对应工作簿的信息
    row_values = sheets.row_values(0)   #获得行数据
    col_values = sheets.col_values(0)
    cell_a1 = sheets.cell(1,0).value    #通过行和列获取单元格的值
    row = sheets.row(2)  #获取整行
    nrows = sheets.nrows    #得到所有的行数
    ncols = sheets.ncols    #得到所有的航速
    datas = []
    for index in range(1,nrows):
        #利用循环将得到的每一行数据添加到一个新的list
        datas.append(sheets.row_values(index))
    return datas


