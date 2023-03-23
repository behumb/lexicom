def get_file_names(names: list) -> list:
    max_length = len(max(names, key=len))
    formatted_names = []
    for name in names:
        unique_chars_name = ''
        for char in name:
            if char.lower() not in unique_chars_name.lower():
                unique_chars_name += char
        formatted_name = unique_chars_name + '_' * (max_length - len(unique_chars_name))
        formatted_names.append(formatted_name)
    return formatted_names
