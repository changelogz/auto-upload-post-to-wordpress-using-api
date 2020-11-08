# plug in 
# https://github.com/WP-API/Basic-Auth
# chay xong tool thi xoa plugin + doi mat khau

# https://developer.wordpress.org/rest-api/
# https://pypi.org/project/wordpress-api/

from high_order_framework_requests_python import utils_class
import requests



import base64
def base_64_encode(message):
    # message = "admin:password"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_string = base64_bytes.decode("ascii") 
    return base64_string

message = 'nghiahsgs:261997'
print(base_64_encode(message))


username = 'nghiahsgs'
password = '261997'
headers = {
    'Authorization':'Basic %s'%base_64_encode('%s:%s'%(username,password))
}




url = 'http://nghiahsgs.com/wp-json/wp/v2/posts'
data = {
    'title'   : 'My test',
    # 'status'  : 'draft', # ok, we do not want to publish it immediately
    'content' : 'lalala',
    'categories' : 5, # category ID
    'tags' : '1,4,23', # string, comma separated
    'date':'2015-05-05T10:00:00', # YYYY-MM-DDTHH:MM:SS
    'excerpt' : 'Read this awesome post',
    # 'password' : '12$45',
    'slug' : 'new-test-post' # part of the URL usually
    # more body params are here:
    # developer.wordpress.org/rest-api/reference/posts/#create-a-post
}
res = requests.post(url, data=data,headers=headers)
print(res)

utils_class.File_Interact('res.txt').write_file(res.text)