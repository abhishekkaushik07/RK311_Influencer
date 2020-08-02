from flask import Flask, flash, request, redirect, url_for ,render_template,session
import ip_in_file
import json
import ip2proxyTest
import ipqualityTest
import shodanTest
import whoisTest
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
GoogleMaps(app, key="8JZ7i18MjFuM35dJHq70n3Hx4")

@app.route('/')
def dashboard():
    return render_template("dashboard.html")

@app.route('/search',methods=["POST","GET"])
def ip_search():
    if request.method == 'POST':
        given_ip = request.form
    
    ip = given_ip["IP"]

    # ipout = ip_in_file.find_in_all_files(ip)


    result = []

    # ipout_fl = ipout[1]
    # if not ipout_fl:
    #     shodan_res = newshodan.shodan1(str(ip))
    #     # shodan_out = shodan_res[0].split('\n')
    #     result.append(shodan_res)

    # whois_out = newshodan.whois1(ip)
    # data = json.loads(whois_out)
    
    # ip_proxy = ip2proxy_detector.ip2proxy(ip)
    # result.append(ip_proxy)

    # ipqua = ipquality.ipQuality(ip)
    # result.append(ipqua.split('\n'))
    # whois_final = []


    # print(type(data))
    # print(type(data['cidr']))
    ipout = ip_in_file.find_in_all_files(ip)
    vpn_db = ipout[0]
    vpn_flag = ipout[1]

    ip2proxy_out = ip2proxyTest.ip2proxy_fun(ip)
    ipquality_out = ipqualityTest.ipquality_fun(ip)
    shodan_out = shodanTest.shodan_fun(ip)
    whois_out = whoisTest.whois_fun(ip)
    
    data = whois_out['nets'][0]

    whois_final = []

    if(data['cidr']):
        whois_final.append("Cidr        : " + data['cidr']) 
    else:
        whois_final.append("Cidr        : " + "NA")

    if(data['name']):
        whois_final.append("Name        : " + data['name'])
    else:
        whois_final.append("Name        : " +"NA")

    if(data['handle']):
        whois_final.append("Handle      : " + data['handle'])
    else:
        whois_final.append("Handle        : " +"NA")

    if(data['range']):
        whois_final.append("Range       : " + data['range'])
    else:
        whois_final.append("Range        : " +"NA")

    if(data['description']):
        whois_final.append("Description : " + data['description'])
    else:
        whois_final.append("Description        : " +"NA")

    if(data['country']):
        whois_final.append("Country     : " + data['country'])
    else:
        whois_final.append("Country        : " +"NA")

    if(data['state']):
        whois_final.append("State       : " + data['state'])
    else:
        whois_final.append("State       : " +"NA")

    if(data['city']):
        whois_final.append("City        : " + data['city'])
    else:
        whois_final.append("City        : " +"NA")

    if(data['address']):
        whois_final.append("Address     : " + data['address'])
    else:
        whois_final.append("Address     : " +"NA")

    if(data['postal_code']):
        whois_final.append("Postal Code : " + data['postal_code'])
    else:
        whois_final.append("Postal Code : " +"NA")

    if(data['created']):
        whois_final.append("Created     : " + data['created'])
    else:
        whois_final.append("Created     : " +"NA")

    if(data['updated']):
        whois_final.append("Updated     : " + data['updated'])
    else:
        whois_final.append("Updated     : " +"NA")

    if(data['emails']):
        whois_final.append("Email       : " + str(data['emails']))
    else:
        whois_final.append("Email       : " +"NA")

    ipquality_final=[]
    
    if(ipquality_out['country_code']):
        ipquality_final.append("Country code:      " + ipquality_out['country_code'])
    else:
        ipquality_final.append("Country code:      " + "NA")

    if(ipquality_out['region']):
        ipquality_final.append("Region:      " + ipquality_out['region'])
    else:
        ipquality_final.append("Region:      " + "NA")

    if(ipquality_out['city']):
        ipquality_final.append("City:      " + ipquality_out['city'])
    else:
        ipquality_final.append("City:      " + "NA")

    if(ipquality_out['ISP']):
        ipquality_final.append("ISP:      " + ipquality_out['ISP'])
    else:
        ipquality_final.append("ISP:      " + "NA")

    if(ipquality_out['organization']):
        ipquality_final.append("Organization:      " + ipquality_out['organization'])
    else:
        ipquality_final.append("Organization:      " + "NA")

    ipqua_res=[]    
    if(ipquality_out['fraud_score']):
        ipqua_res.append("Fraud_score: " + str(ipquality_out['fraud_score']))
    else:
        ipqua_res.append("Fraud_score: " + "NA")

    if(ipquality_out['tor']):
        ipqua_res.append("Tor: " + str(ipquality_out['tor']))
    else:
        ipqua_res.append("Tor: " + "NA")

    if(ipquality_out['vpn']):
        ipqua_res.append("VPN: " + str(ipquality_out['vpn']))
    else:
        ipqua_res.append("VPN: " + "NA")

    if(ipquality_out['proxy']):
        ipqua_res.append("Proxy: " + str(ipquality_out['proxy']))
    else:
        ipqua_res.append("Proxy: " + "NA")


    lat_log =[]
    if(ipquality_out['latitude']):
        lat_log.append(ipquality_out['latitude'])
    else:
        lat_log.append(0)

    if(ipquality_out['longitude']):
        lat_log.append(ipquality_out['longitude'])
    else:
        lat_log.append(0)
    str_lat_log = "https://maps.google.com/maps?q="+str(lat_log[0])+","+str(lat_log[1])+"&hl=en&z=9&amp;output=embed"

    mymap = Map(
        identifier="view-side",
        lat=str(lat_log[0]),
        lng=str(lat_log[1]),
        markers=[(str(lat_log[0]), str(lat_log[1]))]
    )
    
    str_vpn=False
    if(shodan_out !={}):
        if(shodan_out['tags']):
            if 'vpn' in shodan_out['tags']:
                str_vpn = True

    ip2proxy_res=''
    if(ip2proxy_out["isProxy"]!="NO" or ip2proxy_out["proxyType"]=="DCH"):   # take care of Data centre/Web hosting
        ip2proxy_res+= "Proxy Detected\n"
        ip2proxy_res+= "proxyType is " + ip2proxy_out["proxyType"]+'\n'
    else :
        ip2proxy_res+= "No Proxy Detected\n"
    # whois_res = whois_out.split('\n')
#	for lines in whois_res :
#		mylist.insert(END, lines)
#	mylist.pack( side = LEFT, fill = BOTH ) 
#	scrollbar.config( command = mylist.yview )
    
    # result.append(ping_out)
    # result.append(ipout)
    # result.append(ipout_fl)
    # result.append(whois_out)
	    
    return render_template("result.html",ip=given_ip,result =result ,whois_res=whois_final, ipquality_final=ipquality_final, mymap=mymap, lat_log=str_lat_log, str_vpn=str_vpn, ip2proxy_res=ip2proxy_res,ipqua_res=ipqua_res )

if __name__ == '__main__':
    app.run(host='localhost',port =5544,debug=True)

