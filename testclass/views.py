from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
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


