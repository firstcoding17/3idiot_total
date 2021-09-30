import pandas as pd


#추천 알고리즘
#sytle => 성향 product => 상품구분 age => 나이
#channel => 채널 구분, age =>나이 gender=>성별
#loan =>대출 여부, special=> 특약 여부, insurance =>보험
#send => 납입 주기 final_send => 최종 납입 횟수 send_adduser=>가입 금액, month_send => 월납 보험료, send_way =>수금 방법
# job =>직업
def type(style,product,age,channel, gender, loan, special, insurance, send, final_send, send_adduser, month_send, send_way, job, moreinfo):

    df = pd.read_csv('mali_data1.csv')

    list = ['N2C0', 'N5A0', 'N1B0', 'N4C0', 'N750', 'N1J0', 'N2B0', 'N2D0', 'N5B0', 'N6D0', 'N380', 'N4A0', 'N1D0',
            'N260', 'N1A0', 'N2A0', 'N3C0', 'N3A0', 'N2E0', 'N1E0', 'N400', 'N6F0', 'N6B0', 'N9F0', 'N6A0', 'N4B0',
            'N910', 'N6C0', 'N440', 'N1H0', 'N460', 'U104', 'N9C0', 'N230', 'N600', 'N450', 'U702', 'N390', 'U703',
            'U504', 'N9N0', 'N9A0', 'U502', 'U408', 'N9M0', 'N1M0', 'N1K0', 'N1C0', 'U606', 'N410', 'U609', 'N1G0',
            'N620', 'N4D0', 'N1N0', 'N220', 'U405', 'U608', 'N500', 'N1F0', 'N9K0', 'U605', 'N110', 'N680', 'N140',
            'N650', 'N720', 'W406', 'N730', 'N690', 'N640', 'W701', 'N370', 'W111', 'N4F0', 'N130', 'W410', 'N710',
            'W310', 'N610', 'N630', 'N520', 'W408', 'N340', 'N240', 'N210', 'N510', 'N360', 'W506', 'N760', 'W703',
            'W609', 'N470', 'N350', 'W210', 'W211', 'N670', 'W510', 'W407', 'N300', 'W104', 'W604', 'W311', 'W710',
            'W702', 'W204', 'W607', 'N700', 'W304', 'W610', 'N150', 'N100', 'N490', 'W704', 'N160', 'N3D0', 'U305',
            'U001', 'N6E0', 'U407', 'N660', 'N900', 'N200', 'W801', 'W003', 'N310', 'U607', 'U701', 'U604', 'N430',
            'U404', 'U601', 'U401', 'N320', 'N330', 'N480', 'U304', 'N420', 'N9B0', 'N740', 'W608', 'N120', 'U704',
            'N9J0', 'W306', 'N270', 'N3B0', 'N9G0', 'W307', 'N9H0', 'N250', 'N9D0', 'U204', 'N9E0']
    style = style
    product = product
    age = age
    channel = channel
    gender = gender
    loan = loan
    special = special
    insurance = insurance
    send = send
    final_send = final_send
    send_adduser = send_adduser
    month_send = month_send
    send_way = send_way
    job = job

    df = df[df['product_cd'] == product]
    df = df[df['age_cd'] == age ]
    df = df[df['channel_cd'] == channel]
    df = df[df['gender'] == gender]
    df = df[df['loan_yn'] == loan]
    df = df[df['rider'] == special]
    df = df[df['cntr_cnt'] == insurance]
    df = df[df['pay_prd'] == send]
    df = df[df['avg_max_pay'] == final_send]
    df = df[df['avg_jn_amt'] == send_adduser]
    df = df[df['sum_fee_amt'] == month_send]
    df = df[df['pcpt_cd'] == send_way]
    df = df[df['job_cd'] == job]
    df = df[df['base_ym'] == '2020-12']



    danger = [2,3,4,5]

    choose_danger = 0

    if style == 1 or style == 2:
        choose_danger = danger[0]
    elif style == 3:
        choose_danger = danger[1]
    elif style == 4:
        choose_danger = danger[2]
    elif style == 5:
        choose_danger = danger[3]

    df = df[df['operation_rsk'] == choose_danger]
    df_sort = df[moreinfo]

    check_list =[]

    for i in range(0, len(df)):
        if df[moreinfo][i] not in check_list:
            check_list.append(df[moreinfo][i])
    check_list = sorted(check_list)
    check_list = reversed(check_list)

    set_df = df[df[moreinfo] == check_list[0]]
    #중복 방지 0번째 출력
    new_df = {'펀드이름' : set_df['fund_nm'][0],'위험도' : set_df['operation_rsk'][0], '운용회사' : set_df['operation_conm'][0]}
    new_df = pd.DataFrame(new_df)
    for i in range(1,len(df)):
        set_df = df[df[moreinfo] == check_list[0]]
        Data_insert = {
            '펀드이름': set_df['fund_nm'][0],
            '위험도': set_df['operation_rsk'][0],
            '운용회사': set_df['operation_conm'][0]
        }
        new_df_1 = pd.DataFrame(Data_insert)

        df = pd.concat([new_df, new_df_1], sort=False)

    return new_df



















