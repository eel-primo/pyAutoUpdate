import os

class LibInstallFailure(Exception):
    def __init__(self, lib_name, description):
        self.lib_name = lib_name
        self.description = description

    def __str__(self):
        return f"LibInstallFailure: Library {self.lib_name} wasn't installed! Cause: {self.description}"

class FileDownloadFailure(Exception):
    def __init__(self, filename, description):
        self.filename = filename
        self.description = description

    def __str__(self):
        return f"FileDownloadFailureFailure: File {self.filename} wasn't downloaded! Cause: {self.description}"

class FileUpdateFailure(Exception):
    def __init__(self, filename, description):
        self.filename = filename
        self.description = description

    def __str__(self):
        return f"FileUpdateFailureFailure: File {self.filename} wasn't updated! Cause: {self.description}"    

class lib_installer:
    def __init__(self, libs):
        self.libs = libs

    def _download_lib_(self, lib_name):
        return os.system("py -m pip install " + lib_name)
    
    def install(self):
        #Just install all libs, no checking their avability
        for lib in self.libs:
            result = self._download_lib_(lib)
            if result != 0:
                raise LibInstallFailure(lib, result)

        # Let's say for main program that we finished
        return True

class file_updater:
    def __init__(self, files, path_on_github):
        self.files = files
        self.path = path_on_github

        li = lib_installer(['requests'])
        li.install()      
        

    def _download_file_(self, filepath):
        import requests
        return requests.get(filepath, timeout=10).text()
    
    def install(self):
        #Just install all libs, no checking their avability
        import hashlib
        should_restart_app = False
        for file_id in range(len(self.files)):
            try:
                content = self._download_file_(self.path[file_id])
                content_hash_sha256 = haslib.sha256().update(content)
                try:
                    # check file hash, if hash != downloaded hash -> update!
                    # 9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A08
                    # 9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A08
                    with open(self.files[file_id], "r") as file:
                        file_hash_256 = haslib.sha256().update(file.read())
                        file.close()

                    if not content_hash_sha256 == file_hash_256:
                        should_restart_app = True
                        with open(self.files[file_id], "w") as file:                            
                            file.write(content)
                            file.close()
                except OSError as err:
                    raise FileUpdateFailure(self.files[file_id], err)
            # Too broad!
            except Exception as err:
                raise FileDownloadFailure(self.files[file_id], err)
        # Let's say for main program that we finished, and should user restart program
        return should_restart_app

        
        
                
        
