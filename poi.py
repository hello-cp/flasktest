import json
import math
import requests

import os

### 需要获取高德地图的key

key = ['337ea1dcad974fab9c89957e165856fd']
area_code = {'驻马店': 411700}
area_road = {'驻马店': []}


def get_road(area: str, page: int):
    data = []  # 保存指定区域的道路名称
    parameters = {'key': key[0], 'keywords': '嵖岈山', 'city': '驻马店', 'citylimit': 'true', 'offset': 1,
                  'page': page, 'extensions': 'all', 'output': 'JSON'}
    res = requests.get('https://restapi.amap.com/v3/place/text?', params=parameters)
    json_dict = json.loads(res.text)
    poi_list = json_dict['pois']
    count = json_dict['count']  # 当前区域道路个数
    for poi in poi_list:
        data.append(poi['location'])
        print(data)
    return count, data


count, data = get_road('驻马店', 1)
print("count : ", count)
print("data : ", data)
for i in data:
    location = i