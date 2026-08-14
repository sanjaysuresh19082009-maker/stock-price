import yfinance as yf
import matplotlib.pyplot as plt
cmpy_name=input("what company: " ).upper()
period = input("what period: ")


ticker=yf.Ticker(f"{cmpy_name}")
print(ticker.history(period=f"{period}") )
data = [
        ticker.analyst_price_targets['high'],
        ticker.analyst_price_targets['median'],
        ticker.analyst_price_targets['low']
        ]
plt.boxplot(data)
plt.boxplot(
    data,
    patch_artist=True, 
    boxprops=dict(facecolor='green', color='green'),
    whiskerprops=dict(color='green', linewidth=1.5), 
    capprops=dict(color='green', linewidth=1.5),          
    medianprops=dict(color='darkgreen', linewidth=2) 
)

plt.title("current value")
plt.ylabel("Values")
plt.show()
