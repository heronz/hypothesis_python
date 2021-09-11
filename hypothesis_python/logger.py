import json
from datetime import datetime


class Logger:
    """
    Class used to log any text into a text file
    """
    def __init__(self, path):
        """
        Create a instance of the logger with a fixed path

        :param path: path that the log file will be created
        """
        self.path = path

    def log(self, text, file_name=f'log_{datetime.now().strftime("%d%m%Y_%H%M%S")}'):
        """
        Method that creates a txt file with any text.
        This method also tries to convert a dict into text using json.dumps

        :param text: Text that will be stored in the log file
        :param file_name: Name of the log file, if not informed will default to log_currentdate_currenttime
        """
        if isinstance(text, dict):
            try:
                text = json.dumps(text)
            except Exception as err:
                text = str(err)
        with open(self.path+f'/{file_name}.txt', 'w') as file:
            file.write(f'{text}')
