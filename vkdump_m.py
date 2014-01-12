# coding:utf-8
import requests
import re
from time import sleep
import os
import sys
import getopt
import logging

logging.basicConfig(level="INFO")

class VkAgent:
    def __init__(self, params):
        r = requests.get("http://m.vk.com/")  # mobile version better for parsing w/o api
        url = re.findall(r'action="(.*?)"', r.text)[0]
        r = requests.post(url, params=params)
        self.headers = r.request.headers
        self.cookies = r.cookies

    def get(self, url):
        sleep(1)
        r = requests.get(url, headers=self.headers, cookies=self.cookies)
        return r.content


def main(email, password, aim_id, folder):
    vk = VkAgent(params={"email": email, "pass": password})
    try:
        data = vk.get("http://m.vk.com/audios%s" % aim_id)
        cnt = int(re.findall(r'<em class\="tab_counter">([0-9,]+)<\/em>', data)[0].replace(',', ''))
    except:
    	logging.error("Can't count audios")
        exit()
    try:
    	os.mkdir(folder)
    except:
    	pass
    for i in range(0, cnt, 50):
        logging.info(u"Offset %s" % i)
        data = vk.get("http://m.vk.com/audios%s?offset=%s" % (aim_id, i)).split('<div class="ai_label">')[1:]
        for d in data:
            artist = re.findall(r'"ai_artist">(.*?)<\/span>', d)[0]
            title = re.findall(r'"ai_title">(.*?)<\/span>', d)[0]
            link = re.findall(r'<input type="hidden" value="(.*?)"', d)[0]
            
            fname = "%s - %s" % (artist, title)
            fname = fname.replace("/", " ")[:200] + ".mp3"
            logging.info(u"Saving file %s" % fname)
            if not os.path.isfile(fname):
                f = open(folder + '/' + fname, 'wb')
                content = vk.get(link)
                f.write(content)
                f.close()


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "u:p:i:f:", ["help", "output="])
    param = dict(opts)
    main(param['-u'], param['-p'], param['-i'], param['-f'])