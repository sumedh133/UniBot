import subprocess
import os

def start_rasa_server():
    # Change directory to the Rasa project directory
    rasa_project_dir = "models/RASA"
    os.chdir(rasa_project_dir)
    
    # Command to start Rasa server
    rasa_command = "rasa run -m models --enable-api --cors \"*\" "
    
    # Execute the command
    subprocess.Popen(rasa_command, shell=True)

if __name__ == '__main__':
    # Start the Rasa server
    start_rasa_server()
    