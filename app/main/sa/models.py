# _*_ Coding:utf-8 _*_

from app import db
from app.main.common.pubstatic import guid
from datetime import datetime



# 人员信息
class USER(db.Model):
    __tablename__ = "t_user"
    # __table_args__ = {"useexisting": True}
    id = db.Column(db.String(64), doc='用户ID',primary_key=True)
    username = db.Column(db.String(64), doc='登录账号')
    user_note = db.Column(db.String(64), doc='用户昵称')
    user_type = db.Column(db.String(64), doc='用户类型')
    email = db.Column(db.String(64), doc='用户邮箱')
    phone = db.Column(db.String(64), doc='手机号')
    sex = db.Column(db.Integer, doc='用户性别')
    avatar = db.Column(db.String(64), doc='头像路径')
    password = db.Column(db.String(64), doc='密码')
    salt = db.Column(db.String(64), doc='盐加密')
    status = db.Column(db.Integer, doc='帐号状态')
    del_flag = db.Column(db.Integer, doc='删除标志')
    login_ip = db.Column(db.String(64), doc='最后登陆IP')
    login_date = db.Column(db.String(64), doc='最后登陆时间')
    create_by = db.Column(db.String(64), doc='创建者')
    created_at = db.Column(db.String(64), default=datetime.now(),doc='创建时间')
    remark = db.Column(db.String(64), doc='备注')


# 用户与角色关联表
class USER_ROLE(db.Model):
    __tablename__ = "t_user_role"
    user_id = db.Column(db.String(64), doc='用户ID')
    role_id = db.Column(db.String(64), doc='角色id')
    created_at = db.Column(db.String(64),default=datetime.now(), doc='创建时间')
    id = db.Column(db.String(64), doc='id',primary_key=True)



# 角色表
class ROLE(db.Model):
    __tablename__ = "t_role"
    # __table_args__ = {"useexisting": True}
    id = db.Column(db.String(64), doc='角色ID',primary_key=True)
    role_name = db.Column(db.String(64), doc='角色名称')
    role_key = db.Column(db.String(64), doc='角色权限字符串')
    role_sort = db.Column(db.Integer, doc='显示顺序')
    data_scope = db.Column(db.Integer, doc='数据范围')
    status = db.Column(db.Integer, doc='角色状态')
    create_by = db.Column(db.String(64), doc='创建者')
    created_at = db.Column(db.String(64),default=datetime.now(), doc='创建时间')
    remark = db.Column(db.String(64), doc='备注')

# 角色与菜单表
class ROLE_MENU(db.Model):
    __tablename__ = "t_role_menu"
    role_id = db.Column(db.String(64), doc='角色ID')
    menu_id = db.Column(db.String(64), doc='菜单ID')
    created_at = db.Column(db.String(64),default=datetime.now(), doc='创建时间')
    id = db.Column(db.String(64), doc='id',primary_key=True)


# 菜单表
class MENU(db.Model):
    __tablename__ = "t_menu"
    # __table_args__ = {"useexisting": True}
    id = db.Column(db.String(64), doc='菜单ID',primary_key=True)
    menu_name = db.Column(db.String(64), doc='菜单名称')
    parent_id = db.Column(db.Integer, doc='父菜单ID')
    order_num = db.Column(db.Integer, doc='显示顺序')
    url = db.Column(db.String(64), doc='请求地址')
    menu_type = db.Column(db.Integer, doc='菜单类型')
    visible = db.Column(db.Integer, doc='菜单状态')
    perms = db.Column(db.String(64), doc='权限标识')
    icon = db.Column(db.String(64), doc='菜单图标')
    is_frame = db.Column(db.Integer, doc='是否外链')
    create_by = db.Column(db.String(64), doc='创建者')
    created_at = db.Column(db.DateTime, default=datetime.now(), doc='创建时间')
    remark = db.Column(db.String(64), doc='备注')


# 系统日志
class LOG(db.Model):
    __tablename__ = "t_log"
    id = db.Column(db.Integer, doc='操作id',primary_key=True)
    ip = db.Column(db.String(64), doc='操作者IP')
    user_id = db.Column(db.String(36), doc='操作者ID')
    user_name = db.Column(db.String(36), doc='用户名称')
    op_url =  db.Column(db.String(2048), doc='操作链接')
    module_name = db.Column(db.String(36), doc='操作简写')
    op_label = db.Column(db.String(36), doc='操作简写')
    op_detail = db.Column(db.Text, doc='描述')
    created_at = db.Column(db.DateTime, default=datetime.now, doc='操作时间')

