#!/usr/bin/env python2
import json
import base64
from urllib import urlencode
from urllib2 import urlopen, Request

# Documentation https://tech.yandex.ru/pdd/doc/concepts/api-dns-docpage/

def get_sub_id(domain,ip,token):
    base_params = {
        'domain': domain,
    }
    r_id = []
    dnsrequest = Request("https://pddimp.yandex.ru/api2/admin/dns/list?" + urlencode(base_params))
    dnsrequest.add_header("PddToken", token)
    #print "Request Method:", dnsrequest.get_method()
    data = urlopen(dnsrequest)
    resp = json.load(data)
    records = resp['records']
    for record in records:
        if (ip == ''):
            if (record['type'] == "A" and record['fqdn'] == domain):
                r_id.append(record['record_id'])
        else:
            if (record['content'] == ip and record['type'] == "A" and record['fqdn'] == domain):
                r_id = record['record_id']
    return r_id

def del_ip(domain,ip,token):
    sub_id = get_sub_id(domain,ip,token)
    base_params = {
        'domain': domain,
        'record_id': sub_id,
    }
    #print "Sub ID:", sub_id
    dnsrequest = Request("https://pddimp.yandex.ru/api2/admin/dns/del", urlencode(base_params))
    dnsrequest.add_header("PddToken", token)
    #print "Del Request:", dnsrequest.get_full_url()
    #print "Request Method:", dnsrequest.get_method()
    data = urlopen(dnsrequest)
    resp = json.load(data)
    return resp

def add_ip(domain,ip,token):
    sub_id = get_sub_id(domain,ip,token)
    base_params = {
        'domain': domain,
        'type': "A",
        'content': ip,
    }
    dnsrequest = Request("https://pddimp.yandex.ru/api2/admin/dns/add", urlencode(base_params))
    dnsrequest.add_header("PddToken", token)
    #print "Add Request:", dnsrequest.get_full_url()
    #print "Request Method:", dnsrequest.get_method()
    data = urlopen(dnsrequest)
    resp = json.load(data)
    return resp
