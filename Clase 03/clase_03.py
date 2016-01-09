# -*- coding: utf-8 -*-
import wx
from random import randint

class MiAplicacion(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))
		sz = wx.BoxSizer(wx.VERTICAL)
		
		self.Centre(True)
		self.Show()


if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None,u"Botón")
	app.MainLoop()
