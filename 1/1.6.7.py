class SingletonFive:
    count = 1
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.count <= 5:
            cls.count += 1
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
