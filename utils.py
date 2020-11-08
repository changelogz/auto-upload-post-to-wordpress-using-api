from high_order_framework_requests_python import utils_class
import requests

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

if __name__ =='__main__':
    domain = 'http://nghiahsgs.com'
    res = get_all_post(domain)
    # print(res)

    domain = 'http://nghiahsgs.com'
    id_post = 2031
    res = get_detail_one_post(domain,id_post)
    # print(res)