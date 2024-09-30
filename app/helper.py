from requests_html import HTMLSession
import json
import requests
class UsernameError(Exception):
    pass
class PlatformError(Exception):
    pass

class User:
    def __init__(self,username=None,platform=None):
        self.__username = username
        self.__platform = platform
    def codeforces(self):
        url = 'https://codeforces.com/api/user.info?handles={}'.format(self.__username)
        r = requests.get(url,timeout=10)
        if r.status_code !=200:
            raise UsernameError('User not found')
        r_data = r.json()
        if r_data['status']!='OK':
            raise UsernameError('User not found')
        data  = dict()
        data['status'] = 'OK'
        data.update(r_data['result'][0])
        return data
    def atcoder(self):
        url = "https://atcoder.jp/users/{}".format(self.__username)
        session = HTMLSession()
        r = session.get(url,timeout=10)
        if r.status_code != 200:
            raise UsernameError('User not found')
        data_tables = r.html.find('.dl-table')
        if not len(data_tables):
            raise UsernameError('User not found')
        data = dict()
        data['status']='OK'
        for table in data_tables:
            data_rows = table.find('tr')
            for row in data_rows:
                attr = row.find('th',first=True).text
                val = row.find('td',first=True).text
                data[attr]=val
                if attr == 'Highest Rating':
                    val = val.split()[0]
                    data[attr]=val
        return data
    def nowcoder(self):
        session = HTMLSession()
        url = "https://ac.nowcoder.com/acm/contest/profile/{}/".format(self.__username)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        r = session.get(url, headers=headers, timeout=10)
        
        if r.status_code != 200:
            raise UsernameError('User not found')
        check = r.html.find('.coder-name', first=True)
        if check is None:
            raise UsernameError('User not found')
        data = dict()
        data['status'] = 'OK'
        data['username'] = check.attrs.get('data-title')
        target = r.html.find('.status-item')
        for li in target:
            text = li.text.split()
            # print(text)
            if len(text)>=2 and text[1]=='Rating':
                data['rating']=text[0]
            if len(text)>=2 and text[1]=='Rating排名':
                data['ranking']=text[0]
        return data
    def get_info(self):
        if self.__platform=='codeforces':
            return self.codeforces()
        if self.__platform == 'atcoder':
            return self.atcoder()
        if self.__platform =='nowcoder':
            return self.nowcoder()
        raise PlatformError('Platform not Found')
if __name__ == '__main__':
    platform = input("Enter platform: ")
    username = input("Enter username: ")
    obj = User(username,platform)
    print(obj.get_info())
