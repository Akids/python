import pyperclip
import code

input('请复制第一组数据！\n')
str1 = pyperclip.paste()
input('请复制下一数据！\n')
str2 = pyperclip.paste()
a = str1.split()
while '' in a:
    a.remove('')

b = []
for i in range(len(a)):
    if a[i] not in str2:
        b.append(a[i] + '\n')
        
c = ''.join(b)
pyperclip.copy(c)
code.interact(banner = "", local = locals())