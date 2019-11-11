# DIY_Tranform
DIY your transformation for your own dataset

## Write Transformation
For DIY your own transformation,you can write your customized transformation(e.g. Rotate) under the tfmmodule module.
An example is given as tfmmodule/Rotate.

## Make Transformation Config
Make the config(i.e. a dict-wise sequence of transformation).
Refer to Transformation.py.

## Run the transformation
Example:
```
# Define transform operations(i.e. Config)
tfmDict = dict(
    Rotate= dict(degree=5)
)

inp = np.zeros((256,256,3))

# Instantiate transforms
transforms = Transform(tfmDict)

# Execute transforms
out = transforms(inp)

```
