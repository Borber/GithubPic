import os


def trains():
    url = input('Github URL:')
    print('CDN URL: ' + url.replace('https://github.com/', 'https://cdn.jsdelivr.net/gh/').replace('blob/master/', ''))


if __name__ == '__main__':
    C = ''
    while C != 'N':
        os.system('cls')
        trains()
        C = input('Enter N to exit the program and press Enter to continue.')
