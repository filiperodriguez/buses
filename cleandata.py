# -*- coding: utf-8 -*-
# copyright (c) 2014 Filipe Rodrigiez
# TFL data to JSON parser
# A parser to convert TFL special data formatting to JSON for easier manipulation
#
#
import json
import re
import time


class CleanData(object):

    def clea_array(self, raw_data):
        raw_data = (raw_data.split('\n'))
        lst = []
        for lines in raw_data:
            line = re.sub(r'\[', "", lines)
            line = re.sub(r'\]', "", line)
            line = re.sub(r'"', "", line)
            lst.append(line)
        lst.pop(0)
        return lst

    def set_list(self, cleaned_data):
        clean_lst = []
        for pn in cleaned_data:
            line = pn.split(',')
            date_and_time = time.gmtime(int(line[4])/1000)
            #dt = time.strftime('%d-%m-%Y', date_and_time)
            tm = time.strftime("%H:%M", date_and_time)
            line[4] = tm
            #line.insert(5, tm)
            clean_lst.append(line)

        return clean_lst

    def set_json(self, cleaned_data):
        clean_lst = []
        for pn in cleaned_data:
            line = pn.split(',')
            date_and_time = time.gmtime(int(line[4])/1000)
            dt = time.strftime('%d-%m-%Y', date_and_time)
            tm = time.strftime("%H:%M", date_and_time)
            clean_lst.append({line[2]: {'line': line[3], 'date': dt, 'time': tm}})

        return json.dumps(clean_lst)


