#!/usr/bin/python3
 
import json
 
# Python 字典类型转换为 JSON 对象
data = {
    'fn' : 'Ezio',
    'ln' : 'Auditore',
    'age' : '20',
    'sex' : 'm',
    'income' : '100000',
}
 
json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)
