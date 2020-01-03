# import json
# info_dict = {'name': 'Joe', 'age': 20, 'job': 'driver'}
# # dumps 将数据转换成字符串
# info_json = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '))
# # 显示数据类型
# print(type(info_json))
# f = open('info.json', 'w')
# f.write(info_json)

import json
import copy
from copy import deepcopy

dict1=json.load(open('faa1.json',encoding='utf-8'))
# print(dict1)
dict2=json.load(open('faa2.json',encoding='utf-8'))
# print(dict2)

# dict3= deepcopy(dict1)
#
# for key in dict2.keys():
#     # print(key)
#     if key in dict3:
#         dict3.update(dict2[key])
#     else:
#         dict3[key]=dict2[key]


# dict3=dict(dict1,**dict2)
dict3=copy.copy(dict1)
print(dict2['preprocess']['subcategory']['1111'])
# print(dict3)

dict3['preprocess']['subcategory'].update(dict2['preprocess']['subcategory']['1111'])
# dict3['preprocess']['subcategory']['1111']=dict2['preprocess']['subcategory']['1111']
# for key in dict3.keys():
#     if key in dict1:
#         dict3[key]=dict(dict3[key],**dict1[key])


dict3=json.dumps(dict3,ensure_ascii=False,sort_keys=False, indent=4, separators=(',', ': '))
# # dict3=json.dumps(dict3,sort_keys=False)
# print(dict3)
with open('faa3.json','w',encoding='utf-8') as f:
    f.write(dict3)

