from src.info import constants


def project_description():
    with open(constants.PROJECT_DESCRIPTION_FILENAME) as description_file:
        return description_file.read()
