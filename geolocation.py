"""
Geolocation
"""
import re
import requests

class Geolocation():
    '''
    class geolocation
    search our IP then get Ip info
    '''
    def __init__(self):
        self.current_ip=''
        self.ip_info_data=''

    def get_current_ip(self):
        '''
        method - return current IP
        '''
        ip_data=requests.get('http://checkip.dyndns.com/').text
        ip_pattern=re.compile(r'(\d){1,3}.(\d){1,3}.(\d){1,3}.(\d){1,3}')
        IP=re.search(ip_pattern,ip_data)
        self.current_ip=str(IP.group())

    def get_ip_info(self):
        '''
        method - return ip info
        '''
        URL='http://ipinfo.io/'+self.current_ip+'/json'
        ip_info_response=requests.get(URL)
        ip_info_data=ip_info_response.json()
        print('IP info')
        print('*'*6)
        hostname=ip_info_data['hostname']
        city=ip_info_data['city']
        region=ip_info_data['region']
        country=ip_info_data['country']
        loc=ip_info_data['loc']
        org=ip_info_data['org']
        print(f"\nHostname: {hostname}\n"\
        f"City: {city}\n"\
        f"Region: {region}\n"\
        f"Country: {country}\n"\
        f"location: {loc}\n"\
        f"Provider: {org}\n")

def __main__():
    geolocation=Geolocation()
    geolocation.get_current_ip()
    geolocation.get_ip_info()

if __name__=='__main__':
    __main__()
