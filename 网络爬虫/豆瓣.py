import  requests
import hashlib
password =str ('sdfs')
jiami = hashlib.sha1(password.encode('utf-8')).hexdigest()
print(jiami)