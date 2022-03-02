import requests
url = 'https://raw.githubusercontent.com/is-tech-y24-2/labs-list/master/README.md'


def get_description_lab(lab):
    respond = requests.get(url)
    s = str(respond.text)
    data = [x for x in s.split('\n') if x != '']
    start = data.index(f'## {lab} лабораторная')
    if lab != 5:
        end = data.index(f'## {lab + 1} лабораторная')
    else:
        end = len(data)
    return data[start:end]
