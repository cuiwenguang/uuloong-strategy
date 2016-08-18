# This file device_model is created by lincan for Project uuloong-strategy
# on a date of 8/11/16 - 2:04 PM

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


class DeviceModelEnum:
    DeviceModeliOS = 0
    DeviceModelAndroid = 1


class DeviceModel:
    model = ""

    def __init__(self, model):
        self.model = model
        if self.model is "iphone":
            self.model_enum = DeviceModelEnum.DeviceModeliOS
        else:
            self.model_enum = DeviceModelEnum.DeviceModelAndroid

    @property
    def enum(self):
        return self.model_enum
