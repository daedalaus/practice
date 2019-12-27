from urllib.robotparser import RobotFileParser
from urllib.request import urlopen, Request

# rp = RobotFileParser()
# rp.set_url('http://www.jianshu.com/robots.txt')
# # rp = RobotFileParser('https://www.jianshu.com/robots.txt')
# rp.read()
# rp.read()
# print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))

# rp = RobotFileParser()
# rp.set_url('http://www.musi-cal.com/robots.txt')
# rp.read()
# print(rp.can_fetch('*', 'http://www.musi-cal.com/cgi-bin/search?city=San+Francisco'))
# print(rp.can_fetch('*', 'http://www.musi-cal.com/wp-admin/'))

req = Request('http://www.jianshu.com/robots.txt', headers={'User-Agent':'Mozilla/5.0 3578.98 Safari/537.36'})

rp = RobotFileParser()
rp.parse(urlopen(req).read().decode().split('\n'))
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
