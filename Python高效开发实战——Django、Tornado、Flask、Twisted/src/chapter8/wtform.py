from flask_wtf.file import FileAllowed
from flask_wtf.form import Form
from wtforms import StringField, BooleanField, HiddenField, TextAreaField, DateTimeField, FileField


class BaseForm(Form):
    id = HiddenField('id')


class BulletinForm(BaseForm):
    dt = DateTimeField('发布时间', format='%Y-%m-%d %H:%M:%S')
    title = StringField('标题')
    content = TextAreaField('详情')
    valid = BooleanField('是否有效')
    source = StringField('来源')
    author = StringField('作者')
    image = FileField('上传图片', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
