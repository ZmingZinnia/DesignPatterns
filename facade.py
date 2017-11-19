import time

SLEEP = 0.5

class T1:
    def run(self):
        print  'Test 1'
        time.sleep(SLEEP)
        print 'do for Test 1'
        time.sleep(SLEEP)
        print 'Done for Test 1'

class T2:
    def run(self):
        print  'Test 2'
        time.sleep(SLEEP)
        print 'do for Test 2'
        time.sleep(SLEEP)
        print 'Done for Test 2'

class T3:
    def run(self):
        print  'Test 3'
        time.sleep(SLEEP)
        print 'do for Test 3'
        time.sleep(SLEEP)
        print 'Done for Test 3'

class Runner:
    def __init__(self):
        self.tests = [i for i in (T1(), T2(), T3())]

    def runALL(self):
        [i.run() for i in self.tests]

def main():
    runner = Runner()
    runner.runALL()


if __name__ == '__main__':
    main()
