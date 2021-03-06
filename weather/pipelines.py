# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import os.path
import urllib2


class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d%H%M%S',time.localtime())
        fileName = today + '.txt'
        with open('weather/gitFiles/txt/' + fileName,'a') as fp:
            fp.write(item['cityDate'].encode('utf-8') + '\t')
            fp.write(item['week'].encode('utf-8') + '\t')
            imgName = 'weather/gitFiles/txt/' + os.path.basename(item['img'])
            fp.write(imgName + '\t')
            if os.path.exists(imgName):
                pass
            else:
                with open(imgName,'wb') as fp:
                    response = urllib2.urlopen(item['img'])
                    fp.write(response.read())
            fp.write(item['temperature'].encode('utf-8') + '\t')
            fp.write(item['weather'].encode('utf-8') + '\t')
            fp.write(item['wind'].encode('utf-8') + '\n')
            # time.sleep(1)
        return item
