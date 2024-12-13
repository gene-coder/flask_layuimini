# _*_ coding: utf-8 _*_


import json
from flask import session, redirect, render_template, request
import uuid
from app.main.common.cryption import bcrypt_encrypt,bcrypt_verify
from app import db
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func
from app.main.sa.models import USER, USER_ROLE, ROLE_MENU, MENU, ROLE
from app.main.sa import system
from app.main.sa.persons import get_nva_tree, get_curr_person_info, get_menu_tree
from app.main.sa.decorated import user_login, user_only_login
from app.main.common.transfile import get_date_search, sql_to_list
from app.main.common.captcha import generate_captcha

# 模板 登入页面 login.html 登入成功跳转页面，
# 模板页面
@system.route('/user/index')
@user_only_login
def index():
    user_info = get_curr_person_info()
    return render_template('index.html', data=user_info)


# 生成验证码
@system.route('/user/captcha')
def captcha():
    text,img = generate_captcha()
    session['captcha'] = text
    return {'status': 'OK',"file_src" : img.decode()}


# 用户登录，验证session
@system.route("/user/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        rdata = dict()
        if "username" not in request.form.to_dict():
            return redirect('/')
        user_name = request.form.get('username')
        user_pwd = request.form.get('password')
        user_captcha = request.form.get('captcha')
        rel_captcha = session['captcha']
        if 'user_id' in session:
            rdata['status'] = True
            rdata['msg'] = "已经登入~"
        else:
            if user_captcha.upper() == rel_captcha.upper():
                person = USER.query.filter(
                    USER.status == 0, USER.username == user_name).first()
                if person:
                    if bcrypt_verify(user_pwd,person.password):
                        session['username'] = user_name
                        session['user_id'] = person.id
                        rdata['status'] = True
                        rdata['msg'] = "登入成功"
                    else:
                        rdata['status'] = False
                        rdata['msg'] = "用户名或密码错误~"
                else:
                    rdata['status'] = False
                    rdata['msg'] = "用户名或密码错误~"
            else:
                rdata['status'] = False
                rdata['msg'] = "验证码错误~"
        return rdata
    else:
        return redirect('/')


# 用户注销
@system.route("/user/logout", methods=["GET", "POST"])
@user_only_login
def logout():
    rdata = dict()
    session.pop("user_id", None)
    session.pop('permission', None)
    rdata['status'] = True
    return redirect('/')


# 用户菜单导航返回
@system.route("/user/nav", methods=["GET", "POST"])
@user_only_login
def nav():
    user_id = session['user_id']
    rdata = get_nva_tree(user_id)
    return json.dumps(rdata, ensure_ascii=False)


@system.route("/user/chpasswd", methods=["GET", "POST"])
@user_only_login
def chpasswd():
    if request.method == 'POST':
        oldpassword = request.form.get('oldpassword')
        newpassword = request.form.get('newpassword')
        user_info = get_curr_person_info()
        if bcrypt_verify(oldpassword,user_info['password']):
            user_id = session['user_id']
            user_data = USER.query.filter(USER.id == user_id).first()
            user_data.password = bcrypt_encrypt(newpassword)
            db.session.commit()
            return json.dumps({'status': True, 'msg': '修改成功'}, ensure_ascii=False)
        else:
            return json.dumps({'status': False, 'msg': '原始密码错误'}, ensure_ascii=False)
    else:
        return redirect('/')

###
# 以下是权限管理，分为菜单，角色，用户，管理。
###



# 1、菜单管理
# 1.1、返回页面
@system.route("/permission/menu")
@user_login
def menu_page():
    print(request)
    return render_template('/system/permission/menu_manager.html')


# 1.2、返回menu数据，数据列表
@system.route("/permission/menu_list")
@user_only_login
def menu_list():
    p_menu = aliased(MENU)
    sql = db.session.query(MENU.id, MENU.menu_name, p_menu.menu_name, MENU.order_num, MENU.url, MENU.menu_type,
                           MENU.visible, MENU.icon, MENU.remark, MENU.parent_id).\
        join(p_menu, MENU.parent_id == p_menu.id).\
        filter(MENU.visible == 0)
    url_req = request.args
    table_title = ['id', 'menu_name', 'par_menu', 'order_num',
                   'herf', 'menu_type', 'visible', 'icon', 'remark', 'parent_id']
    rdata = get_date_search(sql.all(), table_title, url_req)
    return rdata


# 1.2、返回菜单，添加目录页面使用
@system.route("/permission/allmenu")
@user_only_login
def allmenu():
    p_menu = aliased(MENU)
    sql = db.session.query(MENU.id, MENU.menu_name, p_menu.menu_name, MENU.order_num, MENU.url,
                           MENU.menu_type, MENU.visible, MENU.icon).\
        join(p_menu, MENU.parent_id == p_menu.id).\
        filter(MENU.visible == 0).\
        order_by(MENU.parent_id, MENU.order_num)
    data = sql.all()
    table_title = ['id', 'menu_name', 'par_menu',
                   'order_num', 'herf', 'menu_type', 'visible', 'icon']
    rdata = sql_to_list(data, table_title)
    return rdata


# 1.3、添加菜单，修改菜单。修改为删除后添加。
@system.route("/permission/add_menu", methods=["GET", "POST"])
@user_only_login
def add_menu():
    if request.method == 'POST':
        menu_id = request.form.get('menu_id')
        url = request.form.get('url')
        menu_name = request.form.get('menu_name')
        par_menu = request.form.get('par_menu')
        icon = request.form.get('icon')
        order_num = request.form.get('order_num')
        datadesc = request.form.get('datadesc')
        user = get_curr_person_info()
        # 查看是否有相同的menu_id，有相同的，则先删除
        MENU.query.filter(MENU.id == menu_id).delete()
        dt = MENU(id=menu_id.strip(), menu_name=menu_name, parent_id=par_menu.strip(), order_num=order_num,
                  url=url, menu_type=1, visible=0, icon=icon, create_by=user['id'], remark=datadesc)
        db.session.add(dt)
        db.session.commit()
        return json.dumps({'status': True, 'msg': '操作完成'}, ensure_ascii=False)
    else:
        return redirect('/')


# 1.4、删除菜单
@system.route("/permission/delete_menu", methods=["GET", "POST"])
@user_only_login
def delete_menu():
    if request.method == 'POST':
        menu_id = request.form.get('menu_id')
        MENU.query.filter(MENU.id == menu_id).update({"visible": "1"})
        db.session.commit()
        return json.dumps({'status': True, 'msg': '操作完成'}, ensure_ascii=False)
    else:
        return redirect('/')


# 2、角色管理
# 2.1、返回页面
@system.route("/permission/role")
@user_login
def role_page():
    return render_template('/system/permission/role_manager.html')


# 2.2、返回role列表
@system.route("/permission/role_list")
@user_only_login
def role_list():
    sql = db.session.query(ROLE.id, ROLE.role_name, ROLE.remark,
                           func.group_concat(MENU.id), func.group_concat(MENU.menu_name)).\
        join(ROLE_MENU, ROLE.id == ROLE_MENU.role_id, isouter=True).\
        join(MENU, MENU.id == ROLE_MENU.menu_id, isouter=True).\
        filter(ROLE.status == 0).\
        group_by(ROLE.id,ROLE.role_name, ROLE.remark).\
        order_by(ROLE.id)
    url_req = request.args
    table_title = ['id', 'role_name', 'remark', 'ids', 'menus']
    rdata = get_date_search(sql.all(), table_title, url_req)
    return rdata


# 2.3、返回目录树，添加角色权限使用
@system.route("/permission/menu_tree")
@user_only_login
def menu_tree():
    rdata = get_menu_tree()
    return json.dumps(rdata, ensure_ascii=False)


# 2.4、添加role：
@system.route("/permission/add_role", methods=["GET", "POST"])
@user_only_login
def add_role():
    if request.method == 'POST':
        role_id = request.form.get('role_id')
        role_name = request.form.get('role_name')
        datadesc = request.form.get('datadesc')
        tree_select = request.form.get('tree_select')
        curr_user = get_curr_person_info()

        # role表新增内容，如果有，先删除。
        ROLE.query.filter(ROLE.id == role_id).delete()
        dt = ROLE(id=role_id, role_name=role_name, status=0,
                  create_by=curr_user['id'], remark=datadesc)
        db.session.add(dt)
        db.session.commit()

        # role_nemu表新增内容。如果有，则删除
        delete_datas = ROLE_MENU.query.filter(
            ROLE_MENU.role_id == role_id).all()
        for delete_data in delete_datas:
            db.session.delete(delete_data)

        data = []
        for select in tree_select.split(','):
            id = str(uuid.uuid4()).split('-')[0]
            data.append(ROLE_MENU(role_id=role_id,
                        menu_id=select.strip(), id=id))
        db.session.add_all(data)
        db.session.commit()
        return json.dumps({'status': True, 'msg': '操作完成'}, ensure_ascii=False)

    else:
        return redirect('/')


# 2.4、删除角色
@system.route("/permission/delete_role", methods=["GET", "POST"])
@user_only_login
def delete_role():
    if request.method == 'POST':
        role_id = request.form.get('role_id')

        # 删除role_menu表数据
        delete_datas = ROLE_MENU.query.filter(
            ROLE_MENU.role_id == role_id).all()
        for delete_data in delete_datas:
            db.session.delete(delete_data)

        # 将role表中的数据改成不可见
        ROLE.query.filter(ROLE.id == role_id).update({"status": "1"})
        db.session.commit()
        return json.dumps({'status': True, 'msg': '操作完成'}, ensure_ascii=False)
    else:
        return redirect('/')


# 3、用户管理
# 3.1、返回页面
@system.route("/permission/user")
@user_login
def user_page():
    return render_template('/system/permission/user_manager.html')


# 3.2、返回用户列表
@system.route("/permission/user_list")
@user_only_login
def user_list():
    sql = db.session.query(USER.id, USER.username, USER.user_note, USER.status, USER.remark, func.group_concat(ROLE.id), func.group_concat(ROLE.role_name)).\
        join(USER_ROLE, USER.id == USER_ROLE.user_id, isouter=True).\
        join(ROLE, USER_ROLE.role_id == ROLE.id, isouter=True).\
        filter(USER.del_flag == 0).\
        group_by(USER.id).\
        order_by(USER.id)
    url_req = request.args
    table_title = ['id', 'username', 'user_note',
                   'status', 'remark', 'roleids', 'rolenames']
    rdata = get_date_search(sql.all(), table_title, url_req)
    return rdata


# 3.3、返回角色，添加角色权限使用
@system.route("/permission/allrole")
@user_only_login
def allrole():
    sql = ROLE.query.filter(ROLE.status == 0).with_entities(
        ROLE.id, ROLE.role_name).order_by(ROLE.id)
    data = sql.all()
    table_title = ['id', 'role_name']
    rdata = sql_to_list(data, table_title)
    return rdata


# 3.4、添加用户：
@system.route("/permission/add_user", methods=["GET", "POST"])
@user_only_login
def add_user():
    if request.method == 'POST':
        curr_user = get_curr_person_info()
        data = request.form
        op_type = data.get('type')  # 操作是新增还是修改
        user_id = data.get('user_id')
        status = data.get('status')
        username = data.get('username')
        user_note = data.get('user_note')
        password = bcrypt_encrypt(data.get('password'))
        datadesc = data.get('datadesc')
        status = 0 if status == 'on' else '1'
        role_all = []
        for i in data:
            if i[:5] == 'role_':
                role_all.append(i[5:])

        # user表新增内容，如果有，先删除。
        if op_type == 'add':
            user_num = USER.query.filter(USER.username == username).count()
            if user_num == 0:
                USER.query.filter(USER.id == user_id).delete()
                dt = USER(id=user_id, username=username, user_note=user_note, password=password,status=status,
                           del_flag=0, create_by=curr_user['id'], remark=datadesc)
                db.session.add(dt)
                db.session.commit()
            else:
                return json.dumps({'status': False, 'msg': '登入名已存在'}, ensure_ascii=False)
        else:
            user_data = USER.query.filter(USER.id == user_id).first()
            user_data.username = username
            user_data.user_note = user_note
            user_data.status = status
            user_data.remark = datadesc
            db.session.commit()

        # user_role表新增内容。如果有，则删除
        delete_datas = USER_ROLE.query.filter(
            USER_ROLE.user_id == user_id).all()
        for delete_data in delete_datas:
            db.session.delete(delete_data)

        data = []
        for role_id in role_all:
            id = str(uuid.uuid4()).split('-')[0]
            data.append(USER_ROLE(role_id=role_id, user_id=user_id, id=id))
        db.session.add_all(data)
        db.session.commit()

        return json.dumps({'status': True, 'msg': '操作完成'}, ensure_ascii=False)

    else:
        return redirect('/')


# 3.5、删除用户
@system.route("/permission/delete_user", methods=["GET", "POST"])
@user_only_login
def delete_user():
    if request.method == 'POST':
        user_id = request.form.get('user_id')

        # 删除role_menu表数据
        delete_datas = USER_ROLE.query.filter(
            USER_ROLE.user_id == user_id).all()
        for delete_data in delete_datas:
            db.session.delete(delete_data)

        # 将role表中的数据改成不可见
        USER.query.filter(USER.id == user_id).update({"del_flag": "1"})
        db.session.commit()
        return json.dumps({'status': True, 'msg': '操作完成'}, ensure_ascii=False)
    else:
        return redirect('/')
 
    
# 3.6 重置密码
@system.route("/permission/resetpasswd", methods=["GET", "POST"])
@user_only_login
def resetpasswd():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        user_data = USER.query.filter(USER.id == user_id).first()
        user_data.password = bcrypt_encrypt('Abc@12345')
        db.session.commit()
        return json.dumps({'status': True, 'msg': '密码修改为：Abc@12345'}, ensure_ascii=False)
    else:
        return redirect('/')