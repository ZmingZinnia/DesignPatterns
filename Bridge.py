class Api_one(object):
    def run(self, test):
        print "I'm one, test: %s" % test

class Api_two(object):
    def run(self, test):
        print "I'm two, test: %s" % test

class Some_Bridge(object):
    def __init__(self, text, api):
        self._text = text
        self._api = api

    def run(self):
        self._api.run(self._text)

    def change(self, text_ext):
        self._text += text_ext

def main():
    objects = [Some_Bridge('hello', Api_one()),
               Some_Bridge('hello', Api_one())]

    for obj in objects:
        obj.change(". I'm bridger")
        obj.run()

if __name__ == "__main__":
    main()
