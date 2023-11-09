NAME: str = "your_project_name"
AUTHOR: str = "your author name",
AUTHOR_EMAIL: str = "your@email.com",
LICENCE: str = "LICENCE"
DESCRIPTION: str = "A short description of your project"
REQUIRED_PYTHON: tuple = (3, 10)
WORKSPACE: str = "folder_containing_the_software"
MAIN_MODULE: str = "main"
MAIN_FUNC: str = "main"

# Change this to ovveride default version number
OVERRIDE_VN: bool = False
VN: str = "1.0.0"

# Fill this part if your tool features command-line interface
HAS_COMMAND_LINE: bool = False
COMMAND: dict = {'console_scripts': [
    f'{NAME}={WORKSPACE}.{MAIN_MODULE}:{MAIN_FUNC}']}
