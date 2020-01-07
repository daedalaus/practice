from flask import Markup


print(Markup('<strong>Hi %s!</strong>') % '<blink>David</blink>')
print(type(Markup('<strong>Hi %s!</strong>')))