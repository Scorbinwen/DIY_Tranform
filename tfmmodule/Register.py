class Register():
    def __init__(self):
        self.register_dict ={}

    def Register_Module(self,cls):

        name = cls.__name__
        assert name not in self.register_dict,\
            ["Class {} is already registered!".format(name)]
        self.register_dict[name]=cls
        return cls

tfmreg = Register()