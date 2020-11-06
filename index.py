# https://developer.wordpress.org/rest-api/
# https://pypi.org/project/wordpress-api/

from high_order_framework_requests_python import utils_class


import requests


url = 'http://nghiahsgs.com/wp-json/wp/v2/posts'
res = requests.get(url).json()

# print(res)
# res[0]


id_post = 2165
url = 'http://nghiahsgs.com/wp-json/wp/v2/posts/%s'%(id_post)
# res = requests.get(url).json()


import base64
def base_64_encode(message):
    # message = "admin:password"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return '%s'%base64_bytes

username = 'nghiahsgs'
password = '261997'
headers = {
    'Authorization':'Basic %s'%base_64_encode('%s:%s'%(username,password))
}
print(headers)