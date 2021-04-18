import subprocess
import os

class CermineTextExtractor:

    def __init__(self):
        self.current_location = os.path.dirname(__file__)
        self.folder_location = ""
        self.jar_location = "cermine-impl-1.13-jar-with-dependencies.jar"

    # Extracts texts of all pdfs in folder and adds the corresponding extraction files to the source folder  
    def cermine_extract(self, folder_location, zonesOption, truevizOption):
        
        command = 'java -cp '+ self.current_location+"/"+self.jar_location + ' pl.edu.icm.cermine.ContentExtractor'
        command += ' -path ' + self.current_location+"/"+folder_location
        command += ' -outputs text'

        if zonesOption:
            command += ',zones'
        if truevizOption:
            command += ',trueviz'

        print("Run command: " + command)

        subprocess.Popen(command, shell=True)
        
        return   

if __name__ == "__main__":
    textExtractor = CermineTextExtractor()

    # Will only output something if there is a new, unprocessed pdf in the folder
    # Also it doesn't work if there are spaces in foldernames in the path
    textExtractor.cermine_extract('../../dataset/',True, True)

