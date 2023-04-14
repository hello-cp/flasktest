import networkx as nx
import requests
from flask import Flask, render_template, request
import random
from poi import all_poi
import copy

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
# ===================================================全局变量
# 算法推荐的景点，内容是poi id
like_poi = dict()  # 我们推荐的景点
random_poi = dict()  # 随机出来的景点
final_poi = dict()  # 经用户增删后的最终景点
order = []  # 排序后的景点名字
coordinate = []  # final_poi景点坐标
nodes = []  # 排序前景点名
final = []
mapp = []


# ====================================================类
class Passenger:  # 访客
    type = []  # 访客选择的想去的景点类型
    meal = []  # 访客选择的喜欢的餐厅类型
    hotel = []  # 访客选择的酒店类型
    shopping = []  # 访客是否有购物需求


# ====================================================函数


def Get_poi(a):  # 推荐荐景    输出：like_poi
    for k in a:
        if k == '小吃街':
            like_poi.update({'洛阳老街': all_poi['洛阳老街']})
        if k == '名山大川':
            like_poi.update({'老君山': all_poi['老君山']})
            like_poi.update({'白云山': all_poi['白云山']})
            like_poi.update({'鸡冠洞': all_poi['鸡冠洞']})
            like_poi.update({'重渡沟旅游度假区': all_poi['重渡沟旅游度假区']})
        if k == '国家公园':
            like_poi.update({'隋唐洛阳城国家遗址公园': all_poi['隋唐洛阳城国家遗址公园']})
            like_poi.update({'王城公园': all_poi['王城公园']})
        if k == '博物馆':
            like_poi.update({'洛阳周王城王天子驾六博物馆': all_poi['洛阳周王城王天子驾六博物馆']})
            like_poi.update({'洛阳博物馆': all_poi['洛阳博物馆']})
        if k == '古城':
            like_poi.update({'洛阳古城': all_poi['洛阳古城']})
            like_poi.update({'丽景门': all_poi['丽景门']})
        if k == '滑雪':
            like_poi.update({'洛阳伏牛山滑雪度假乐园': all_poi['洛阳伏牛山滑雪度假乐园']})
        if k == '宗教色彩':
            like_poi.update({'龙门石窟': all_poi['龙门石窟']})
            like_poi.update({'白马寺': all_poi['白马寺']})
            like_poi.update({'香山寺': all_poi['香山寺']})


def Get_random():  # 随机景点
    ran = random.sample(range(0, 12), 6)
    print(ran)
    for i in ran:
        print(poi[i])
        random_poi.update({poi[i]: all_poi[poi[i]]})


def get_dis_tm(origin, destination):
    url = 'https://restapi.amap.com/v3/direction/driving?'
    key = '337ea1dcad974fab9c89957e165856fd'  # 这里就是需要
    link = '{}origin={}&destination={}&key={}'.format(url, origin, destination, key)
    response = requests.get(link)
    dis, tm = 999999, 999999
    if response.status_code == 200:
        results = response.json()
        if results['status'] == '1':
            dis = int(results['route']['paths'][0]['distance'])
            tm = int(results['route']['paths'][0]['duration'])
        else:
            print(link)
    return dis, tm


def Dijstrle(a):
    global final
    G = nx.Graph(my_g='my_graph')  # 无向图
    # final_poi = ['洛阳老街', '老君山', '隋唐洛阳城国家遗址公园', '白云山', '王城公园']
    final_poi = a
    nodes = []
    for k in final_poi:
        nodes.append(all_poi[k].name)
        coordinate.append(all_poi[k].location)
    print(coordinate)
    t = len(nodes)
    distance = []
    for i in range(0, t - 1):
        for j in range(i + 1, t):
            tt1 = str(coordinate[i][0])
            mm1 = str(coordinate[i][1])
            road1 = tt1 + ',' + mm1
            tt2 = str(coordinate[j][0])
            mm2 = str(coordinate[j][1])
            road2 = tt2 + ',' + mm2
            d, m = get_dis_tm(road1, road2)
            d = d / 1000
            a = [nodes[i], nodes[j], {'weight': d}]
            b = tuple(a)
            distance.append(b)
    G.add_nodes_from(nodes)
    G.add_edges_from(distance)

    final = copy.deepcopy(nodes)
    d = [0] * 20
    a = [0] * 20
    dmin = 99999
    print("最短路线：")
    for j in nodes:
        start = j
        l = copy.deepcopy(nodes)
        l.remove(start)
        t = len(l)

        for i in range(0, t - 1):
            end = l[i]
            temp = copy.deepcopy(l)
            print(end)
            temp.remove(end)
            a[i] = min([path  # 返回 key 为最小值的 path
                        for path in nx.all_simple_paths(G, source=start, target=end)  # gAnt 中所有起点为A、终点为E的简单路径
                        if all(n in path for n in temp)],  # 满足路径中包括顶点 B,C,D
                       key=lambda x: sum(G.edges[edge]['weight'] for edge in nx.utils.pairwise(x)))  # key 为加权路径长度

            d[i] = sum(G.edges[edge]['weight'] for edge in nx.utils.pairwise(a[i]))
            print(a[i])
            print(d[i])
            if (d[i] < dmin) & (i >= 0):
                dmin = d[i]
                print("最小值", dmin)
                final = a[i]
    print(final)
    vv = final
    for i in vv:
        mapp.append(all_poi[i].location)
    print(mapp)


# like_poi = {'龙门石窟': all_poi['龙门石窟'], '隋唐洛阳城国家遗址公园': all_poi['隋唐洛阳城国家遗址公园'],
#          '白马寺': all_poi['白马寺'], '王城公园': all_poi['王城公园'], '丽景门': all_poi['丽景门']}
#Dijstrle(like_poi)

def roadtime(a):
    lat = []
    order1 = []
    for k in a:
        lat.append(all_poi[k].location)
    i = len(lat)
    k = 0
    while i:
        tt = str(lat[k][0])
        mm = str(lat[k][1])
        road = tt + ',' + mm
        order1.append(road)
        i = i - 1
        k = k + 1

    t = 0
    i = len(lat) - 1
    while i:
        m, n = get_dis_tm(order1[t], order1[t + 1])
        i = i - 1
        t = t + 1
        return int(n/60)

#print("测试roadtime")
#final_poi = ['洛阳老街', '老君山', '隋唐洛阳城国家遗址公园', '白云山', '王城公园']
#roadtime(final_poi)


# ==========================================================================================路由
@app.route("/", methods=['GET', 'POST'])
def root():
    a = '公园'
    Get_poi(a)  # 第一遍推荐
    if request.method == 'GET':
        #Dijstrle()
        return render_template('map.html',order=mapp,final=final)  # 第一个界面，统计用户喜好
    elif request.method == 'POST':  # 输出：person属性值
        a = request.form.get('test')
        if a == '白马寺':
            return render_template('map.html')


@app.route("/home", methods=['GET', 'POST'])
def plan():
    if request.method == 'POST':  # 收到function.html提交的表单，根据用户选择的功能跳转不同的页面

        a = request.values.get('按钮一')  # 如果选择了按钮一，那么a=按钮一.value   如果没有选择 a=None if不会实现
        b = request.values.get('按钮二')
        c, d, e, f, = 1
        if a == '路径规划':  # /plan
            return render_template('a.html', like_poi=like_poi)
        if b == '景点查询':  # /poi  #琛琛
            return render_template('b.html')
        if c == '旅游盲盒':  # /blind   琛琛
            return render_template('c.html')
        if d == '热门路线':  # /classic   小黄
            return render_template('d.html')
        if e == '旅客游记':  # /journal  候姐
            return render_template('e.html')
        if f == '日程规划':  # /schedule    燕莉
            return render_template('f.html')


# =============================================================路径规划功能下所有路由
@app.route("/plan", methods=['GET', 'POST'])
def plann():  #
    1


# [{{[0]}},{{map[1]}},{{map[2]}},{{map[3]}},{{map[4]}}];
# =============================================================景点查询下所有路由
@app.route("/poi", methods=['GET', 'POST'])
def poi():  #
    if request.method == 'GET':
        order = [[112.477463, 34.558782], [112.457846, 34.634196], [112.448052, 34.635286], [112.421423, 34.666779],
                 [112.485290, 34.680390]]
        return render_template('map.html', order=order)  # 第一个界面，统计用户喜好
    elif request.method == 'POST':  # 输出：person属性值
        a = request.form
        if a['test'] == '嵖岈山风景区':
            return render_template('function.html')  # 功能页面【包括智能推荐】,表单提交到/home
        if a['test'] == '白马寺':
            return render_template('a.html')


# ===============================================================盲盒
@app.route("/blind", methods=['GET', 'POST'])
def blind():  #
    if request.method == 'GET':
        return render_template('a.html', random_poi=random_poi)


# ===============================================================热门路线
@app.route("/classic", methods=['GET', 'POST'])
def classic():
    return render_template('a.html')


@app.route("/classic/<int:num>", methods=['GET', 'POST'])
def classic_detail(num):
    if num == 1:
        return render_template('a洛阳全景4日路线.html')
    if num == 2:
        return render_template('a洛阳旅发委推荐4日线路.html')
    if num == 3:
        return render_template('a洛阳景点文化2日线路.html')
    if num == 4:
        return render_template('a洛阳周边赏秋2日线路.html')
    if num == 5:
        return render_template('a洛阳经典3日线路.html')
    if num == 6:
        return render_template('a洛阳孟津人文1日线路.html')
    if num == 7:
        return render_template('a洛阳古韵气息2日线路.html')
    if num == 8:
        return render_template('a洛阳自然之旅2日线路.html')
    if num == 9:
        return render_template('a洛阳博物馆文化之旅2日线路.html')


# =================================================================旅客游记
@app.route("/journal", methods=['GET', 'POST'])
def journal():  #
    1


# =================================================================日程规划
@app.route("/schedule", methods=['GET', 'POST'])
def schedule():  #
    1


# ==================================================================主函数
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
