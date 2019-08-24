import subprocess
from pygments.lexers import shell
from IPython.utils.io import stdout

ssh = subprocess.Popen(['ssh','ansible@3.84.3.206'],shell=False,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
print(ssh.stdout.readline())