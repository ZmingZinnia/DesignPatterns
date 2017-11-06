
class SportsCar(object):
    def fly(self):
        print "I'm fly, to catch me"

class Tricycle(object):
    def climb(self):
        print "I'll catch you. Don't run."


class Adapter(object):
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

def main():
    objects = [SportsCar(), Tricycle()]
    adapted = []
    for obj in objects:
        if isinstance(obj, SportsCar):
            adapted.append(Adapter(obj, dict(run=obj.fly)))
        elif isinstance(obj, Tricycle):
            adapted.append(Adapter(obj, dict(run=obj.climb)))
    
    for car in adapted:
        car.run()
    


if __name__ == "__main__":
    main()
