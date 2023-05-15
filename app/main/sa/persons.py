# _*_ coding: utf-8 _*_

from app import db
from flask import session
from app.main.sa.models import USER, USER_ROLE, ROLE_MENU, MENU
from app.main.common.transfile import sql_to_list
from sqlalchemy.orm import aliased
from app.main.common.file_op import readfile

"""
用户信息（全）
"""


# 获取人员信息
def get_person_info(person_id):
    person_info = USER.query.filter_by(id=person_id, status=0).\
    with_entities(USER.id,USER.username,USER.user_note,USER.password).all()
    redata = sql_to_list(person_info,['id','username','user_note','password'])
    return redata[0]


# 获取当前登录人信息
def get_curr_person_info():
    return get_person_info(session['user_id'])


# 获取用户权限url
def get_permission_list(psm_id):
    per = list()
    sql = db.session.query(USER.id, USER.user_note, MENU.menu_name, MENU.url).\
        join(USER_ROLE, USER.id == USER_ROLE.user_id).\
        join(ROLE_MENU, ROLE_MENU.role_id == USER_ROLE.role_id).\
        join(MENU, ROLE_MENU.menu_id == MENU.id).\
        filter(USER.status == 0, MENU.visible == 0, USER.id == psm_id)
    use_menu = sql.all()
    for i in use_menu:
        per.append(i[3])
    return per


# 将目录转换成目录树,parent_id为第一级菜单id
## layuimini 和layui树 子菜单不同，layuimini使用child作为子菜单，layui使用children
def create_tree(json,parent_id='0',lable = 'child'):
    menu_dict = []
    for menu in json:
        if menu["parent_id"] == str(parent_id):
            menu["target"] = "_self"
            menu_dict.append(menu)
    if len(menu_dict) > 0:
        data = []
        for menu in menu_dict:
            menu[lable] = create_tree(json,menu['menu_id'],lable)
            data.append(menu)
        return data
    return []


# 获取用户权限，返回json，用来生成目录，传入user_id
web_inf=readfile('./app/conf/main.ini','ini')['web']
def get_nva_tree(psm_id=1):
    per = {"homeInfo": {
        "title": web_inf['index_title'],
        "href": "/welcome"
    },
        "logoInfo": {
        "title": web_inf['web_title'],
        "image": "/static/images/logo.png",
        "href": ""
    }}
    sql = db.session.query(USER.id, MENU.menu_name, MENU.icon, MENU.url, MENU.id, MENU.parent_id).\
        join(USER_ROLE, USER.id == USER_ROLE.user_id).\
        join(ROLE_MENU, ROLE_MENU.role_id == USER_ROLE.role_id).\
        join(MENU, ROLE_MENU.menu_id == MENU.id).\
        filter(USER.status == 0, MENU.visible == 0, USER.id == psm_id, MENU.menu_type == 1).\
        order_by(MENU.parent_id, MENU.order_num)
    use_menu = sql.all()
    lable = ['user_id', 'title', 'icon', 'href', 'menu_id', 'parent_id']
    menu_power = sql_to_list(use_menu, lable)
    per["menuInfo"] = create_tree(menu_power)
    return per


# 返回json，用来生成目录，角色页面使用
def get_menu_tree():
    sql = MENU.query.filter(MENU.visible==0).\
        with_entities(MENU.id,MENU.id,MENU.menu_name,MENU.parent_id).\
        order_by(MENU.parent_id, MENU.order_num)
    use_menu = sql.all()
    lable = ['id','menu_id','title', 'parent_id']
    menu_power = sql_to_list(use_menu, lable)
    return {"status":True,"data":create_tree(menu_power,lable='children')}