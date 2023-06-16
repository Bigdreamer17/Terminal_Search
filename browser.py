import webbrowser
import sys

url = "https://www.google.com/search?q="
valild_websites = [
        'reddit.com',
        'stackoverflow.com',
        'stackexchange.com',
        'medium.com'
]

chrome_path = '/usr/bin/brave-browser %s'

def create_filter():
    filter = '('
    for index, website in enumerate(valild_websites):
        filter += 'site:' + website
        if index == len(valild_websites) - 1:
            filter += ')'
        else:
            filter += ' OR '
    return filter

# print(sys.argv[1:])

def create_query():
    query = sys.argv[1:]
    return ' '.join(query)

def create_url():
    if len(sys.argv[1:]) == 0:
        print("Error: Please enter a valid search query")
    else:
        final_url = url + create_query() + create_filter()
        webbrowser.get(chrome_path).open(final_url)

create_url()
