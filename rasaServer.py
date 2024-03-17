import subprocess
import os

def start_rasa_server():
    rasa_project_dir = "models/RASA"
    os.chdir(rasa_project_dir)
    
    rasa_command = "rasa run -m models --enable-api --cors \"*\" "

    subprocess.Popen(rasa_command, shell=True)

if __name__ == '__main__':
    start_rasa_server()
        