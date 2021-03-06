class Signal(object):
    def __init__(self):
        self.__handlers = []

    def __iadd__(self, handler):
        if handler not in self.__handlers:
            self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        if handler in self.__handlers:
            self.__handlers.remove(handler)
        return self

    def dispatch(self, *args, **keywargs):
        for handler in self.__handlers:
            handler(*args, **keywargs)

    def removeAllListeners(self, inObject):
        for theHandler in self.__handlers:
            if theHandler.im_self == inObject:
                self -= theHandler
