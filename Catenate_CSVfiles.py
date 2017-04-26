# -*- coding: utf-8 -*-
import os
import glob
import pandas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def concatenate():
    os.chdir(" ")
    fileList=glob.glob("*.csv")
    muluFiles = []
    for filename in fileList:
        print(filename)
        df = pandas.read_csv(filename,low_memory=False)
        muluFiles.append(df)
    return muluFiles

muluFiles = concatenate()
print("data brung, now showing data ...")

df = pd.DataFrame(muluFiles)