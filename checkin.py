# -*- coding: utf-8 -*-
import logging
import requests
import os
import json
# url
url = "https://glados.rocks/api/user/checkin"
# cookie
cookie = os.environ["COOKIE"]

payload = "{\"token\":\"glados.network\"}"
headers = {
  'authority': 'glados.rocks',
  'accept': 'application/json, text/plain, */*',
  'dnt': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
  'content-type': 'application/json;charset=UTF-8',
  'origin': 'https://glados.rocks',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://glados.rocks/console/checkin',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': cookie
}
def do_action():
    logger = logging.getLogger()
    response = requests.request("POST", url, headers=headers, data = payload)
    result = response.text.encode('utf8')

    result_json = json.loads(result)
    message = result_json['message']
    logger.info(result_json)
    print('*******************************************\n')
    print('Result : {message}!  \n'.replace('message',message))
    print('*******************************************')
    return result


if __name__ == '__main__':
    do_action()
