import random


class Car(object):
    def run(self):
        print 'car run run run!'


class SportsCar(Car):
    def run(self):
        print "I'm Sports Car"
        super(SportsCar, self).run()


class Tricycle(Car):
    def run(self):
        print "I'm Tricycle Car"
        super(Tricycle, self).run()


if __name__ == "__main__":
    # So u can run the same method, just make sure the object is inherited from the car.
    objs = [SportsCar, Tricycle]
    unknow_obj = random.choice(objs)
    unknow_obj().run()
