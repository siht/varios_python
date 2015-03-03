class Partial(type):
    __methods = {}
    def __new__(meta, name, bases, dct):
        if not meta.__methods.has_key(name):
            meta.__methods.update({name:dct})
        else:
            meta.__methods[name].update(dct)
        return type.__new__(meta, name, bases, meta.__methods[name])

if __name__ == '__main__':
    print 'not run. :)'