def getDividendHistory(stockObject):

    #getting info and converting to dict
    stockDividendInfo = stockObject.dividends
    df = stockDividendInfo.to_frame() 
    df_dict = df.to_dict('index')

    for n in df_dict:

        df_dict[n] = (df_dict[n]['Dividends'])

    for n in df_dict:
        print(f"Date: {n}, Dividend Paid =  ${df_dict[n]}")

def swedishInvestorRatios(stockObject):
    # show earnings
    print(stockObject.history(period="12mo"))

    stockObject.history_metadata   
    print(stockObject.earnings)
