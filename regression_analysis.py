import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import joblib

# 读取数据
df = pd.read_csv("data/engagement_data.csv")
X = df[["W", "X"]]
y = df["Y_obs"]

# 模型1: 不控制支出
X1 = sm.add_constant(df["W"])
model1 = sm.OLS(y, X1).fit()
print("Model 1 (Y ~ W) Summary:\n", model1.summary())

# 模型2: 控制支出
X2 = sm.add_constant(X)
model2 = sm.OLS(y, X2).fit()
print("Model 2 (Y ~ W + X) Summary:\n", model2.summary())

# 拟合 sklearn 模型用于 Flask
lr = LinearRegression()
lr.fit(X, y)
joblib.dump(lr, "model/trained_model.pkl")

# 残差图
y_pred = lr.predict(X)
residuals = y - y_pred
plt.figure(figsize=(6,4))
sns.residplot(x=y_pred, y=residuals, lowess=True, line_kws={'color': 'red'})
plt.xlabel("Predicted Engagement Score")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.tight_layout()
plt.savefig("figures/residual_plot.png")
