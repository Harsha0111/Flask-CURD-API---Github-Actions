from flask import Flask, jsonify, request

app = Flask(__name__)

persons = [
    {
        'id': 1,
        'name': "Abi"
    },
    {
        'id': 3,
        'name': "Siva"
    },
    {
        'id': 4,
        'name': "sss"
    }
]

# home


@app.route('/')
def home():
    return "Hello to Api"

# GET ALL /person


@app.route('/persons')
def get_all_persons():
    return jsonify({'persons': persons})

# GET one


@app.route('/person/<int:id>')
def get_person(id):
    for person in persons:
        if person['id'] == id:
            return person
    return {'msg': 'person not found'}, 404

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
@app.route('/person/<int:id>', methods=['PUT'])
def person(id):
    req_id = request.get_json()
    for person in persons:
        if person['id'] == id:
            update = {
                'name': req_id['name']
            }
            person.update(update)
            return (person)
    return jsonify({'msg': 'person not found'})


# DELETE
@app.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    # global persons
    # # Find the index of the person with the given ID in the `persons` list
    # index_to_delete = next((index for index, person in enumerate(persons) if person['id'] == id), None)

    # if index_to_delete is not None:
    #     # If the person is found, remove them from the list
    #     deleted_person = persons.pop(index_to_delete)
    #     return jsonify({"message": f"Person with id={id} deleted successfully.", "deleted_person": deleted_person}), 200
    # else:
    #     return jsonify({"message": f"Person with id={id} not found in the list."}), 404

    person_to_delete = next((person for person in persons if person['id'] == id), None)
    if person_to_delete:
        # If the person is found, remove them from the list
        persons.remove(person_to_delete)
        print(f"Dictionary with id={id} deleted successfully.")
        print(persons)  # Print the updated list after deletion

        # Return a response indicating success (Optional)
        return jsonify({"message": f"Dictionary with id={id} deleted successfully."}), 200
    else:
        print(f"Dictionary with id={id} not found in the list.")
        # Return a response indicating failure (Optional)
        return jsonify({"error": f"Dictionary with id={id} not found in the list."}), 404


app.run(port=5009, debug=True)
