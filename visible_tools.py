#https://qiita.com/takapy_AI/items/73415599579f2588080e
#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns
%matplotlib inline
import random
def make_hist(x,bin):
	plt.hist(x, bins=bin)
	plt.title("quality_Histgram")
	plt.xlabel('quality')
	plt.ylabel('count')
	plt.show()

def make_data(x,bin):
	random.seed(0)
	plt.figure(figsize=(20, 6))
	plt.hist(x, bins=bin, range=(20,80))
	plt.grid(True)

def scatter_plot(x,y):
	random.seed(0)
	plt.figure(figsize=(16, 6)) #グラフの大きさ指定
	#グラフの描写
	plt.plot(x, y, 'o')
	plt.title("title")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True)


#x = np.random.randn(10**5)*10 + 50
x = np.random.randn(50) #x軸のデータ
y = np.sin(x) + np.random.randn(50) #y軸のデータ

bin = 60
make_hist(x,bin)
#make_data(x,bin)
scatter_plot(x,y)