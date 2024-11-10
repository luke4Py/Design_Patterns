

class Singleton():

    __instance__ = None

    def __init__(self):
        if Singleton.__instance__ is None:
            Singleton.__instance__=self
        else:
            raise Exception('You cannot create another singleton class')


x = Singleton()

Singleton.__instance__

y = Singleton()