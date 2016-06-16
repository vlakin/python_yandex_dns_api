#!/usr/bin/env python2

from yadns.yadns import get_sub_id, add_ip, del_ip

token="S6HCXK46Z44397S4QOTZZGFDTJVEO2QEVQC5AFXLGJ7XZZZJLLPQ"
domain="test.com"
ip="127.0.0.1"

# Checking record existance 
# [] - do not exists
sub_id = get_sub_id(domain,ip,token)
print sub_id

# Adding IP
add_status = add_ip(domain,ip,token)
print add_status

# Checking record existance 
# 24999289 - record exists
sub_id = get_sub_id(domain,ip,token)
print sub_id

# Deleting IP
del_status = del_ip(domain,ip,token)
print del_status

# Checking record existance 
# [] - do not exists
sub_id = get_sub_id(domain,ip,token)
print sub_id

