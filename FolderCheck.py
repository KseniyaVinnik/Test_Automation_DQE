import os


class FolderCheck:
    file_list = []

    def __init__(self, path):
        self.path = path

    def remove_files(self):
        in_folder = os.listdir(path=self.path)
        if in_folder:
            for file in in_folder:
                if file.endswith('.fb2'):
                    FolderCheck.file_list.append(file)
                else:
                    os.rename(self.path + file, 'incorrect_input/' + file)
        return FolderCheck.file_list
