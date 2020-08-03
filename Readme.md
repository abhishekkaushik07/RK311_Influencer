1. Objective: Proxy & VPN Detector - detect whether an IP is behind VPN/Proxy

2. Dependencies
	1. Framework used is Python Flask. 
	2. Setting up Flask - make sure you are in home directory
		1. sudo apt install python3-venv
		2. mkdir my_flask_app
		3. cd my_flask_app
		4. python3 -m venv sih
		5. source sih/bin/activate (execute this command in parent directory of sih to activate sih virtual environment)
		6. pip install Flask (use pip or pip3 - doesn't matter in sih virtual environment)
		7. python -m flask --version

	3. Installing necessary modules/tools/libraries in sih virtual environment
		1. sudo apt-get install -y net-tools
		2. sudo apt-get install -y nmap
		3. sudo apt install -y gcc libpcre3-dev zlib1g-dev libluajit-5.1-dev libpcap-dev openssl libssl-dev libnghttp2-dev libdumbnet-dev bison flex libdnet autoconf libtool
		4. sudo apt-get install -y wkhtmltopdf
		5. pip install setuptools
		6. pip install python3-nmap
		7. pip install shodan
		8. pip install ipwhois
		9. pip install wheel
		10. pip install json2html
		11. pip install flask-googlemaps
		12. pip install pdfkit
		13. pip install zipfile36
		14. pip install numpy

3. Usage
	1. Use following command in parent directory of sih project folder
		$ python app.py
	2. Enter an IP address in the textbox and Click on 'Submit' to check the results.

4. Team details
	1. Abhishek Kaushik - cs17b001@iittp.ac.in
	2. Nilesh Tiwari - cs17b022@iittp.ac.in
	3. Mithlesh - cs17b018@iittp.ac.in
	4. Vora Brijesh - cs17b031@iittp.ac.in
	5. Nitesh Kumar - cs17b023@iittp.ac.in
	6. Aparna Vadlamani - cs17b005@iittp.ac.in

5. College - Indian Institute of Technology Tirupati