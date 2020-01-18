from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils.translation import ugettext as _
from django.template import loader, Context
from django.http.response import HttpResponse, HttpResponseRedirect

from mvc.models import Area, User, Category, Note
from utils import function, formatter
from tmitter.settings import *
# Create your views here.


# check user was existed
def __check_username_exist(_username):
    _exist = True

    try:
        _user = User.objects.get(username=_username)
        _exist = True
    except User.DoesNotExist:
        _exist = False

    return _exist


# response result message page
def __result_message(request,
                     _title=_('Message'),
                     _message=_('Unknown error, processing interrupted.'),
                     _go_back_url=''):
    _islogin = __is_login(request)

    if _go_back_url == '':
        _go_back_url = function.get_referer_url(request)

    # body content
    _template = loader.get_template('result_message.html')

    _context = Context({
        'page_title': _title,
        'message': _message,
        'go_back_url': _go_back_url,
        'islogin': _islogin,
    })

    output = _template.render(_context.flatten())
    return HttpResponse(output)


def __is_login(request):
    return request.session.get('islogin', False)


def __check_login(_username, _password):
    _state = {
        'success': True,
        'message': 'none',
        'userid': -1,
        'realname': '',
    }

    try:
        _user = User.objects.get(username=_username)

        # to decide password
        if function.md5_encode(_password) == _user.password:
            _state['success'] = True
            _state['userid'] = _user.id
            _state['realname'] = _user.realname
        else:
            # password incorrect
            _state['success'] = False
            _state['message'] = _('Password incorrect.')
    except User.DoesNotExist:
        # user not exist
        _state['success'] = False
        _state['message'] = _('User does not exist.')

    return _state


def __do_login(request, _username, _password):
    _state = __check_login(_username, _password)
    if _state['success']:
        request.session['islogin'] = True  # 标识已登录
        request.session['userid'] = _state['userid']  # 保存用户的id
        request.session['username'] = _username  # 保存用户名
        request.session['realname'] = _state['realname']  # 真实姓名
    return _state


# get session user id
def __user_id(request):
    return request.session.get('userid', -1)


# get session realname
def __user_name(request):
    return request.session.get('username', '')


def __do_signup(request, _userinfo):
    _state = {
        'success': False,
        'message': '',
    }

    # check username exist
    if _userinfo['username'] == '':
        _state['success'] = False
        _state['message'] = _('"Username" have not inputted.')
        return _state

    if _userinfo['password'] == '':
        _state['success'] = False
        _state['message'] = _('"Password" have not inputted.')
        return _state

    if _userinfo['realname'] == '':
        _state['success'] = False
        _state['message'] = _('"Real Name" have not inputted.')
        return _state

    if _userinfo['email'] == '':
        _state['success'] = False
        _state['message'] = _('"Email" have not inputted.')
        return _state

    # check username exist
    if __check_username_exist(_userinfo['username']):
        _state['success'] = False
        _state['message'] = _('"Username" have existed.')
        return _state

    # check password & confirm password
    if _userinfo['password'] != _userinfo['confirm']:
        _state['success'] = False
        _state['message'] = _('"Confirm Password" have not match.')
        return _state

    _user = User(
        username=_userinfo['username'],
        realname=_userinfo['realname'],
        password=_userinfo['password'],
        email=_userinfo['email'],
        area=Area.objects.filter().all()[0]
    )
    _user.save()
    return _state


def signup(request):
    _islogin = __is_login(request)  # 判断是否登录
    if _islogin:  # 如果已经登录，则重定向到根目录
        return HttpResponseRedirect('/')

    _userinfo = {  # 用户信息的数据结构
        'username': '',
        'password': '',
        'confirm': '',
        'realname': '',
        'email': '',
    }

    try:
        _userinfo = {  # 从页面获取用户的输入
            'username': request.POST['usernaem'],
            'password': request.POST['password'],
            'confirm': request.POST['confirm'],
            'realname': request.POST['realname'],
            'email': request.POST['email'],
        }
        _is_post = True
    except KeyError:
        _is_post = False

    if _is_post:  # 如果是post消息，则执行注册逻辑
        _state = __do_signup(request, _userinfo)
    else:
        _state = {
            'success': False,
            'message': _('Signup')
        }

    if _state['success']:  # 如果注册成功，则返回成功页面
        return __result_message(request, _('Signup successed'), _('Your account was registered success.'))

    _result = {  # 显示注册信息
        'success': _state['success'],
        'message': _state['message'],
        'form': {
            'username': _userinfo['username'],
            'realname': _userinfo['realname'],
            'email': _userinfo['email'],
        }
    }

    # body content
    _template = loader.get_template('signup.html')  # 渲染注册页面
    _context = {  # 配置模板参数
        'page_title': _('Signup'),
        'state': _result,
    }
    _output = _template.render(_context)
    return HttpResponse(_output)


def signin(request):
    _islogin = __is_login(request)  # 检查是否登录

    try:
        # get post params    # 获取输入用户名和密码
        _username = request.POST['username']
        _password = request.POST['password']
        _is_post = True
    except KeyError:
        _is_post = False

    # check username and password
    if _is_post:
        _state = __do_login(request, _username, _password)  # 进行登录操作

        if _state['success']:
            return __result_message(request, _('Login successed'), _('You are logied now.'))
    else:
        _state = {
            'success': False,
            'message': _('Please login first.')
        }

    # body content
    _template = loader.get_template('signin.html')  # 显示登录页面
    _context = {
        'page_title': _('Signin'),
        'state': _state,
    }
    _output = _template.render(_context)
    return HttpResponse(_output)


# user messages view and page
def index_user_page(request, _username, _page_index):
    # get user login status
    _islogin = __is_login(request)
    _page_title = _('Home')

    try:
        # get post params
        _message = request.POST['message']
        _is_post = True
    except KeyError:
        _is_post = False

    # save message
    if _is_post:
        # check login
        if not _islogin:
            return HttpResponseRedirect('/signin/')

        # save messages
        _category, _is_added_cate = Category.objects.get_or_create(name='网页')

        try:
            _user = User.objects.get(id=__user_id(request))
        except:
            return HttpResponseRedirect('/signin/')

        _note = Note(message=_message, category=_category, user=_user)
        _note.save()

        return HttpResponseRedirect('/user/' + _user.username)

    _userid = -1
    # get message list
    _offset_index = (int(_page_index) - 1) * PAGE_SIZE
    _last_item_index = PAGE_SIZE * int(_page_index)

    _login_user_friend_list = None
    if _islogin:
        # get friend messages if user is logined
        _login_user = User.objects.get(username=__user_name(request))
        _login_user_friend_list = _login_user.friend.all()
    else:
        _login_user = None

    _friends = None
    _self_home = False
    if _username != '':
        # there is get user's messages
        _user = get_object_or_404(User, username=_username)
        _userid = _user.id
        _notes = Note.objects.filter(user=_user).order_by('-addtime')
        _page_title = '%s' % _user.realname
        # get friend list
        _friends = _user.friend.order_by('id')[0:FRIEND_LIST_MAX]
        print('................', _friends)
        if _userid == __user_id(request):
            _self_home = True

    else:
        # get all messages
        _user = None

        if _islogin:
            _query_users = [_login_user]
            _query_users.extend(_login_user.friend.all())
            _notes = Note.objects.filter(
                user__in=_query_users).order_by('-addtime')
        else:
            # can't get message
            _notes = []

    # page bar
    _page_bar = formatter.page_bar(_notes, _page_index, _username)


    # get current page
    _notes = _notes[_offset_index:_last_item_index]

    # body content
    _template = loader.get_template('index.html')

    _context = {
        'page_title': _page_title,
        'notes': _notes,
        'islogin': _islogin,
        'userid': __user_id(request),
        'self_home': _self_home,
        'user': _user,
        'page_bar': _page_bar,
        'friends': _friends,
        'login_user_friend_list': _login_user_friend_list,
    }

    _output = _template.render(_context)
    return HttpResponse(_output)


# detail view
def detail(request, _id):
    # get user login status
    _islogin = __is_login(request)

    _note = get_object_or_404(Note, id=_id)

    # body content
    _template = loader.get_template('detail.html')

    _context = {
        'page_title': _('%s\'s message %s') % (_note.user.realname, _id),
        'item': _note,
        'islogin': _islogin,
        'userid': __user_id(request),
    }

    _output = _template.render(_context)
    return HttpResponse(_output)


# all users list
def users_index(request):
    return users_list(request, 1)


# all users list
def users_list(request, _page_index=1):
    # check is login
    _islogin = __is_login(request)

    _page_title = _('Everyone')
    _users = User.objects.order_by('-addime')

    _login_user = None
    _login_user_friend_list = None
    if _islogin:
        try:
            _login_user = User.objects.get(id=__user_id(request))
            _login_user_friend_list = _login_user.friend.all()
        except:
            _login_user = None

    # page bar
    _page_bar = formatter.page_bar(_users, _page_index, '',
                                   'control/userslist_pagebar.html')

    # get message list
    _offset_index = (int(_page_index) - 1) * PAGE_SIZE
    _last_item_index = PAGE_SIZE * int(_page_index)

    # get current page
    _users = _users[_offset_index:_last_item_index]

    # body content
    _template = loader.get_template('users_list.html')

    _context = {
        'page_title': _page_title,
        'users': _users,
        'login_user_friend_list': _login_user_friend_list,
        'islogin': _islogin,
        'userid': __user_id(request),
        'page_bar': _page_bar,
    }

    _output = _template.render(_context)
    return HttpResponse(_output)


# add friend
def friend_add(request, _username):
    # check is login
    _islogin = __is_login(request)
    if not _islogin:
        return HttpResponseRedirect('/signin/')

    _state = {
        'success': False,
        'message': '',
    }

    _user_id = __user_id(request)
    try:
        _user = User.objects.get(id=_user_id)
    except:
        return __result_message(request, _('Sorry'),
                                _('This user does not exist.'))

    # check friend exist
    try:
        _friend = User.objects.get(username=_username)
        _user.friend.add(_friend)
        return __result_message(
            request, _('Successed'),
            _('%s and you are friend now.') % _friend.realname
        )
    except:
        return __result_message(request, _('Sorry'),
                                _('This user does not exist.'))


# remove friend
def friend_remove(request, _username):
    """
    解除与某人的好友关系
    """
    # check is login
    _islogin = __is_login(request)
    if not _islogin:
        return HttpResponseRedirect('/signin/')

    _state = {
        'success': False,
        'message': '',
    }

    _user_id = __user_id(request)
    try:
        _user = User.objects.get(id=_user_id)
    except:
        return __result_message(request, _('Sorry'), _('This user does not exist.'))

    # check friend exist
    try:
        _friend = User.objects.get(username=_username)
        _user.friend.remove(_friend)
        return __result_message(request, _('Successed'),
                                'Friend "%s" removed.' % _friend.realname)
    except:
        return __result_message(request, _('Undisposed'),
                                'He/She does not your friend, undisposed.')


def settings(request):
    pass