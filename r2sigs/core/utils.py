import os

def get_file_list_from_location(location):

    file_list = []

    if os.path.isdir(location):

        for file in sorted_alphanumeric(os.listdir(location)):

            file_list.append(os.path.join(location, file))

    elif os.path.isfile(location):

        file_list.append(location)

    return file_list
