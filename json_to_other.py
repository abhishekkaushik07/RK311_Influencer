# install these before running this file
# 1. sudo apt-get install wkhtmltopdf
# 2. pip install json2html
# 3. pip install pdfkit

from json2html import *
import json
import pdfkit

def convert_json():
	with open("shodanout.json") as f:
		js = json.load(f)
		x = json2html.convert(json = js)

		f1 = open("shodanout.html",'w')
		f1.write(x)
		f1.close()

	with open("shodanout.json") as f:
		data = f.read().replace('\n', '')

		f2 = open("shodanout.txt", 'w')
		f2.write(data)
		f2.close()

	with open("ip2proxyout.json") as f:
		js = json.load(f)
		x = json2html.convert(json = js)
		
		f1 = open("ip2proxyout.html",'w')
		f1.write(x)
		f1.close()

	with open("ip2proxyout.json") as f:
		data = f.read().replace('\n', '')

		f2 = open("ip2proxyout.txt", 'w')
		f2.write(data)
		f2.close()

	with open("ipqualityout.json") as f:
		js = json.load(f)
		x = json2html.convert(json = js)

		f1 = open("ipqualityout.html",'w')
		f1.write(x)
		f1.close()

	with open("ipqualityout.json") as f:
		data = f.read().replace('\n', '')

		f2 = open("ipqualityout.txt", 'w')
		f2.write(data)
		f2.close()

	with open("whoisout.json") as f:
		js = json.load(f)
		x = json2html.convert(json = js)

		f1 = open("whoisout.html",'w')
		f1.write(x)
		f1.close()

	with open("whoisout.json") as f:
		data = f.read().replace('\n', '')

		f2 = open("whoisout.txt", 'w')
		f2.write(data)
		f2.close()

	pdfkit.from_file('whoisout.html','whoisout.pdf')
	pdfkit.from_file('ipqualityout.html','ipqualityout.pdf')
	pdfkit.from_file('ip2proxyout.html','ip2proxyout.pdf')
	pdfkit.from_file('shodanout.html','shodanout.pdf')