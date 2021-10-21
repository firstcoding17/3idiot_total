import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib.ticker as ticker
import numpy as np
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#고용률
def Main():
    data = pd.read_csv('고용률.csv')
    #금융부채만
    ylabel = list(data['실업률'])
    xlabel = ['201801', '201802', '201803', '201804', '201805', '201806', '201807', '201808', '201809', '01810', '201811', '201812', '201901', '201902', '201903', '201904', '201905',
              '201906', '201907', '201908', '201909', '201910', '201911', '201912', '202001', '202002', '202003', '202004', '202005',
              '202006', '202007', '202008', '202009', '202010', '202011', '202012', '202101', '202102', '202103', '202104', '202105', '202106', '202107', '202108', '202109']
    x = np.arange(len(xlabel))
    print(xlabel)

    plt.bar(x,ylabel)
    plt.xticks(x,xlabel)
    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(15))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
    plt.title('서울 실업률')

    plt.show()













if __name__ == '__main__':
    Main()