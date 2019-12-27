import requests
from requests.cookies import RequestsCookieJar

headers1 = {
    'Cookie': '_zap=0677f76d-07dd-46cf-b9a0-ff24e9542fbe; _xsrf=fe4fc969-6045-460f-808e-b06674'
              'cbd90b; d_c0="AMAsTPkFHhCPTmBvpsibmJAIotQLoGVALas=|1569672738"; Hm_lvt_98beee57'
              'fd2ef70ccdd5ca52b9740c49=1569672741; tgw_l7_route=80f350dcd7c650b07bd7b485fcab5'
              'bf7; capsion_ticket="2|1:0|10:1569679870|14:capsion_ticket|44:ODg1OGRmMmI2MDc1N'
              'DRlNmEzODU0N2E5NWE4MjcyMWM=|6930fa709437297e5640bfe24d0a11c03974643c9545eec17d2'
              '59a607b1ffc64"; z_c0="2|1:0|10:1569679892|4:z_c0|92:Mi4xbVlfM0RBQUFBQUFBd0N4TS1'
              'RVWVFQ1lBQUFCZ0FsVk5GTGg4WGdDeWN6MnhjY3VCbDQwc0d1bzM5d0xpdDU1OC13|d7b7f231dcf28'
              '01ebe8d05348ca110a3d82b2be7af3135f618d3ab9ffded90fe"; unlock_ticket="AKBlPXJMcQ'
              '4mAAAAYAJVTRxxj11PiBy88S1n6DE31aLBJXo7_rDE_w=="; tst=r; Hm_lpvt_98beee57fd2ef70'
              'ccdd5ca52b9740c49=1569679918',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/77.0.3865.90 Safari/537.36'
}

# r1 = requests.get('https://zhihu.com', headers=headers1)
# print(r1.text)


headers2 = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/77.0.3865.90 Safari/537.36'
}
cookies = '_zap=0677f76d-07dd-46cf-b9a0-ff24e9542fbe; _xsrf=fe4fc969-6045-460f-808e-b06674cbd90b; ' \
           'd_c0="AMAsTPkFHhCPTmBvpsibmJAIotQLoGVALas=|1569672738"; Hm_lvt_98beee57fd2ef70ccdd5ca52' \
           'b9740c49=1569672741; capsion_ticket="2|1:0|10:1569679870|14:capsion_ticket|44:ODg1OGRmM' \
           'mI2MDc1NDRlNmEzODU0N2E5NWE4MjcyMWM=|6930fa709437297e5640bfe24d0a11c03974643c9545eec17d2' \
           '59a607b1ffc64"; z_c0="2|1:0|10:1569679892|4:z_c0|92:Mi4xbVlfM0RBQUFBQUFBd0N4TS1RVWVFQ1l' \
           'BQUFCZ0FsVk5GTGg4WGdDeWN6MnhjY3VCbDQwc0d1bzM5d0xpdDU1OC13|d7b7f231dcf2801ebe8d05348ca11' \
           '0a3d82b2be7af3135f618d3ab9ffded90fe"; unlock_ticket="AKBlPXJMcQ4mAAAAYAJVTRxxj11PiBy88S' \
           '1n6DE31aLBJXo7_rDE_w=="; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1569679953'

jar = RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)

r = requests.get('https://www.zhihu.com', cookies=jar, headers=headers2)
print(r.text)
