import xlwings as xw
import code
import re

sheet = xw.books[0].sheets[0]
all_row = sheet.api.UsedRange.Rows.Count
column0 = sheet.range("A3").expand("right").count
column1 = column0 - 2
Name = []
d = {}
# 姓名列表
for A in sheet.range((5, 2), (all_row - 2, 2)):
    if not A.value is None:
        Name.append(A.value.replace(' ',''))
        d.update({A.value.replace(' ',''): A.row})

		sheet2 = xw.books[0].sheets[2]
		#查找表头地址
		for t in sheet2.range("A1:A10"):
		    if t.value == '时间':
		        adr2 = t.address
		        add2 = int(re.findall(r'\d+',adr2)[0])

		sheet2_row = sheet2.range(adr2).expand('down').count + (add2 -1)  #sheet总行数
		sheet2_col = sheet2.range(adr2).expand('right').count
		#获取打卡时间所在列
		s2_add = []
		for s in range(sheet2_col):
		    if sheet2.range((add2,s+1),(add2,s+1)).value == '打卡时间':
		        s2_add.append (s + 1)

		CRange = sheet2.range((add2+1, 2), (sheet2_row, 2))
		#遍历
		for i in Name:
			for C in CRange:
				if C.value ==i:
					v = C.end('left').expand('right').value
					s2_data = int(v[0][-2:])
					if v[s2_add[0]-1] != '--':
						if v[s2_add[0]-1] <= '09:00':
							sheet.range(d[i],(3 + s2_data)).value = "☆"
						if v[s2_add[0]-1] >= '17:00':
							sheet.range((d[i] +1 ),(3 + s2_data)).value = "☆"
					if v[s2_add[1]-1] != '--':
						if v[s2_add[1]-1] <= '09:00':
							sheet.range(d[i],(3 + s2_data)).value = "☆"
						if v[s2_add[1]-1] >= '17:00':
							sheet.range((d[i] +1 ),(3 + s2_data)).value = "☆"

code.interact(banner = "",local = locals())