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
    main(['install','--upgrade','-U','pip3'])
    main(['freeze','--user','pip3'])

try:
    from sklearn import datasets
except:
    import subprocess
    print("Try to install with subprocess")
    subprocess.call(['pip3', 'install', '-U', 'scikit-learn'])
    subprocess.call(['pip3', 'list'])

from sklearn import datasets

print("It is ok")
