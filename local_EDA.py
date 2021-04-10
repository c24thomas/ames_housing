from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def heat(df, target, x=12, y=12, annot=True, masked=True):
    '''
    Creates a mask and then plots a seaborn heatmap.

    df: The dataframe to map
    target: The target variable (i.e. whatever variable you want to appear last)
    x: x-dimension of the size of the visualization (default=12)
    y: y-dimension (default=12)
    annot: Whether or not the correlations are overlaid on the heatmap (default=True)
    masked: Whether or not the top half triangle is masked (default=True)
    '''
    tgt = df[target]
    df = df.drop(columns=[target])
    df.insert(loc=len(df.columns), column=target, value=tgt)
    if masked:
        corr = df.corr()
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True
    else:
        mask=None
    plt.figure(figsize=(x, y))
    sns.heatmap(corr, annot=annot, cmap='coolwarm', mask=mask, vmin=-1, vmax=1);



def get_corr_above_or_below(df, percentage):
    '''
    Returns a dict of correlations above a certain abs(percent).

    df: The dataframe to map
    percentage: The absolute value of the max/min percent correlation
    '''
    corr = df.corr()
    col_rows = corr.columns.tolist()
    keep_corrs = {}
    for col in col_rows:
        for row in col_rows:
            if corr.loc[col, row] >= percentage or corr.loc[col, row] <= percentage*-1:
                if col == row:
                    break
                if col in keep_corrs:
                    keep_corrs[col][row] = corr.loc[col, row]
                else:
                    keep_corrs[col] = {row: corr.loc[col, row]}
    return keep_corrs



def r2_adj(model, X, y):
    r2 = model.score(X, y)
    n = y.shape[0]
    k = X.shape[1]
    return 1 - (((1 - r2)*(n - 1))/(n - k - 1))



def scores(X, y):
    model = LinearRegression()
    model.fit(X, y)
    y_hat = model.predict(X)
    r2 = model.score(X, y)
    adj_r2 = r2_adj(model, X, y)
    mse = mean_squared_error(y, y_hat)
    rmse = mean_squared_error(y, y_hat, squared=False)
    return f'''
R2: {round(r2, 4)}\n
Adjusted R2: {round(adj_r2, 4)}\n
MSE: {round(mse, 4)}\n
RMSE: {round(rmse, 4)}
'''
