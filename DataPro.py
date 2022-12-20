
import quandl
import numpy as np
import pandas as pd
import csv
import talib
import datetime

#Login
#----------------------------

#acc 1
#intrinio.client.username = 'c1ee45eb7551da89ef3595ade3a2690a'
#intrinio.client.password = 'd47499179b27b45b6c4be847e2c62274'
#intrinio.client.username = '75108fd3e3fbc7ab90e98450067e4c7d'
#intrinio.client.password = '608b1d414830cd39ec55573a1a2a16fa'
quandl.ApiConfig.api_key = "RMfMK6xZuHGPzt9XKNod"
#----------------------------


#for display better
#----------------------------
pd.set_option('display.height',2000)
pd.set_option('display.max_rows',5000)
pd.set_option('display.max_columns',5000)
pd.set_option('display.width',10000)
#------------------------------------
#mydata = quandl.get_table('ZACKS/FR', ticker='AAPL')
#print(mydata)

#print(intrinio.prices('AAPL', start_date='2016-01-01'))
#print(intrinio.fundamentals('AAPL','QTR', 'cash_flow_statement'))

mainD = pd.read_csv('dataName.csv')
stockName =mainD['ticker']
#output_file = open('output.csv', 'w', newline='')
#data = csv.writer(output_file)

#Target is  SMA30 after 180 days
count = 0
trainData = ['ticker','date', 'Target','SMAN','volC90','volC180','BBH','BBL','NATR','AR','ROCP','MACD','BIAS','MBWR', 'MBMR' ,'MBSR', 'MBWS' ,'MBMS' ,'MBSS','ADR','SMA6', 'SMA4','SMA2','BV1','BV2','OCF2','OCF1','OPM2','OPM1','OPM'
             ,'AT','AT1','AT2','rEq','rA','rA1','rA2','cR','rIn','rIn1','rIn2','rTEQ','rTEQ1','Lterm','gMar','FCF1','FCF2','QTR','DS1','DS2']

mydata = quandl.get_table('ZACKS/FR', ticker='AAPL')
#print(mydata)
for i in range(len(mydata.index)):
    here =  ['ticker','date', 'Target','SMAN','volC90','volC180','BBH','BBL','NATR','AR','ROCP','MACD','BIAS','MBWR', 'MBMR' ,'MBSR', 'MBWS' ,'MBMS' ,'MBSS','ADR','SMA6', 'SMA4','SMA2','BV1','BV2','OCF2','OCF1','OPM2','OPM1','OPM'
             ,'AT','AT1','AT2','rEq','rA','rA1','rA2','cR','rIn','rIn1','rIn2','rTEQ','rTEQ1','Lterm','gMar','FCF1','FCF2','QTR','DS1','DS2']

    ticker =  mydata.get_value(mydata.index[i],'ticker')
#    print(quandl.get("WIKI/" + ticker, start_date=date, end_date=end_fullDate))
 #   df['SMA60'] = talib.SMA(np.array(df['Close']), timeperiod=60)
    if(mydata.get_value(mydata.index[i],'per_type') == 'Q'):
        count = count + 1
        # handle Date
        date = mydata.get_value(mydata.index[i], 'per_end_date')
        a61days = date + datetime.timedelta(days=61)
        b61days = date - datetime.timedelta(days=61)
        b30days = date - datetime.timedelta(days=31)


        # print(df)
        # QTR
        QTR = mydata.get_value(mydata.index[i], 'per_cal_qtr')

        # SMAN
        df = quandl.get("WIKI/" + mydata.get_value(mydata.index[i], 'ticker'), start_date=b61days, end_date=date)
        SMAN = talib.SMA(np.array(df['Adj. Close']), timeperiod=30)[-1]
        VolN = talib.SMA(np.array(df['Adj. Volume']), timeperiod=30)[-1]

        #target
        df = quandl.get("WIKI/" + mydata.get_value(mydata.index[i], 'ticker'),
                        start_date=date , end_date=date + datetime.timedelta(days=183))
        target = talib.SMA(np.array(df['Adj. Close']), timeperiod=30)[-1] / SMAN

        # SMA 6
        df = quandl.get("WIKI/" + mydata.get_value(mydata.index[i], 'ticker'),
                    start_date=date - datetime.timedelta(days=230), end_date=date - datetime.timedelta(days=183))
        SMAb180 = talib.SMA(np.array(df['Adj. Close']), timeperiod=30)[-1]
        SMA6 = SMAN / SMAb180

        # SMA 4
        df = quandl.get("WIKI/" + mydata.get_value(mydata.index[i], 'ticker'),
                    start_date=date - datetime.timedelta(days=170), end_date=date - datetime.timedelta(days=122))
        SMAb120 = talib.SMA(np.array(df['Adj. Close']), timeperiod=30)[-1]
        SMA4 = SMAN / SMAb120

        # SMA 2
        df = quandl.get("WIKI/" + mydata.get_value(mydata.index[i], 'ticker'),
                    start_date=date - datetime.timedelta(days=110), end_date=date - datetime.timedelta(days=61))
        SMAb60 = talib.SMA(np.array(df['Adj. Close']), timeperiod=30)[-1]
        SMA2 = SMAN / SMAb60


        #volC90
        df = quandl.get("WIKI/" + mydata.get_value(mydata.index[i], 'ticker'),
                        start_date=date - datetime.timedelta(days=140), end_date=date - datetime.timedelta(days=92))
        volb90 = talib.SMA(np.array(df['Adj. Volume']), timeperiod=30)[-1]
        volC90 = VolN / volb90
        #volC180
        df = quandl.get("WIKI/" + mydata.get_value(mydata.index[i], 'ticker'),
                        start_date=date - datetime.timedelta(days=230), end_date=date - datetime.timedelta(days=183))
        volb180 = talib.SMA(np.array(df['Adj. Volume']), timeperiod=30)[-1]
        volC180 = VolN/ volb180

        #BBH and BBL
        df = quandl.get("WIKI/" + mydata.get_value(mydata.index[i], 'ticker'),
                    start_date=date - datetime.timedelta(days=90), end_date=date)

        upperband, middleband, lowerband = talib.BBANDS(np.array(df['Adj. Close']), timeperiod=50, nbdevup=2, nbdevdn=2, matype=0)
        BBH = upperband[-1] / SMAN
        BBL = lowerband[-1] / SMAN


        #NATR
        df = quandl.get("WIKI/" + mydata.get_value(mydata.index[i], 'ticker'),
                        start_date=date - datetime.timedelta(days=220), end_date=date)
        NATR = talib.NATR(np.array(df['Adj. High']), np.array(df['Adj. Low']), np.array(df['Adj. Close']), timeperiod=50)[-1]

        #'AROON'
        aroondown, aroonup = talib.AROON(np.array(df['Adj. High']), np.array(df['Adj. Low']),timeperiod = 30)
        AR = aroonup[-1] - aroondown[-1]

        # 'ROCP'
        ROCP = talib.ROCP(np.array(df['Adj. Close']), timeperiod=30)[-1]
        # 'MACD'
        MACD, macdsignal, macdhist = talib.MACD(np.array(df['Adj. Close']), fastperiod=60, slowperiod=120, signalperiod=45)


        # 'BIAS'
        BIAS = (SMAN -talib.SMA(np.array(df['Adj. Close']), timeperiod=92)[-1]) /talib.SMA(np.array(df['Adj. Close']), timeperiod=92)[-1]

        # 'Mike Base = WR, MR ,SR  , WS ,MS ,SS
        df = quandl.get("WIKI/" + mydata.get_value(mydata.index[i], 'ticker'),
                        start_date=date - datetime.timedelta(days=180), end_date=date)

        TYP = (talib.SMA(np.array(df['Adj. Close']), timeperiod=130)[-1] * 2 +talib.SMA(np.array(df['Adj. High']), timeperiod=130)[-1] +talib.SMA(np.array(df['Adj. Low']), timeperiod=130)[-1]) /4
        WR = (TYP + (TYP - min(np.array(df['Adj. Low']))))/SMAN
        MR = (TYP + max(np.array(df['Adj. High'])) -min(np.array(df['Adj. Low']))) /SMAN
        SR = (2* max(np.array(df['Adj. High'])) -min(np.array(df['Adj. Low']))) /SMAN
        WS = (2* TYP - max(np.array(df['Adj. High'])))/SMAN
        MS = (TYP - max(np.array(df['Adj. High'])) + min(np.array(df['Adj. Low'])))/SMAN
        SS = (min(np.array(df['Adj. Low'])) *2 - max(np.array(df['Adj. High'])))/SMAN

        # 'ADR'



        # 'BV1'
        # 'BV2'
        # 'OCF2'
        # 'OCF1'
        # 'OPM2'
        # 'OPM1'
        # 'OPM'
        # 'AT'
        # 'AT1'
        # 'AT2'
        # 'rEq'
        # 'rA'
        # 'rA1'
        # 'rA2'
        # 'cR'
        # 'rIn'
        # rIn1
        # rIn2
        # rTEQ
        # 'rTEQ1
        # Lterm
        # gMar
        # FCF1
        # FCF2
        # DS1
        # DS2'

        print(target)
        print(SMAN)
        print(SMA2)
        print(SMA4)
        print(volC90)
        print(volC180)
        print(BBH)
        print(BBL)
        print(NATR)
#        if(count > 2):5


