import pprint
def _save_database(info_dictionary):
    print("Save to DB complete!")
    pprint.pprint(info_dictionary)

def handle_membership_creation(name, id, phone, *hobby, **other_information):
    gender = other_information['gender'] if 'gender' in other_information else "unknown"
    age = other_information['age'] if 'age' in other_information else "unknown"
    born_city = other_information['born_city'] if 'born_city' in other_information else "unknown"
    member_information = {
        'member_name': name,
        'member_personal_id': id,
        'member_cellphone_number': phone,
        'member_hobby': hobby,
        'member_gender': gender,
        'member_age': age,
        'member_born city': born_city,
    }

    _save_database(info_dictionary = member_information)

if __name__ == '__main__':
    hobby = ['basketball', 'biking', 'video game']
    info = {
        'gender': 'male',
        'age': 18,
        'born_city': 'Taipei' 
    }
    handle_membership_creation("Chung Yi", 'B1263545645', '0912345678', *hobby, **info)