import requests

import asyncio
import aiohttp

import itertools

from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Shop, Address, Coordinates
from .serializers import AddressSerializer, CoordinatesSerializer
from . import services
from .services import service_address, service_coordinate, service_parse_location, service_search_parser

class AddressView(APIView):
    
    def get(self, request, format=None):
        # print(services.service_address)
        # service_address.parser_address_moyo()
        # service_address.parser_address_allo()
        # service_address.parser_address_foxtrot()
        
        queryset = Address.objects.all()
        serializer_class = AddressSerializer(queryset, many=True)
        return Response(serializer_class.data)

class CoordinatesView(APIView):

    def get(self, request, format=None):
        service_coordinate.parse_coordinates()

        queryset = Coordinates.objects.all()
        serializer_class = CoordinatesSerializer(queryset, many=True)
        return Response(serializer_class.data)

class ParseLocationView(APIView):

    # def get(self, request):
    #     print(request)
    
    def get(self, request):
        # СДЕЛАТЬ ОБРАБОТКУ ОШИБОК
        # ПРОВЕРИТЬ SHOP_LIST НА ДУБЛИКАТЫ
        # ЕСЛИ ВВЕДЕНО НЕКОРРЕКТНОЕ НАЗВАНИЕ
        # ЕСЛИ ПРИШЁЛ НЕУСПЕШНЫЙ ОТВЕТ ПРИ ЗАПРОСЕ
        # ЕСЛИ ОШИБКА ВОЗНИКЛА ВО ВРЕМЯ ПАРСИНГА (НЕ ТОТ КЛАСС И Т.Д.)
        # протестировать различные ключи запросов (Apple, Apple X, note 9)
        
        # test_coord = { 
        #     'lat': 50.0062302,
        #     'lng': 36.2343553 
        # }
        # nearest_address = service_parse_location.parse_location(test_coord)
        # list_address = [i[0] for i in nearest_address]
        # shop_list = [4]

        # for point in list_address:
            # address = Address.objects.filter(id=point).values_list('shop_id_id')
        #     shop_list.append(address[0][0])
        
        
        #  dataSource = [
        #     'Address', [ { 'address', 'shop' } ]
        #     'Records': [ {'Products ...'} ]
        # ]

        query = 'apple'
        shop_list = [2,4,5]
        shop_requests = []
        
        for shop_id in shop_list:
            search_request = Shop.objects.filter(id=shop_id).values_list('search_request')
            shop_info = [shop_id, search_request[0][0]]
            shop_requests.append(tuple(shop_info))
        
        def call_url(shop):
            request_query = shop[1] + 'samsung note 9'
            response = service_search_parser.parse_shop(shop[0], request_query)
            return response

        futures = [call_url(shop) for shop in shop_requests]
        flat_structure = list(itertools.chain.from_iterable(futures))

        return Response(flat_structure)

