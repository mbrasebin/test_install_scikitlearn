import os

try:
    from pip._internal import main
except:
    plugin_dir=os.path.dirname(__file__)
    getpipscript= os.path.join(plugin_dir, "get-pip.py")
    import subprocess
    subprocess.call("python3 get-pip.py --user", shell=True)
    #exec(compile(open(getpipscript).read(), getpipscript, 'exec'))
    from pip._internal import main
    # just in case the included version is old
    main(['install','--upgrade','--user','pip3'])
    main(['freeze','--user','pip3'])
    print("Try to install with pip3 directly")    
    
# For windows users
try:
    from sklearn import datasets
except:
    import subprocess
    subprocess.call(['easy_install', '-m', 'scikit-learn'])
    print("Try to install with easy install")

try:
    from sklearn import datasets
except:
    import subprocess
    print("Try to install with subprocess")
    subprocess.call(['pip3', 'install', '-U' ,'--user', 'scikit-learn'])
    subprocess.call(['pip3', 'freeze', '-U' ,'--user'])

from sklearn import datasets

print("It is ok")
