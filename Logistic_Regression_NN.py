# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:56:37 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from lr_utils import load_dataset

train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = 
    load_dataset()
