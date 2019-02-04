import os
  
    
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

from sklearn import datasets

print("It is ok")
