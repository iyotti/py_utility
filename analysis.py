#https://qiita.com/takubb/items/286916434ce44889d0fd

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#class Pareto:
#	def make_pareto(self):
	
A = np.repeat('Cat_A', 15)
B = np.repeat('Cat_B', 5)
C = np.repeat('Cat_C', 135)
D = np.repeat('Cat_D', 23)
E = np.repeat('Cat_E', 86)
F = np.repeat('Cat_F', 44)
G = np.repeat('Cat_G', 13)
H = np.repeat('Cat_H', 3)
I = np.repeat('Cat_I', 3)
J = np.repeat('Cat_J', 2)
K = np.repeat('Cat_K', 2)
data = np.concatenate((A,B,C,D,E,F,G,H,I,J,K))
data = pd.Series(data)

plt.figure(figsize=(15,3))
sns.countplot(data)

t = data.value_counts() #カテゴリごとの合計
r = t/t.sum() #割合に変換
r_ = r.cumsum() #累積割合に変換
#上記で集計したカテゴリ枚の合計(t)と累積割合(r_)を可視化
#全体構成の80％のボーダーライン
fig, ax1 = plt.subplots()
t.plot.bar(figsize=(15, 3), color='blue', ax=ax1)
ax2 = ax1.twinx()
r_.plot(figsize=(15, 3), color='orange', ax=ax2, marker='o')
plt.hlines(y=0.8, xmin=-1, xmax=len(t), lw=.7, color='indianred', linestyle='--')
plt.show()