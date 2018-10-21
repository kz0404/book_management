from django.shortcuts import render
from django.views import View
import logging

# Create your views here.
logger = logging.Logger(__name__)


class TestIndexView(View):
    '''
    テスト用のView。
    ここから色々呼び出したりする。
    '''

    logger.info('Running View')
