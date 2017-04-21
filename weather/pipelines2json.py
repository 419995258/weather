# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import json
import codecs


class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d%H%M%S',time.localtime())
        fileName = today + '.json'
        with codecs.open('weather/gitFiles/json/' + fileName,'a',encoding='utf-8') as fp:
            line = json.dumps(dict(item),ensure_ascii=False) + '\n'
            fp.write(line)
            # time.sleep(1)
        return item
