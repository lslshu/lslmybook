"""
读写二进制文件

Date: 2019-11-11
"""

import base64

with open('mm.jpg','rb') as f:
	data = f.read()
	print('字节数',len(data))
	print(base64.b64decode(data))

with open('girl.jpg','wb') as f:
	f.write(data)
print('写入完成!')