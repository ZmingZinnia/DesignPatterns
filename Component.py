class Component(object):
    def __init__(self, name):
        self.childs = []
        self.name = name

    def get_name(self):
        return self.name

    def display(self):
        pass

    def add(self, obj):
        pass

    def remove(self, obj):
        self.childs.remove(obj)


class File(Component):
    def display(self):
        return self.name

    def add(self):
        pass

    def remove(self):
        pass


class Folder(Component):
    def display(self):
        return [tmp.get_name() for tmp in self.childs]

    def add(self, name, is_folder):
        tmp = None
        if is_folder:
            tmp = Folder(name)
        else:
            tmp = File(name)
        self.childs.append(tmp)

    def remove(self, name):
        for child in self.childs():
            if child.get_name() == name:
                self.childs.remove(child)


def main():
    f = Folder('note')
    f.add('text', False)
    f.add('work', True)
    print f.display()

if __name__ == '__main__':
    main()
