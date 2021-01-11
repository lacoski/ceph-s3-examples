import requests
from awsauth import S3Auth

ACCESS_KEY = 'E2R228B3YF1TF6IYBZJ1'
SECRET_KEY = 'clsTQb6EtomIA6kZH54Xv0mrOnRjLyRCCNTTqiWr'

url = 'http://172.16.70.31:7480/'
r = requests.get(url, auth=S3Auth(ACCESS_KEY, SECRET_KEY, url))

print(r.text)