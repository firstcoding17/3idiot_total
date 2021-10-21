import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#모집단 의료레벨 분류
def Main():
    medical = pd.read_csv('world_Life_expectancy.csv')
    pop_list = ['GHA', 'KOR', 'USA', 'IND']
    ratio = []
    for i in range(len(pop_list)):
        a = medical[medical['Country Code'] == pop_list[i]]
        ratio.append(int(a['2019']))
    labels = ['가나', '한국','미국','인도']


    print(ratio)







if __name__ == '__main__':
    Main()