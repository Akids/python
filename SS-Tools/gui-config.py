from lxml import etree
import json
import os, shutil, time
import qrcode, base64

#解析html
html=etree.HTML(text,etree.HTMLParser())
result = html.xpath('//td/text()')

file_path = r'E:\Shadowsocks-4.1.4'

with open(file_path + r'\gui-config.json', "r", encoding="utf-8") as f:
    data = json.load(f)

data["configs"] = []
for i in range(len(result)):
    if i%7 == 1:
        dict ={}
        dict['server'] = result[i]
        dict['server_port'] = int(result[i + 1])
        dict['password'] = result[i + 3]
        dict['method'] = result[i + 2]
        dict['plugin'] = ''
        dict['plugin_opts'] = ''
        dict['plugin_args'] = ''
        dict['remarks'] = result[i + 5]
        dict['timeout'] = 5
        data["configs"].append(dict)

json_data = json.dumps(data, indent=4, separators=(',', ': ')) #sort_keys=True,排序


#备份json
if not os.path.exists(file_path + r'\Backup'):
    os.mkdir(file_path + r'\Backup')
#移动文件
shutil.move(file_path + r'\gui-config.json', file_path + r'\Backup\gui-config' + '-' + str(int(time.time())) + ' ' + '.json')

with open(file_path + r'\gui-config.json', 'w', encoding='utf-8') as w:
    w.write(json_data)

#二维码图片
for j in range(len(data["configs"])):
     a = data["configs"][j]
     qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10, border=4,)
     b = r'ss://' + str(base64.b64encode((a['method'] + ':' + a['password'] + '@' + a['server'] + ':' + str(a['server_port'])).encode('utf-8')), encoding='utf-8')
     qr.add_data(b)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save(file_path + r'\Pictures' + '\\'+ a['server'] + r'.png')

#生成Shadowrocket json
ss_data = []
for i in range(len(result)):
    if i%7 == 1:
        dict ={}
        dict['server'] = ''
        dict['weight'] = int(time.time())
        dict['allowInsecure'] = bool(0)
        dict['title'] = result[i]
        dict['host'] = result[i]
        dict['ota'] = bool(0)
        dict['file'] = ''
        #dict['uuid'] = ''
        dict['method'] = result[i + 2]
        dict['flag'] = result[i + 5]
        dict['updated'] = time.time()
        dict['obfs'] = 'none'
        dict['type'] = 'Shadowsocks'
        dict['user'] = ''
        dict['protoParam'] = ''
        dict['tls'] = bool(0)
        dict['port'] = result[i + 1]
        dict['selected'] = bool(0)
        dict['proto'] = 'none'
        dict['password'] = result[i + 3]
        dict['data'] = ''
        dict['ping'] = -1
        dict['created'] = time.time()
        ss_data.append(dict)

#备份Shadowrocket json
if not os.path.exists(file_path + r'\Backup'):
    os.mkdir(file_path + r'\Backup')
#移动文件
shutil.move(file_path + r'\Shadowrocket.json', file_path + r'\Backup\Shadowrocket' + '-' + str(int(time.time())) + ' ' + '.json')

sss_data = json.dumps(ss_data, indent=4, separators=(',', ': '))
with open(file_path + r'\Shadowrocket.json', 'w', encoding='utf-8') as w:
    w.write(sss_data)