from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .mongodb import mongo
from .mafengwo import MafengwoSpider

# Create your views here.


def index(request):
    # print('*'*100)
    return render(request, 'view.html')


# /echarts/<city>
class Mafengwo(APIView):
    def get(self, request, city):
        # 获取城市的景点数据
        # print(city)
        count = mongo.find_scenic_count(city=city)
        # print("********" + str(count))

        if not count:
            # 创建指定城市的爬虫,抓取需要的数据
            print("*"*10)
            MafengwoSpider(city).run()

        data = mongo.find_scenics(city)

        return Response(data)