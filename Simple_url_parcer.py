url = input("Введите URL: ")

def parse_url(url):

    if "https" in url:
        short_url = url.removeprefix('https://')
    elif "http" in url:
        short_url = url.removeprefix('http://')
    elif "ftp" in url:
        short_url = url.removeprefix('ftp://')

    if "www" in short_url:
        short_url = short_url[4::]

    index = short_url.index('/')
    short_url = short_url[:index]
    return short_url

print(parse_url(url))