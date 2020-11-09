import base64
from high_order_framework_requests_python import utils_class
import requests
import datetime
import slugify

# utils_class.File_Interact('res.txt').write_file(res)

# 10 bai
def get_all_post(domain):
    url = '%s/wp-json/wp/v2/posts'%domain
    res = requests.get(url).json()
    return res


def get_detail_one_post(domain,id_post):
    url = '%s/wp-json/wp/v2/posts/%s'%(domain,id_post)
    res = requests.get(url).json()
    return res

def get_current_time_wp():
    now = datetime.datetime.now()
    year = '%s'%now.year
    month = '%s'%now.month
    day = '%s'%now.day
    hour = '%s'%now.hour
    minute = '%s'%now.minute
    second = '%s'%now.second

    if len(month) ==1:
        month = '0%s'%month
    if len(day) ==1:
        day = '0%s'%day
    if len(hour) ==1:
        hour = '0%s'%hour
    if len(minute) ==1:
        minute = '0%s'%minute
    if len(second) ==1:
        second = '0%s'%second

    current_time = '%s-%s-%sT%s:%s:%s'%(year,month,day, hour, minute, second)
    # print(current_time)
    return current_time

def base_64_encode(message):
    # message = "admin:password"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_string = base64_bytes.decode("ascii") 
    return base64_string


def geneate_headers(username,password):
    headers = {
        'Authorization':'Basic %s'%base_64_encode('%s:%s'%(username,password))
    }
    return headers



def auto_create_new_post(domain,username,password,title,content,categorie_id):
    headers = geneate_headers(username,password)

    slug = slugify.slugify(title)
    url = '%s/wp-json/wp/v2/posts'%domain
    data = {
        'title'   : title,
        'status'  : 'publish', # ok, we do not want to publish it immediately
        'content' : content,
        'categories' : categorie_id, # category ID
        # 'tags' : '1,4,23', # string, comma separated
        # 'date':get_current_time_wp(), # YYYY-MM-DDTHH:MM:SS
        # 'excerpt' : 'Read this awesome post',
        # 'password' : '12$45',
        'slug' : slug # part of the URL usually
        # more body params are here:
        # developer.wordpress.org/rest-api/reference/posts/#create-a-post
    }
    res = requests.post(url, data=data,headers=headers)
    res = res.json()
    src = res['guid']['raw']
    return src


def auto_upload_image(domain,username,password,filepath,title,caption):
    headers = geneate_headers(username,password)

    url = '%s/wp-json/wp/v2/media/'%domain
    filename = filepath.split('\\')[-1]

    if filename.split('.')[-1]=='png':
        Content_Type = 'image/png'
    if filename.split('.')[-1]=='jpg':
        Content_Type = 'image/jpeg'

    files = {
        'file': (filename, open(filepath, 'rb')),
        'Content-Type': Content_Type,
        'Content-Length': 1
    }

    dataPost = {
        'title':title,
        'caption':caption,
    }

    res = requests.post(url, data=dataPost,files = files,headers=headers)
    res = res.json()

    src = res['guid']['raw']
    return src

if __name__ =='__main__':
    # domain = 'http://nghiahsgs.com'
    # res = get_all_post(domain)
    # print(res)

    # domain = 'http://nghiahsgs.com'
    # id_post = 2031
    # res = get_detail_one_post(domain,id_post)
    # print(res)


    # domain = 'http://nghiahsgs.com'
    # username = 'nghiahsgs'
    # password = '261997'
    
    # title =  'day la bai viet thu nhat cua toi'
    # content = utils_class.File_Interact('data.txt').read_file()
    # categorie_id = '5'

    # link_post = auto_create_new_post(domain,username,password,title,content,categorie_id)
    # print(link_post)

    # # filepath = 'avatar.png'

    pass