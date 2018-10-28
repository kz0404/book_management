

import logging
from bookmanagement.service.factry_method.factory import Duck, Frog, Pond
logger = logging.getLogger('testclass')


class PondService(object):
    @classmethod
    def get_pond(cls, kind_animal, number):
        logger.debug('get_pond')
        pond = []
        if kind_animal == 'Frog':
            pond = Pond(number, Frog)
        elif kind_animal == 'Duck':
            logger.info('2')
            pond = Pond(number, Duck)
        if hasattr(pond, 'simulate_one_day'):
            pond.simulate_one_day()
