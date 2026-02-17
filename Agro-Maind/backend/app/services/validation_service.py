def validate_age(age):
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a non-negative integer.")
    return True

def validate_identification_number(id_number):
    if not isinstance(id_number, str) or len(id_number) != 10 or not id_number.isdigit():
        raise ValueError("Identification number must be a 10-digit string.")
    return True

def validate_user_input(user_data):
    validate_age(user_data.get('age'))
    validate_identification_number(user_data.get('identification_number'))
    return True