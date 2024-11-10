class Encap():

    def __init__(self, name, age) -> None:
        self.__name = name #Private variable
        self.__age = age #Private variable
        self._gender = 'Male' #Protected Variable

    def get_name(self):
        return self.__name

obj1 = Encap('Luke', 27)

obj1.get_name()

obj1.__name #Result in error 
obj1._gender #doesnt result in error



