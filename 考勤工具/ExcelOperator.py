from UI.noname import MyFrame1
import wx
import xlwings as xw
import datetime, time, re


class MyFrame(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.m_button2.Disable()

    def open_file(self, file):
        self.app = xw.App(visible=True, add_book=False)
        self.app.display_alerts = True
        self.app.screen_updating = True
        self.wb = self.app.books.open(file)
        self.sheet = self.wb.sheets[0]

    def m_button1_OnButtonClicj( self, event ):
        self.m_button1.Disable()
        fileDialog = wx.FileDialog(self, message="选择Excel文件", wildcard="Excel (*.xlsx)|*.xlsx|" "All files (*.*)|*.*", style=wx.FD_OPEN)
        dialogResult = fileDialog.ShowModal()
        path = fileDialog.GetPath()
        #print (path)
        self.m_textCtrl1.Value = path
        self.m_textCtrl2.Value = "文件打开中，请勿关闭程序！"
        self.open_file(path)
        self.m_button2.Enable()
        self.m_textCtrl2.Value = "点击右侧按钮开始程序！"

    def m_button2_OnButtonClicj(self, event):
        self.m_button2.Disable()
        self.m_textCtrl2.Value = "程序运行中"
        all_row = self.sheet.api.UsedRange.Rows.count
        column0 = self.sheet.range('A3').expand('right').count
        column1 = column0 - 2
        Name = []
        d = {}
        # 姓名列表
        for A in self.sheet.range((5, 2), (all_row - 2, 2)):
            if not A.value is None:
                Name.append(A.value.replace(' ',''))
                d.update({A.value.replace(' ',''): A.row})
        sheet1 = self.wb.sheets[1]
        #sheet1_row = sheet1.range('A3').expand('down').count + 2
        #BRange = sheet1.range((4, 2), (sheet1_row, 2))
        #遍历前十行，查找表头（"时间"）所在行和地址
        for t in sheet1.range("A1:A30"):
            if t.value == '时间':
                adr = t.address
                add = int(re.findall(r'\d+',adr)[0])
                break
        sheet1_row = sheet1.range(adr).expand('down').count + (add -1)  #sheet总行数
        sheet1_col = sheet1.range(adr).expand('right').count
        #遍历"审批单"所在列
        for s in range(sheet1_col):
            if sheet1.range((add,s+1),(add,s+1)).value == '审批单':
                s_add = s + 1
                break

        BRange = sheet1.range((add+1, 2), (sheet1_row, 2))
        for i in Name:
            #column2 = column1
            for B in BRange:
                if B.value == i:
                    v = B.end('left').expand('right').value
                    dday = int(v[0][-2:])
                    if v[s_add-1] == '--':
                        if v[s_add] <= '09:00' and v[s_add] != '--':
                            self.sheet.range(d[i], (3 + dday)).value = '√'
                        if v[s_add+1] >= '17:00' and v[s_add+1] != '--':
                            self.sheet.range(d[i] + 1, (3 + dday)).value = '√'
                    #column2 = column2 - 1
        sheet2 = self.wb.sheets[2]
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
                            self.sheet.range(d[i],(3 + s2_data)).value = "☆"
                        if v[s2_add[0]-1] >= '17:00':
                            self.sheet.range((d[i] +1 ),(3 + s2_data)).value = "☆"
                    if v[s2_add[1]-1] != '--':
                        if v[s2_add[1]-1] <= '09:00':
                            self.sheet.range(d[i],(3 + s2_data)).value = "☆"
                        if v[s2_add[1]-1] >= '17:00':
                            self.sheet.range((d[i] +1 ),(3 + s2_data)).value = "☆"
        self.m_button1.Enable()
        self.m_textCtrl2.Value = "完成！耗时{0}秒".format(time.process_time())
