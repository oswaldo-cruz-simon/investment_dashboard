import pandas as pd
import numpy as np
import datetime

YEAR = 360
MINIMUN = 1000


def investment_return(capital, time, yield_):
    if capital % MINIMUN != 0:
        raise ValueError("capital must be multiple of 1000")
    revenue = (capital * yield_ * time)/YEAR
    commission_percentage = 0.077328
    commission = revenue * commission_percentage
    return_ = revenue - commission
    return {
        "revenue": revenue,
        "commission_percentage": commission_percentage,
        "commission": commission,
        "return": return_
    }


def fix_capital(capital):
    if (capital % MINIMUN) == 0:
        return 0
    capital = MINIMUN - (capital % MINIMUN)
    return capital


def fix_capital_no_extra(capital):
    res = capital % MINIMUN
    return capital - res, res


def predict_by_year(vehicles):
    capital = 0
    days = 0
    time_serie = []
    for i in vehicles:
        capital += i['capital'] if "capital" in i else 0
        invret = investment_return(capital, i['time'], i['yield'])
        days += i['time']
        capital += invret['return']
        complement = fix_capital(capital)
        time_serie.append({
            "time": days,
            "extra_money": complement,
            "return": invret,
            "capital": capital
        })
        capital += complement
    extra_money = sum([i['extra_money'] for i in time_serie])
    return {
        "time_serie": time_serie,
        "return": capital,
        "days": days,
        "extra_money": extra_money,
        "investment_capital": extra_money + vehicles[0]['capital'],
        "profits": capital - extra_money - vehicles[0]['capital']
    }


def predict_by_year_no_extra(vehicles):
    capital = 0
    days = 0
    time_serie = []
    for i in vehicles:
        capital += i['capital'] if "capital" in i else 0
        complete, incomplete = fix_capital_no_extra(capital)
        invret = investment_return(complete, i['time'], i['yield'])
        days += i['time']
        capital += invret['return']

        time_serie.append({
            "time": days,
            "extra_money": 0,
            "return": invret,
            "capital": capital
        })
    extra_money = sum([i['extra_money'] for i in time_serie])
    return {
        "time_serie": time_serie,
        "return": capital,
        "days": days,
        "extra_money": extra_money,
        "investment_capital": extra_money + vehicles[0]['capital'],
        "profits": capital - extra_money - vehicles[0]['capital']
    }


def to_dataframe(prediction):
    today = datetime.datetime.now()
    time = np.array([today + datetime.timedelta(i['time']) for i in prediction['time_serie']])
    capital = np.array([i['capital'] for i in prediction['time_serie']])
    return_ = np.array([i['return']['return'] for i in prediction['time_serie']])
    ts = pd.Series(return_, index=time)
    ts = ts.cumsum()
    df = pd.DataFrame({"return": return_}, index=time)
    df = df.cumsum()
    df['capital'] = pd.Series(capital, index=time)
    return df

