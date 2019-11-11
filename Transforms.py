from tfmmodule import tfmreg
import numpy as np
print(tfmreg.register_dict["Rotate"])
class Transform():

    def __init__(self,transforms):
        self.transforms = transforms
        assert isinstance(transforms,dict),\
            ["Expected type of transforms is list,got {}.".format(type(transforms))]


    def __call__(self,inp):
        out = None

        for (tfm_name,tfm_params) in self.transforms.items():
            # print(item)
            # tfm_name,tfm_params = item.items()
            assert tfm_name in tfmreg.register_dict,\
                ["Class {} not found!".format(tfm_name)]
            assert isinstance(tfm_params,(list,dict)),\
                ["Expected type of tfm_params is either list or dict,got {}.".format(type(tfm_params))]

            tfmcls = tfmreg.register_dict[tfm_name]
            if isinstance(tfm_params,list):
                transf = tfmcls(*tfm_params)
                out = transf(inp)
            else:
                transf = tfmcls(**tfm_params)
                out = transf(inp)

        return out


# Define transform operations
tfmDict = dict(
    Rotate= dict(degree=5)
)

inp = np.zeros((256,256,3))

# Instantiate transforms
transforms = Transform(tfmDict)

# Execute transforms
out = transforms(inp)


print(out)


