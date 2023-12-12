import transbigdata as tbd
import json
import requests

file = open('./data/config.json','r')
config = json.load(file)
file.close()
print(config)

def initial_trans_big_data():
    tbd.set_mapboxtoken(config["MapboxToken"])
    tbd.set_imgsavepath(config["mapPath"])
    return tbd

def get_routes(origin,destination,waypoints,departure_time):
    BaiduMapApiToken = config["BaiduMapApiToken"]

    # 百度地图API的开发者密钥
    ak = BaiduMapApiToken

    # 构造请求URL
    url = f"http://api.map.baidu.com/directionlite/v1/driving?origin={origin}&destination={destination}&waypoints={'|'.join(waypoints)}&tactics=0&departure_time={departure_time}&ak={ak}"

    # 发送请求
    response = requests.get(url)
    data = response.json()

    # 解析路线规划结果
    if data["status"] == 0:
        routes = data["result"]["routes"]
        return routes
    return data
