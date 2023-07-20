from app import create_app

import flask_sqlalchemy
import platform
import subprocess


print(flask_sqlalchemy.__version__)

if __name__ == '__main__':
    operating_system = platform.system()
    script_path = ""

    print(f'Starting flask server...\nPlatform: {operating_system}')

    if operating_system == 'Windows':
        script_path = 'install_JS_packages.ps1'
        subprocess.run(['./' + script_path], shell=True)

        script_path = 'install_PY_packages.ps1'
        subprocess.run(['./' + script_path], shell=True)

    elif operating_system == 'Linux' or operating_system == 'Darwin':
        script_path = 'install_JS_packages.sh'
        subprocess.run(['./' + script_path], shell=True)

        script_path = 'install_PY_packages.sh'
        subprocess.run(['./' + script_path], shell=True)

    else:
        print("Unsupported operating system.")
        exit(1)
    
    

    app = create_app()
    app.run(debug=True)