import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#한국 가계 부채 데이터 별로 없어서 보고 만듬
def Main():
    #금융부채만
    all = [5041,5539,5755,6050]
    seoul = [5609,5900,6196,6392]
    label= [2017,2018,2019,2020]

    x= np.arange(4)

    plt.bar(x,all,color='red',width=0.2)
    plt.bar(x+0.2,seoul,color='blue',width=0.2)
    plt.xticks(x,label)
    plt.title('가계 부채(금융부채)')
    plt.ylim(0,8000)
    plt.show()

    #총소득
    all = [5478,5705,5828,5924]
    seoul = [6172,6495,6595,6575]
    label= [2017,2018,2019,2020]

    x= np.arange(4)

    plt.bar(x,all,color='red',width=0.2)
    plt.bar(x+0.2,seoul,color='blue',width=0.2)
    plt.xticks(x,label)
    plt.title('총 소득')
    plt.ylim(0,8000)
    plt.show()












if __name__ == '__main__':
    Main()