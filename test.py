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
    main(['install','--upgrade','--user','pip'])
    main(['freeze','--user','pip'])
    
    
    

try:
    from sklearn import datasets
except:
    from pip._internal import main
    main(['install','-U' ,'--user', 'scikit-learn'])

# For windows users
try:
    from sklearn import datasets
except:
    import subprocess
    subprocess.call(['easy_install', '-m', 'scikit-learn'])
    

try:
    from sklearn import datasets
except:
    import subprocess
    subprocess.call(['pip', 'install', '-U' ,'--user', 'scikit-learn'])
    
from sklearn import datasets

print("It is ok")
