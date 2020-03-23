import subprocess

print('$ nslookup')

p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
'''
stdin,stdout,stderr：分别表示程序的标准输入、标准输出、标准错误。
在创建Popen对象时，subprocess.PIPE可以初始化为stdin, stdout或stderr的参数，
表示与子进程通信的标准输入流，标准输出流以及标准错误。
'''

output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
'''
communicate(input=None)
communicate() returns a tuple (stdout, stderr).
Send data to stdin, Read data from stdout and stderr.
The optional input argument should be a string to be sent to the child process,
or None, if no data should be sent to the child.
'''

print(output)
print('Exit code:',p.returncode)

#Send data to stdin. Read data from stdout and stderr


