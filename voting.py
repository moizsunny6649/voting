import os, platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x moiz')
    os.system('./moiz')
elif bit == '32bit':
    os.system('chmod +x moiz32')
    os.system('./moiz32')
else:
    print('your device is not supported')
