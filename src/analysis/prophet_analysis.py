import fbprophet
import matplotlib.pyplot as plt
# from scipy.special import inv_boxcox
# from scipy.stats import boxcox


def get_pred(df, periods=5):

    df = df.drop(columns=['open', 'high', 'low', 'volume'])
    df.columns = ['ds', 'y']

    model = fbprophet.Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods, freq='d')
    forecast = model.predict(future)
    model.plot(forecast)
    model.plot_components(forecast)
    # forecast[['yhat','yhat_upper','yhat_lower']] = forecast[['yhat','yhat_upper','yhat_lower']].apply(lambda x: inv_boxcox(x, lam))
    plt.show()