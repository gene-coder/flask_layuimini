# flask_layuimini
使用layuimini flask编写的后台管理页面，包含用户管理，菜单管理，角色管理。
本系统参考layui、layuimini
# 环境说明
使用了python 3.9.12，mariadb 10.10.3-MariaDB。
# 使用说明
1. 安装python mariadb(mysql)，
2. 使用pip安装python依赖包
3. 将appuser.sql导入数据库中。
4. 执行python app.py启动。
# 注意
1. 程序中，密码采用hash加密，其余数据采用ase加密。
2. 数据库配置文件在app/conf/main.ini中。
3. 系统admin默认密码为comeon。
