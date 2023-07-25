from flask import Flask, jsonify ,request

app = Flask(__name__)

options = [
    {
        'ip': '1.1.1.1',
        'tools': [
            {
                'name': 'Java',
                'version': 8,
                'port': 9090
            }
        ]
    },
    {
       'ip': '1.1.1.2',
        'tools': [
            {
                'name': 'Jenkins',
                'version': 7,
                'port': 8080
            }
        ]
    }
]

# msg = [
#     {
#        'status': 'Installing Java 7'
#     },
#     {
#        'status': 'Installing Jenkins 3 on port 8080'
#     }
# ]
@app.route('/')
def home():
    return "Hello to Api"

#GET /option 
@app.route('/option' )
def get_all_options():
    return jsonify({'options': options})  

#GET /option/<string:ip>
@app.route('/option/<string:ip>' )
def get_option(ip):
    for option in options:
        if option['ip'] == ip:
            return jsonify(option)
    return jsonify({'msg': 'option not found'})

#GET /option/<string:ip>/tool
@app.route('/option/<string:ip>/tool')
def get_tools_in_option(ip):
    for option in options:
        if option['ip'] == ip:
            return jsonify({'tools': option['tools']})
    return jsonify({'msg': 'option not found'})  
    

#POST /option  ip: {address}
@app.route('/option', methods=['POST'])
def create_option():
    req_ip = request.get_json()
    new_option= {
        'ip' : req_ip['ip'],
        'tools' : []
    }
    options.append(new_option)
    return jsonify(new_option)


#POST /option/<string:ip>/tool {name:, version:, port:}
@app.route('/option/<string:ip>/tool', methods=['POST'])
def create_tool_in_option(ip):
    req_ip = request.get_json()
    for option in options:
        if option['ip'] == ip:
            new_tool = {
               'name' : req_ip['name'],
               'version' : req_ip['version'],
               'port' : req_ip['port']
            }
            option['tools'].append(new_tool)
            # msg = [
            #     {
            #         'status': 'Installing' req_ip['name']
            #     },
            #     {
            #         'status': 'Installing' req_ip['version']  req_ip['port']
            #     }
            #     ]
            #return jsonify ({'msg': msg })
           
            return jsonify (f"{ req_ip['name']} is the tool , version is {req_ip['version']} and installed on {req_ip['port']} port")

    return jsonify({'msg': 'option not found'})

#UPDATE 
@app.route('/option/<string:ip>', methods=['PUT'])
def update(ip):
    req_ip = request.get_json()
    for update_option in options:
    #   if update_option.get('ip', 0) == ip:
         if update_option['ip'] == ip:
            update_tool = {
               'name' : req_ip['name'],
               'version' : req_ip['version'],
               'port' : req_ip['port']
            }
            update_option['tools'].append(update_tool)
            return jsonify (f"{ req_ip['name']} is the tool , version is {req_ip['version']} and installed on {req_ip['port']} port")

    return jsonify({'msg': 'option not found'})
    


#DELETE 
@app.route('/option/<string:ip>', methods=['DELETE'])
def delete(ip):
    global options
    options =  list(filter( lambda dictionary: dictionary['ip'] != ip, options ))
    return jsonify ({'msg' : options})

 




app.run(port=5005, debug=True)

 

