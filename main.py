import argparse
import urllib
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PARSER = argparse.ArgumentParser()

REQUIRED = PARSER.add_mutually_exclusive_group(required=True)
REQUIRED.add_argument("-u", "--url", help="URL to request")
REQUIRED.add_argument("-f", "--file", help="File with URLs to request")

PARSER.add_argument("-o", "--output", required=False, default="screenshots", help="Screenshot directory")

ARGS = vars(PARSER.parse_args())

OPTIONS = Options()
OPTIONS.add_argument('--headless')
OPTIONS.add_argument('--ignore-certificate-errors')

DRIVER = webdriver.Chrome(options=OPTIONS)
DRIVER.set_window_size(1920, 1080)
DRIVER.set_page_load_timeout(5)

def screenshot(url) -> None:
    try: up = urllib.parse.urlparse(url)
    except:
        print(f'[ERROR] Failed to parse : {url}')
        return
    
    try:
        DRIVER.get(url)
    except:
        print(f'[ERRO] Failed to get : {url}')
        return

    time.sleep(4)

    path = f'{ARGS["output"]}/{up.scheme}_{up.hostname}_{up.port}.png'

    try: DRIVER.save_screenshot(path)
    except:
        print(f'[ERRO] Failed to get : {url}')
        return


def main() -> None:

    try: os.mkdir(ARGS['output'])
    except: pass

    if ARGS['url']:
        screenshot(ARGS['url'])
        print(f'[I] Completed : {url}')
        return

    if ARGS['file']:
        with open(ARGS['file'], 'r') as f:
            lines = f.readlines()
            lines = [line.rstrip('\n') for line in lines]

            for url in lines:
                screenshot(url)



if __name__ == '__main__':
    main()
