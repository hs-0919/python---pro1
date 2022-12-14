# MariaDB에 저장된 jikwon 테이블을 이용하여 아래의 문제에 답하시오.
#      - pivot_table을 사용하여 성별 연봉의 평균을 출력
#      - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
#      - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))

import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False
import sys

try : 
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('connect err : ', e)
    sys.exit()

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select buser_name,jikwon_gen,jikwon_pay
        from jikwon inner join buser 
        on buser_num=buser_no
    """

    print('pandas의 sql 처리 기능 사용해서 읽기')
    df = pd.read_sql(sql, conn)
    df.columns = ['부서','성별','연봉']
    print(df.head(3))

    print()
    print(df.pivot_table(values=['연봉'], index=['성별'], aggfunc=np.mean))

    # 시각화 : 성별 연봉 평균
    m = df[df['성별'] == '남']
    m_pay_mean = m.loc[:,'연봉'].mean()
    f = df[df['성별'] == '여']
    f_pay_mean = f.loc[:,'연봉'].mean()
    mean_pay = [m_pay_mean, f_pay_mean]

    plt.bar(range(len(mean_pay)), mean_pay, color=['black','yellow'])
    plt.xlabel('성별')
    plt.ylabel('연봉')
    plt.xticks(range(len(mean_pay)), labels=['남성','여성'])

    for i, v in enumerate(range(len(mean_pay))):
        plt.text(v, mean_pay[i], mean_pay[i], 
                 fontsize=12,
                 color='blue',
                 horizontalalignment='center',
                 verticalalignment='bottom')
    plt.show()

    ctab = pd.crosstab(df['부서'], df['성별'])
    print(ctab)

except Exception as e:
    print('처리 오류 : ', e)  