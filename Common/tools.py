import helpers
import os
import random
import string

from Common.constants import UserTypesValues


class Tools:

    @staticmethod
    def get_path_of_files_for_upload():
        return helpers.get_project_dir() + r"\files_for_upload"

    @staticmethod
    def get_full_path_of_specific_file_for_upload(file_name):
        return helpers.get_project_dir() + fr"\files_for_upload\{file_name}"

    @staticmethod
    def get_all_files_for_upload():
        path = Tools.get_path_of_files_for_upload()
        return os.listdir(path)

    @staticmethod
    def get_jpg_file_for_upload(used_file_name=''):
        for x in Tools.get_all_files_for_upload():
            if "jpg" in x:
                if not used_file_name == x:
                    return x

    @staticmethod
    def get_any_different_than_jpg_file_for_upload(used_file_name=''):
        for x in Tools.get_all_files_for_upload():
            if "jpg" not in x:
                if not used_file_name == x:
                    return x


class UserData:
    def __init__(self):
        self.email = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10))) + "@example.com"
        self.password = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
        self.user_type = random.choice([UserTypesValues.NORMAL_USER, UserTypesValues.ENTERPRISE_USER])

    @staticmethod
    def generate_random_string():
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
