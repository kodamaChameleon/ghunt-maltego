import subprocess
import asyncio

# Install required python dependencies
def install_requirements():
    subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

# Build config file for easy importation
def build_config():
    subprocess.check_call(['python3', 'project.py', 'list'])

# Obtain Ghunt credentials
async def ghunt_login():
    try:
        from ghunt.modules import login
    except ImportError:
        print("Failed to import the ghunt credentials module")
        return

    await login.check_and_login(None, False)

if __name__ == '__main__':
    install_requirements()
    asyncio.run(ghunt_login())
    build_config()
