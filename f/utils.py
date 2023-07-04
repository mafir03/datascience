import os
import pandas as pd
from datetime import datetime

def fileList(path):
    arr = os.listdir(path)
    return arr

def readCsv(path):
    return pd.read_csv(path)


def main():
    arr = fileList("rsc/")
    print(arr)

if __name__ == '__main__':
    main()
