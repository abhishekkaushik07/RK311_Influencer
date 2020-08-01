from flask import Flask, flash, request, redirect, url_for ,render_template,session
import ping
import ip_in_file
import shodan_test
import whois

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template("dashboard.html")

@app.route('/search',methods=["POST","GET"])
def ip_search():
    if request.method == 'POST':
        given_ip = request.form
    
    ip = given_ip["IP"]
    # ping_out = ping.ping1(ip).split('\\'+'n')
    ipout = ip_in_file.find_in_all_files(ip)

#	mylist.insert(END, ipout[0])
    result = []
#    print(ping_out)
    ipout_fl = ipout[1]
    if not ipout_fl:
        shodan_res = shodan_test.shodan1(str(ip))
        shodan_out = shodan_res[0].split('\n')
        result.append(shodan_out)
#		for lines in shodan_out :
#			mylist.insert(END, lines)

#		if shodan_res[1] == 1 :
#			l4 = Label(r,text="Yes")
#			l4.pack()
#		else :
#			l4 = Label(r,text="No")
#			l4.pack()
    whois_out = whois.whois1(ip)
    whois_res = whois_out.split('\n')
#	for lines in whois_res :
#		mylist.insert(END, lines)
#	mylist.pack( side = LEFT, fill = BOTH ) 
#	scrollbar.config( command = mylist.yview )
    
    # result.append(ping_out)
    result.append(ipout)
    result.append(ipout_fl)
    
    result.append(whois_res)
	    
    return render_template("result.html",ip=given_ip,result =result )

if __name__ == '__main__':
    app.run()

