

import json
from copy import deepcopy

dict1=json.load(open('standalone_operators2.json',encoding='utf-8'))
# print(dict1)
dict2=json.load(open('standalone_operators1.json',encoding='utf-8'))
# print(dict2)

dict3= deepcopy(dict1)

for key in dict2.keys():
    # print(key)
    if key in dict3:
        dict3.update(dict2[key])
    else:
        dict3[key]=dict2[key]


dict3=json.dumps(dict3,ensure_ascii=False,sort_keys=False, indent=4, separators=(',', ': '))

print(dict3)
# with open('aa.json','w',encoding='utf-8') as f:
#     f.write(dict3)

