import glob
import os

path = input("prefixを付けたいディレクトリを入力：")
pfx  = input("prefixを入力：")
files = glob.glob(path+"/*")

for f in files:
	os.rename(f,os.path.join(path,pfx+os.path.basename(f)))