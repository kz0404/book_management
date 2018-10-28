from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from bookmanagement.service.factry_method.core import PondService
import logging

# Create your views here.
logger = logging.getLogger(__name__)


class TestIndexView(View):
    '''
    テスト用のView。
    ここから色々呼び出したりする。
    '''

    # logger.info('Running View')
    def get(self, request):
        logger.debug('os')

        print('aaa')
        return HttpResponse(200)


class FactoryMethodSample(View):
    '''
    FactoryMethodパターンの練習
    '''
    def get(self, request):
        logger.info('1')
        PondService.get_pond('Frog', 1)
        logger.info('9')
        return HttpResponse(200)


class AbstractFactorySample(View):
    '''
    AbstractFactoryパターンの練習
    '''
    def get(self):
        return HttpResponse(200)