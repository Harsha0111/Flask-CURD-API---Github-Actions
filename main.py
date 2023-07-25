from flask import Flask, jsonify, request

app = Flask(__name__)

persons = [
    {
        'id': 1,
        'name': "Abi"
    },
    {
        'id': 2,
        'name': "Banu"
    }
]

# home


@app.route('/')
def home():
    return "Hello to Api"

# GET /person


@app.route('/persons')
def get_all_persons():
    return jsonify({'persons': persons})

# POST /person


@app.route('/person', methods=['POST'])
def create_person():
    req_id = request.get_json()
    global persons

    if "id" not in persons:
        # If "id" key is not present in the data, generate a new unique ID
        if persons:
            # Get the last ID from the list and increment it by 1
            new_id = persons[-1]["id"] + 1
        else:
            # If the list is empty, start with ID 1
            new_id = 1
    new_person = {
        'id':   new_id,
        'name': req_id['name']
    }
    persons.append(new_person)
    return jsonify(new_person)


# UPDATE
@app.route('/person', methods=['PUT'])
def update_dictionary():
    req_id = request.get_json()



# DELETE

# @app.route('/person/<string:id>', methods=['DELETE'])
# req_id = request.get_json()
# updated_list = delete_id(persons, req_id)
# if len(updated_list) < len(persons):
#     print(f"Dictionary with id={id} deleted successfully.")
#     print(updated_list)
# else:
#     print(f"Dictionary with id={id} not found in the list.")
app.run(port=5009, debug=True)
