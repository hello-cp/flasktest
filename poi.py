# 高德地图驾车路径规划，获取两地点之间的驾车里程和时间
import random


class Poi:  # 景点详细信息
    name = '1'  # 景点名称
    location = []  # 景点经纬度
    address = ''  # 地址（路）
    rating = 1  # 评分
    photo = 'https://lbs.amap.com/api/webservice/guide/api/search'
    time = 1  # 不管


random_poi = dict()
# all_poi存放所有景点信息 字典
all_poi = {'洛阳老街': Poi(), '老君山': Poi(), '隋唐洛阳城国家遗址公园': Poi(), '白云山': Poi(), '王城公园': Poi(),
           '鸡冠洞': Poi(), '栾川重渡沟风景区': Poi(), '洛阳周王城天子驾六博物馆': Poi(), '洛阳博物馆': Poi(),
           '洛邑古城': Poi(),
           '丽景门景区': Poi(), '龙门石窟': Poi(), '白马寺': Poi(), }
poi = ['洛阳老街', '老君山', '隋唐洛阳城国家遗址公园', '白云山', '王城公园', '鸡冠洞', '栾川重渡沟风景区', '丽景门景区',
       '洛阳周王城天子驾六博物馆', '洛阳博物馆', '洛邑古城', '龙门石窟', '白马寺']

all_poi['洛阳老街'].name = '洛阳老街'
all_poi['洛阳老街'].location = [112.479198,34.681411]
all_poi['洛阳老街'].address = '老城区正义街(农校街小学东北侧约50米)'
all_poi['洛阳老街'].rating = 4.7
all_poi[
    '洛阳老街'].photo = 'https://ts1.cn.mm.bing.net/th/id/R-C.120e103ab3e02901fc033b1579060d45?rik=WsqCd2vUbZIhKg&riu=http%3a%2f%2fp3.ifengimg.com%2fa%2f2019_27%2f91cb2d552e5494d_size253_w600_h400.jpg&ehk=KA8EXCUyFl2%2fnRDgJ105wVZlfFpPPXKQ2FYgHNUAXKE%3d&risl=&pid=ImgRaw&r=0'
all_poi['洛阳老街'].time = 90

all_poi['老君山'].address = '栾川县鸾州大道南侧'
all_poi['老君山'].name = '老君山'  # 老君山风景名胜区
all_poi['老君山'].location = [111.657836,33.739153]
all_poi['老君山'].rating = 4.9
all_poi['老君山'].photo = 'https://img.zcool.cn/community/01ba4d5e295427a8012165188f8345.jpg@1280w_1l_2o_100sh.jpg'
all_poi['老君山'].time = 180

all_poi['隋唐洛阳城国家遗址公园'].address = '西宁区定鼎路与中州路交汇处'
all_poi['隋唐洛阳城国家遗址公园'].name = '隋唐洛阳城国家遗址公园'
all_poi['隋唐洛阳城国家遗址公园'].location = [112.455942,34.680804]
all_poi['隋唐洛阳城国家遗址公园'].rating = 4.4
all_poi[
    '隋唐洛阳城国家遗址公园'].photo = 'https://ts1.cn.mm.bing.net/th/id/R-C.22eb34d32c33620d3887d8193fd4804d?rik=RsjMyADgYm8WzQ&riu=http%3a%2f%2fdimg02.c-ctrip.com%2fimages%2ffd%2ftg%2fg1%2fM07%2f99%2fD6%2fCghzfFTF-eeAcngnAAFdov-eOF8051.jpg&ehk=8T3tRVN%2fMSU9wofLpJqHA3ThPKkne7i7HaZsh5fRzIs%3d&risl=&pid=ImgRaw&r=0'
all_poi['隋唐洛阳城国家遗址公园'].time = 50

all_poi['白云山'].address = '嵩县'
all_poi['白云山'].name = '白云山'
all_poi['白云山'].location = [111.841283,33.683911]
all_poi['白云山'].rating = 4.0
all_poi['白云山'].photo = 'https://p1.ssl.qhimg.com/t015154bc5acec1e38f.jpg'
all_poi['白云山'].time = 180

all_poi['王城公园'].address = '西工区中州中路312号'
all_poi['王城公园'].name = '王城公园'
all_poi['王城公园'].location = [112.421954,34.666010]
all_poi['王城公园'].rating = 4.8
all_poi[
    '王城公园'].photo = 'https://ts1.cn.mm.bing.net/th/id/R-C.20148610a0061cd33cef199120048871?rik=Igp%2b1HvaVOs8gw&riu=http%3a%2f%2fwww.cnzzzz.com%2fuploads%2fallimg%2f18%2f3-1PZ5091029209.jpg&ehk=mvMGLcaEHeFuhlGUF%2fUiEvpSS3Yu2TPvfuX0Yw%2buqxU%3d&risl=&pid=ImgRaw&r=0'
all_poi['王城公园'].time = 90

all_poi['鸡冠洞'].address = '栾川县城西3公里处'
all_poi['鸡冠洞'].name = '鸡冠洞'  # 洛阳鸡冠洞风景名胜区
all_poi['鸡冠洞'].location = [111.570571,33.783207]
all_poi['鸡冠洞'].rating = 4.8
all_poi['鸡冠洞'].photo = 'https://tse1-mm.cn.bing.net/th/id/OIP-C.WJ39M6m0nwXt1lp4uL0dhQHaE8?pid=ImgDet&rs=1'
all_poi['鸡冠洞'].time = 180

all_poi['栾川重渡沟风景区'].address = '栾川县潭头镇重渡村'
all_poi['栾川重渡沟风景区'].name = '栾川重渡沟风景区'
all_poi['栾川重渡沟风景区'].location = [111.733545,33.947952]
all_poi['栾川重渡沟风景区'].rating = 4.2
all_poi['栾川重渡沟风景区'].photo = 'https://tse1-mm.cn.bing.net/th/id/OIP-C.ta4pbAkj3E7Vd-Hnum-5KAHaEw?pid=ImgDet&rs=1'
all_poi['栾川重渡沟风景区'].time = 180

# all_poi['翠云峰森林公园'].name = '翠云峰森林公园'
# all_poi['翠云峰森林公园'].location = [112.454228, 34.709402]
# all_poi['翠云峰森林公园'].address = '老城区310国道附近'
# all_poi['翠云峰森林公园'].rating = 3.8
# all_poi['翠云峰森林公园'].photo = 'https://ts1.cn.mm.bing.net/th/id/R-C.7ddfb370cc3456fc5df52e87c77d45e8?rik=Nszv4icrwrSwdA&riu=http%3a%2f%2fpic118.huitu.com%2fres%2f20190427%2f1802427_20190427164641863070_1.jpg&ehk=B1mzrHA4zWW3KjBingOfobiBPqSq53Nk9G7KBD%2bwxzQ%3d&risl=&pid=ImgRaw&r=0'
# all_poi['翠云峰森林公园'].time = 1

all_poi['白马寺'].name = '白马寺'
all_poi['白马寺'].location = [112.604499,34.72122]
all_poi['白马寺'].address = '洛龙区洛白路6号'
all_poi['白马寺'].rating = 4.7
all_poi[
    '白马寺'].photo = 'https://ts1.cn.mm.bing.net/th/id/R-C.419a7d711d0d803b0c610ea2fc43d7ca?rik=q8XDjsLnK%2f2Aww&riu=http%3a%2f%2f5b0988e595225.cdn.sohucs.com%2fimages%2f20190723%2f4a6cb9a904d543829232be8d04f9feb6.JPG&ehk=6F7YlaVniOMLVfWR7MVLDkExRRFqzbluxkgEFOnpYNg%3d&risl=&pid=ImgRaw&r=0'
all_poi['白马寺'].time = 120

all_poi['洛阳周王城天子驾六博物馆'].name = '洛阳周王城天子驾六博物馆'
all_poi['洛阳周王城天子驾六博物馆'].location = [112.443146,34.674010]
all_poi['洛阳周王城天子驾六博物馆'].address = '中州中路226号'
all_poi['洛阳周王城天子驾六博物馆'].rating = 4.7
all_poi['洛阳周王城天子驾六博物馆'].photo = 'http://store.is.autonavi.com/showpic/9a9a7a1827188090ea176376a45f27e0'
all_poi['洛阳周王城天子驾六博物馆'].time = 60

all_poi['洛阳博物馆'].name = '洛阳博物馆'
all_poi['洛阳博物馆'].location = [112.451541,34.643323]
all_poi['洛阳博物馆'].address = '洛龙区文博路'
all_poi['洛阳博物馆'].rating = 4.9
all_poi[
    '洛阳博物馆'].photo = 'https://tse3-mm.cn.bing.net/th/id/OIP-C.rogoPucg7jDNkfitcF760QHaET?w=305&h=180&c=7&r=0&o=5&dpr' \
                          '=1.5&pid=1.7 '
all_poi['洛阳博物馆'].time = 76

all_poi['洛邑古城'].name = '洛邑古城'
all_poi['洛邑古城'].location = [112.485290,34.680390]
all_poi['洛邑古城'].address = '老城区九都东路与柳林街交叉口北侧'
all_poi['洛邑古城'].rating = 4.9
all_poi[
    '洛邑古城'].photo = 'https://tse1-mm.cn.bing.net/th/id/OIP-C.e73gIhippTZskwrqNlmNXgHaE8?w=295&h=197&c=7&r=0&o=5&dpr=1.5&pid=1.7'
all_poi['洛邑古城'].time = 88

all_poi['丽景门景区'].name = '丽景门景区'
all_poi['丽景门景区'].location = [112.471252,34.680899]
all_poi['丽景门景区'].address = '老城区西门口街与金业路交叉口东'
all_poi['丽景门景区'].rating = 4.9
all_poi[
    '丽景门景区'].photo = 'https://ts1.cn.mm.bing.net/th/id/R-C.884de9a187b5204dca37458b4c3fee52?rik=VGDM12JSBregFg&riu=http%3a%2f%2fimg95.699pic.com%2fphoto%2f50097%2f8697.jpg_wh860.jpg&ehk=39bNjlN2K%2bv320a5ELjHwc5ailXbOcy6okzDmzGNW08%3d&risl=&pid=ImgRaw&r=0'
all_poi['丽景门景区'].time = 180

all_poi['龙门石窟'].name = '龙门石窟'
all_poi['龙门石窟'].location = [112.476585,34.551832]
all_poi['龙门石窟'].address = '洛龙区老城区龙门石窟景区奉先寺附近'
all_poi['龙门石窟'].rating = 3.6
all_poi[
    '龙门石窟'].photo = 'https://ts1.cn.mm.bing.net/th/id/R-C.aa40667db180958011b3a064082eff71?rik=Bqy1uAn3mZTgZQ&riu=http%3a%2f%2fpic.kuaizhan.com%2fg1%2fM00%2f19%2f1F%2fCgpQU1kBHcuAWzHfAAHQiL2NXXo0565196&ehk=T70Y4MhWW3jWJHiqua%2bDbL56Q93GRPMUvgdr25xlM8w%3d&risl=&pid=ImgRaw&r=0'
all_poi['龙门石窟'].time = 60
