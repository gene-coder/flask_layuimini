# _*_ coding: utf-8 _*_

from app import db
from app.main.sa.models import LOG
from flask import session,request

def save_log(module_name,op_label,op_detail):
    user_name = session['username'] 
    user_id = session['user_id']
    user_ip = request.remote_addr
    op_url = request.path
    dt = LOG(ip=user_ip, user_id=user_id,user_name = user_name ,op_url =op_url,module_name = module_name,op_label =op_label,op_detail=op_detail)
    db.session.add(dt)
    db.session.commit()

