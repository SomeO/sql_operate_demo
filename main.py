from flask import Flaskfrom sql_operate.sql import init_orm_proxyfrom sql_operate.orm_proxy import ORMProxyfrom flask import requestimport jsonfrom lib import data_libapp = Flask(__name__)init_orm_proxy(app)@app.route('/')def home():    return 'home_page'@app.route('/healthy')def healthy():    return 'healthy'@app.route('/v1/api/get_id', methods=['GET'])def get_id():    page_index = int(request.args.get('page_index'))    data_count_per_page = int(request.args.get('data_count_per_page'))    with app.app_context():        orm_proxy = ORMProxy()        list_data = orm_proxy.find_eqx_parsed_by_paginate(page_index, data_count_per_page)        res = {data.id: data.name for data in list_data}    return json.dumps(res)@app.route('/vi/api/get_data')def get_data():    data_id = int(request.args.get('id'))    with app.app_context():        orm_proxy = ORMProxy()        data = orm_proxy.find_eqx_parsed_by_id(data_id)        dict_data = data_lib.sql_data_to_dict(data)    return json.dumps(dict_data)if __name__ == '__main__':    app.run()