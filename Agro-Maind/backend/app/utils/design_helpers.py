def format_crop_info(crop_data):
    formatted_info = {
        "name": crop_data.get("name", "Unknown"),
        "type": crop_data.get("type", "N/A"),
        "growth_conditions": crop_data.get("growth_conditions", "N/A"),
        "pests": crop_data.get("pests", []),
        "diseases": crop_data.get("diseases", [])
    }
    return formatted_info

def validate_user_input(user_input):
    if not user_input.get("age") or user_input["age"] < 18:
        return False, "User must be at least 18 years old."
    if not user_input.get("identification_number"):
        return False, "Identification number is required."
    return True, "Validation successful."

def generate_response_message(message_type, content):
    response = {
        "type": message_type,
        "content": content
    }
    return response

def style_chat_widget(widget_data):
    return {
        "background_color": widget_data.get("background_color", "#ffffff"),
        "font_size": widget_data.get("font_size", "14px"),
        "border_radius": widget_data.get("border_radius", "5px"),
        "padding": widget_data.get("padding", "10px")
    }