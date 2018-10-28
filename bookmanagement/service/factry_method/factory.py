import logging

logger = logging.getLogger('testclass')


class Pond(object):
    '''
    試しにFactoryMethodを作ってみる
    '''

    def __init__(self,
                 number_animals,
                 animal_class,
                 number_plants=0,
                 plant_class=None):
        self.animal_class = animal_class
        self.plant_class = plant_class

        self.animals = []
        logger.info('3')
        for i in range(number_animals):
            logger.info('4')
            animal = self.new_organism("animal", "動物%d" % (i,))
            logger.info('7')
            self.animals.append(animal)

        self.plants = []
        for i in range(number_plants):
            logger.info('4')
            plant = self.new_organism("plant", "植物%d" % (i,))
            logger.info('7')
            self.plants.append(plant)

    def new_organism(self, itr_type, name):
        if itr_type == "animal":
            return self.animal_class(name)
        elif itr_type == "plant":
            return self.plant_class(name)

    def simulate_one_day(self):
        logger.info('8')
        for animal in self.animals:
            animal.eat()
            animal.speak()
            animal.sleep()

    def new_animal(self, name):
        raise NotImplementedError


class Frog(object):
    """Frog object"""
    def __init__(self, name):
        self.name = name

    def eat(self):
        logger.debug("カエルは(%s)食事をしています。" % (self.name,))

    def speak(self):
        logger.debug("カエルは(%s)ゲコゲコ鳴いています。" % (self.name,))

    def sleep(self):
        logger.debug("カエルは(%s)寝ています。" % (self.name,))


class Duck(object):
    """アヒルobject"""
    def __init__(self, name):
        self.name = name
        logger.info('6')

    def eat(self):
        logger.debug("アヒルは(%s)食事をしています。" % (self.name,))

    def speak(self):
        logger.debug("アヒルは(%s)ガーガー鳴いています。" % (self.name,))

    def sleep(self):
        logger.debug("アヒルは(%s)寝ています。" % (self.name,))
