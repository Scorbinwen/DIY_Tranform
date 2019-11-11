from .Register import tfmreg
from PIL.Image import Image
import PIL
import numpy as np
import cv2
import torchvision.transforms as transforms

# A transform example
@tfmreg.Register_Module
class Rotate():
    """
    Rotate the image by the degree.
    Args:
        Refer to transforms
        Luckily you can implement your own Rotate on your demand.
    """
    def __init__(self,degree, resample=False, expand=False, center=None):
        self.degree = degree
        self.resample = resample
        self.expand = expand
        self.center = center


    def __call__(self,inp):
        """
        :param inp:
            type:either PIL.image or numpy
        :return:
        """
        out = None

        if isinstance(inp,Image):
            tfm = transforms.RandomRotation(self.degree,self.resample,self.expand,self.center)
            out = tfm(inp)
        elif isinstance(inp,np.ndarray):
            inp = PIL.Image.fromarray(inp.astype('uint8'), 'RGB')
            tfm = transforms.RandomRotation(self.degree, self.resample, self.expand, self.center)
            out = tfm(inp)
            out = np.asarray(out)
        else:
            print("Expected type of inp should be either"
                  " PIL.Image.Image or np.ndarray,got {}".format(type(inp)))
        return out

