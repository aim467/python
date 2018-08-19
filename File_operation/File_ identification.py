
'''
a = 1

def change_integer(a):
    a = a + 1
    return a

print change_integer(a)
'''


import filetype
 
def main():
 kind = filetype.guess(path)
 if kind is None:
  print('Cannot guess file type!')
  return
 
 print('File extension: %s' % kind.extension)
 print('File MIME type: %s' % kind.mime)
 
if __name__ == '__main__':
    path = input("请输入文件类型:")
    main()
