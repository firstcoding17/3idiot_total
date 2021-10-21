import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#코로나 확진자와 사망자 그리고 접종률
def Main():
    covid = pd.read_csv('owid-covid-data.csv')


    pop_list = ['GHA', 'KOR', 'USA', 'IND']
    covid_world = covid[covid['location'] == 'World']
    covid_GHA = covid[covid['iso_code'] == 'GHA']
    covid__KOR = covid[covid['iso_code'] == 'KOR']
    covid_USA = covid[covid['iso_code'] == 'USA']
    covid_IND = covid[covid['iso_code'] == 'IND']


    #전세계 확진자 수 사망자수 1당 100만
    world_case = list(covid_world['total_cases_per_million'])
    world_deaths = list(covid_world['total_deaths_per_million'])
    world_date = list(covid_world['date'])
    print(world_case)
    print(world_deaths)

    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))



    plt.plot(world_date,world_case,color='blue')

    plt.title('전세계 확진자 증가 추세')
    plt.show()
    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(world_date,world_deaths,color='red')
    plt.title('전세계 코로나 사망자 증가 추세')
    plt.show()
    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(world_date,world_case,color='blue')
    plt.plot(world_date,world_deaths,color='red')
    plt.title('전세계 확진자와 사망자 추세')
    plt.show()

    #가나 확진자 사망자

    GHA_case = list(covid_GHA['total_cases_per_million'])
    GHA_deaths = list(covid_GHA['total_deaths_per_million'])
    GHA_date = list(covid_GHA['date'])



    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
    plt.plot(GHA_date,GHA_case,color='blue')
    plt.title('가나 확진자 증가 추세')
    plt.show()
    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
    plt.plot(GHA_date,GHA_deaths,color='red')
    plt.title('가나 사망자 증가 추세')
    plt.show()

    #한국 확진자 사망자

    KOR_case = list(covid__KOR['total_cases_per_million'])
    KOR_deaths = list(covid__KOR['total_deaths_per_million'])
    KOR_date = list(covid__KOR['date'])
    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))




    plt.plot(KOR_date,KOR_case,color='blue')
    plt.title('한국 확진자 증가 추세')
    plt.show()
    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
    plt.plot(KOR_date,KOR_deaths,color='red')
    plt.title('한국 사망자 증가 추세')
    plt.show()


    #미국 확진자 사망자

    USA_case = list(covid_USA['total_cases_per_million'])
    USA_deaths = list(covid_USA['total_deaths_per_million'])
    USA_date = list(covid_USA['date'])
    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))




    plt.plot(USA_date,USA_case,color='blue')
    plt.title('미국 확진자 증가 추세')
    plt.show()
    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
    plt.plot(USA_date,USA_deaths,color='red')
    plt.title('미국 사망자 증가 추세')
    plt.show()


    #인도 확진자 사망자

    IND_case = list(covid_IND['total_cases_per_million'])
    IND_deaths = list(covid_IND['total_deaths_per_million'])
    IND_date = list(covid_IND['date'])
    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))




    plt.plot(IND_date,IND_case,color='blue')
    plt.title('인도 확진자 증가 추세')
    plt.show()
    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
    plt.plot(IND_date,IND_deaths,color='red')
    plt.title('인도 사망자 증가 추세')
    plt.show()
    ax = plt.axes()

    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
    plt.plot(GHA_date,GHA_case,color='red')
    plt.plot(KOR_date,KOR_case,color='blue')
    plt.plot(USA_date,USA_case,color='green')
    plt.plot(IND_date,IND_case,color='yellow')
    plt.title('모집단 확진자 증가 추세')
    plt.show()
    ax = plt.axes()

    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(GHA_date,GHA_deaths,color='red')
    plt.plot(KOR_date,KOR_deaths,color='blue')
    plt.plot(USA_date,USA_deaths,color='green')
    plt.plot(IND_date,IND_deaths,color='yellow')
    plt.title('모집단 사망자 증가 추세')
    plt.show()


    #전세계 접종률
    world_vaccinations = list(covid_world['people_vaccinated'])
    world_vaccinations2 = list(covid_world['people_fully_vaccinated'])
    world_date = list(covid_world['date'])

    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(world_date,world_vaccinations,color='green')
    plt.plot(world_date,world_vaccinations2,color='skyblue')
    plt.title('전세계 백신 접종 현황')
    plt.show()

    #가나 접종률
    GHA_vaccinations = list(covid_GHA['people_vaccinated'])
    GHA_vaccinations2 = list(covid_GHA['people_fully_vaccinated'])
    GHA_date = list(covid_GHA['date'])

    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(GHA_date,GHA_vaccinations,color='green')
    plt.plot(GHA_date,GHA_vaccinations2,color='skyblue')
    plt.title('가나 백신 접종 현황')
    plt.show()

    #한국 접종률
    KOR_vaccinations = list(covid__KOR['people_vaccinated'])
    KOR_vaccinations2 = list(covid__KOR['people_fully_vaccinated'])
    KOR_date = list(covid__KOR['date'])

    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(KOR_date,KOR_vaccinations,color='green')
    plt.plot(KOR_date,KOR_vaccinations2,color='skyblue')
    plt.title('한국 백신 접종 현황')
    plt.show()

    #미국 접종률
    USA_vaccinations = list(covid_USA['people_vaccinated'])
    USA_vaccinations2 = list(covid_USA['people_fully_vaccinated'])
    USA_date = list(covid_USA['date'])

    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(USA_date,USA_vaccinations,color='green')
    plt.plot(USA_date,USA_vaccinations2,color='skyblue')
    plt.title('미국 백신 접종 현황')
    plt.show()

    #인도 접종률
    IND_vaccinations = list(covid_IND['people_vaccinated'])
    IND_vaccinations2 = list(covid_IND['people_fully_vaccinated'])
    IND_date = list(covid_IND['date'])

    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(IND_date,IND_vaccinations,color='green')
    plt.plot(IND_date,IND_vaccinations2,color='skyblue')
    plt.title('인도 백신 접종 현황')
    plt.show()

    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(GHA_date,GHA_vaccinations,color='red')
    plt.plot(KOR_date,KOR_vaccinations,color='blue')
    plt.plot(USA_date,USA_vaccinations,color='green')
    plt.plot(IND_date,IND_vaccinations,color='yellow')
    plt.title('모집단 백신 1차 접종 현황')
    plt.show()

    ax=plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(GHA_date,GHA_vaccinations2,color='red')
    plt.plot(KOR_date,KOR_vaccinations2,color='blue')
    plt.plot(USA_date,USA_vaccinations2,color='green')
    plt.plot(IND_date,IND_vaccinations2,color='yellow')
    plt.title('모집단 백신2차 접종 현황')
    plt.show()

    # 전세계 접종률
    world_vaccinations = list(covid_world['people_vaccinated_per_hundred'])
    world_vaccinations2 = list(covid_world['people_fully_vaccinated_per_hundred'])
    world_date = list(covid_world['date'])

    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(world_date, world_vaccinations, color='green')
    plt.plot(world_date, world_vaccinations2, color='skyblue')
    plt.title('전세계 백신 접종 현황')
    plt.show()

    # 가나 접종률
    GHA_vaccinations = list(covid_GHA['people_vaccinated_per_hundred'])
    GHA_vaccinations2 = list(covid_GHA['people_fully_vaccinated_per_hundred'])
    GHA_date = list(covid_GHA['date'])

    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(GHA_date, GHA_vaccinations, color='green')
    plt.plot(GHA_date, GHA_vaccinations2, color='skyblue')
    plt.title('가나 백신 접종 현황')
    plt.show()

    # 한국 접종률
    KOR_vaccinations = list(covid__KOR['people_vaccinated_per_hundred'])
    KOR_vaccinations2 = list(covid__KOR['people_fully_vaccinated_per_hundred'])
    KOR_date = list(covid__KOR['date'])

    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(KOR_date, KOR_vaccinations, color='green')
    plt.plot(KOR_date, KOR_vaccinations2, color='skyblue')
    plt.title('한국 백신 접종 현황')
    plt.show()

    # 미국 접종률
    USA_vaccinations = list(covid_USA['people_vaccinated_per_hundred'])
    USA_vaccinations2 = list(covid_USA['people_fully_vaccinated_per_hundred'])
    USA_date = list(covid_USA['date'])

    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(USA_date, USA_vaccinations, color='green')
    plt.plot(USA_date, USA_vaccinations2, color='skyblue')
    plt.title('미국 백신 접종 현황')
    plt.show()

    # 인도 접종률
    IND_vaccinations = list(covid_IND['people_vaccinated_per_hundred'])
    IND_vaccinations2 = list(covid_IND['people_fully_vaccinated_per_hundred'])
    IND_date = list(covid_IND['date'])

    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(IND_date, IND_vaccinations, color='green')
    plt.plot(IND_date, IND_vaccinations2, color='skyblue')
    plt.title('인도 백신 접종 현황')
    plt.show()

    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(GHA_date, GHA_vaccinations, color='red')
    plt.plot(KOR_date, KOR_vaccinations, color='blue')
    plt.plot(USA_date, USA_vaccinations, color='green')
    plt.plot(IND_date, IND_vaccinations, color='yellow')
    plt.title('모집단 100만명당 백신 1번 이상 접종 완료')
    plt.show()

    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

    plt.plot(GHA_date, GHA_vaccinations2, color='red')
    plt.plot(KOR_date, KOR_vaccinations2, color='blue')
    plt.plot(USA_date, USA_vaccinations2, color='green')
    plt.plot(IND_date, IND_vaccinations2, color='yellow')
    plt.title('모집단 100만명당 백신 2회이상 접종완료')
    plt.show()


if __name__ == '__main__':
    Main()

