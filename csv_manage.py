#https://www.m3tech.blog/entry/python-snippets

import csv

class Csv:
	def read(self,csvfile):
		with open(csvfile,'r',encoding='utf-8') as rf:
			reader = csv.reader(rf,delimiter=' ')
			header = next(reader)
			
			for row in reader:
				print(','.join(row))
		
	def write(self,csvfile):
		with open(csvfile,'w',encoding='utf-8') as wf:
			writer = csv.writer(wf,elimiter=',',lneterminator='\n')
			writer.writerow(list) 		

CSV = Csv()
CSV.read("test.csv")
