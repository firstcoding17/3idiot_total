import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#전세계 의료레벨 분류
def Main():
    medical = pd.read_csv('world_Life_expectancy.csv')
    over_85 = 0
    over_80 = 0
    over_75 = 0
    over_70 = 0
    over_65 = 0
    over_60 = 0
    over_55 = 0
    under_55 = 0
    nan = 0
    for i in range(0,len(medical)):
        if medical['2019'][i] >=85:
            over_85+=1
        elif medical['2019'][i]  < 85 and medical['2019'][i]  >= 80:
            over_80+=1
        elif medical['2019'][i] < 80 and medical['2019'][i] >= 75:
            over_75+=1
        elif medical['2019'][i] < 75 and medical['2019'][i] >= 70:
            over_70+=1
        elif medical['2019'][i] < 70 and medical['2019'][i] >= 65:
            over_65+=1
        elif medical['2019'][i] < 65 and medical['2019'][i] >= 60:
            over_60+=1
        elif medical['2019'][i] < 60 and medical['2019'][i] >= 55:
            over_55+=1
        elif medical['2019'][i] < 55:
            under_55+=1
        else:
            nan+=1
    ratio = [(over_85/len(medical)*100.0),(over_80/len(medical) * 100.0),(over_75/len(medical)*100.0),
             (over_70/len(medical)*100.0),(over_65/len(medical)*100.0),(over_60/len(medical)*100.0),(over_55/len(medical)*100.0),(under_55/len(medical)*100.0),
    (nan/len(medical)*100.0)
             ]


    labels = ['8등급','7등급','6등급','5등급','4등급','3등급','2등급','1등급','데이터 없음']
    plt.pie(ratio,labels=labels,autopct='%.1f%%', startangle = 260, counterclock=False, shadow=True)
    plt.show()
    print(ratio[8])










if __name__ == '__main__':
    Main()






