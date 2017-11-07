class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

    def __str__(self):
        return self.state

class YourBorg(Borg):
    pass

if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'First'
    print Borg._shared_state
    rm2.state = 'Second'

    print Borg._shared_state

    print 'rm1:%s' % rm1
    print 'rm2:%s' % rm2

    rm2.state = 'Boss'

    print 'rm1:%s' % rm1
    print 'rm2:%s' % rm2

    print 'rm1 id:%s' % id(rm1)
    print 'rm2 id:%s' % id(rm2)

    rm3 = YourBorg()

    print 'rm1:%s' % rm1
    print 'rm2:%s' % rm2
    print 'rm3:%s' % rm3
