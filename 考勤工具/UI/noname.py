# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Excel Operator", pos = wx.DefaultPosition, size = wx.Size( 300,150 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 150,25 ), 0 )
		gSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"打开文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,25 ), 0 )
		gSizer1.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"数据生成", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1_OnButtonClicj )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2_OnButtonClicj )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button1_OnButtonClicj( self, event ):
		event.Skip()

	def m_button2_OnButtonClicj( self, event ):
		event.Skip()


