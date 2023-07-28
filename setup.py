import subprocess, trio

# Install required python dependencies
def install_requirements():
    subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

# Build config file for easy importation
def build_config():
    subprocess.check_call(['python3', 'project.py', 'list'])

# Obtain Ghunt credentials
def ghunt_login():

    try:
        from ghunt.modules import login
    except ImportError:
        print("Failed to import the ghunt credentials module")

    trio.run(login.check_and_login, None, False)

if __name__ == '__main__':
    install_requirements()
    ghunt_login()
    build_config()