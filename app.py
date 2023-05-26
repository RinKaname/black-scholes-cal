from matplotlib.colors import LogNorm
import streamlit as st
import math as math
from scipy.stats import norm

stock_price = st.number_input(label='stock_price', value= 100)
strike_price = st.number_input(label='strike_price', value= 110.25)
time_to_maturity = st.number_input(label='time_to_maturity', value= 3)
implied_volatility = st.number_input(label='implied_volatility', value= 20)
free_float_rate = st.number_input(label='free_float_rate', value= 4)
dividend_yield = st.number_input(label='dividend_yield', value= 0)

if(time_to_maturity != 0, implied_volatility != 0, free_float_rate != 0, dividend_yield != 0):
    time_to_maturity = time_to_maturity / 12
    implied_volatility = implied_volatility / 100
    free_float_rate = free_float_rate / 100
    dividend_yield = dividend_yield / 100

d1 = ((math.log(float(stock_price) / float(strike_price))) + (float(free_float_rate) + float(implied_volatility)**2 / 2) * float(time_to_maturity)) / (float(implied_volatility) * math.sqrt(float(time_to_maturity)))
d2 = ((math.log(float(stock_price) / float(strike_price))) + (float(free_float_rate) - float(implied_volatility)**2 / 2) * float(time_to_maturity)) / (float(implied_volatility) * math.sqrt(float(time_to_maturity)))
Nd1 = 1 - norm.cdf(-d1)
Nd2 = 1 - norm.cdf(-d2)
Nd1p = 1 - norm.cdf(d1)
Nd2p = 1 - norm.cdf(d2)

Call_premium = (stock_price * Nd1) * (math.e ** (- dividend_yield * time_to_maturity )) - strike_price * Nd2 * (math.e ** (-free_float_rate * time_to_maturity))
rounded_call_premium = round(number= Call_premium, ndigits= 2)
Put_premium = (strike_price * Nd2p * math.e ** (-free_float_rate*time_to_maturity)) - (stock_price * Nd1p) * (math.e ** (- dividend_yield * time_to_maturity )) 
rounded_put_premium = round(number= Put_premium, ndigits= 2)
st.markdown("<h1 style='text-align: center; color: red;'>Option Call and Put Premium</h1>", unsafe_allow_html=True)
st.write(f'Call premium: {rounded_call_premium}')
st.write(f'Put premium: {rounded_put_premium}')


