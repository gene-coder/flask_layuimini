# -*- coding: utf-8 -*-
# 各种数据类型的转换
import json

# 元组转换为字典
def sql_to_list(data,table_title):
    # 输入1 二重元组，输入2 列表标题
    jsonData = []
    if len(data) == 0 :
        return jsonData
    elif len(data[0]) == len(table_title):
        for row in data:
            result = {}
            for i in range(0,len(table_title)):
                result[table_title[i]] = row[i]
            else:
                jsonData.append(result)
        return jsonData
    else:
        return 'error'


# 返回layui数据表格数据
## 过滤,筛选的时候用
def select_date(data,key,value):
    for i in list(reversed(data)):
        print(str(value))
        if str(value) not in str(i[key]) :
            data.remove(i) 
        else:
            pass

## 获取分页数据
def get_date_search(sql_data,table_title,url_req):
    # sql_data:sql查询结果
    # table_title：返回数据表格列标题，需要和layui数据表格一直
    # url_req：url请求

    data = sql_to_list(sql_data,table_title)
    
    # 筛选
    if url_req.get("searchParams"):
        select_dict = json.loads(url_req.get("searchParams"))
        key_list = [key for key in select_dict]
        for key in key_list:
            value=select_dict[key].strip()
            if len(str(value))>0 :
                select_date(data,key,select_dict[key])

    #分页
    limit = int(url_req.get("limit"))
    page = int(url_req.get("page"))
    start = (page - 1) * limit
    end = page * limit if len(data) > page * limit else len(data)
    ret = data[start:end]
    return {"code": 0, "msg": "", "count": len(data), "data": ret, }