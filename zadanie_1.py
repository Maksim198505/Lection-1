# Написать метод domain_name, который вернет домен из url адреса:
# url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# url = "https://www.cnet.com"                -> domain name = "cnet"
from urllib.parse import urlparse

GENERIC_TLDS = [
    'aero', 'asia', 'biz', 'com', 'coop', 'edu', 'gov', 'info', 'int', 'jobs',
    'mil', 'mobi', 'museum', 'name', 'net', 'org', 'pro', 'tel', 'travel', 'cat'
    ]


def domain_name(url):
    hostname = urlparse(url.lower()).netloc
    if hostname == '':
        # Force the recognition as a full URL
        hostname = urlparse('http://' + url).netloc

    # Remove the 'user:passw', 'www.' and ':port' parts
    hostname = hostname.split('@')[-1].split(':')[0].lstrip('www.').split('.')

    num_parts = len(hostname)
    if (num_parts < 3) or (len(hostname[-1]) > 2):
        return '.'.join(hostname[:-1])
    if len(hostname[-2]) > 2 and hostname[-2] not in GENERIC_TLDS:
        return '.'.join(hostname[:-1])
    if num_parts >= 3:
        return '.'.join(hostname[:-2])


if __name__ == '__main__':
    print(domain_name("https://youtube.com"))
