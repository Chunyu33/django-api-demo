if __name__ == '__main__':
    import requests
    import urllib3
    import re

    def get_out_ip():
        """
        获取公网ip
        """
        ip = ''
        try:
            res = requests.get('https://myip.ipip.net', timeout=5, verify=False).text
            ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)', res)
            ip = ip[0] if ip else ''
        except Exception as err:
            print('错误:{}'.format(err))
        return ip


    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    ip_add = get_out_ip()
    print('ip地址为:{}'.format(ip_add))
