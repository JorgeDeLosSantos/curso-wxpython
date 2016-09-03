# -*- coding: utf-8 -*-
import wx

class MiAplicacion(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))
		sz = wx.BoxSizer(wx.VERTICAL)
		
		self.sld = wx.Slider(self, wx.ID_ANY, value=10, minValue=0, maxValue=10,
							style=wx.SL_AUTOTICKS|wx.SL_LABELS)
		self.sld.SetTickFreq(10)
		self.txt = wx.StaticText(self, wx.ID_ANY)
		self.txt.SetBackgroundColour("#ffffff")
		
		sz.Add(self.sld, 1, wx.EXPAND|wx.ALL, 10)
		sz.Add(self.txt, 1, wx.EXPAND|wx.ALL, 10)
		
		self.Bind(wx.EVT_SLIDER, self.on_click)
		
		self.SetSizer(sz)
		self.Centre(True)
		self.Show()
		
	def on_click(self,event):
		print self.sld.GetTickFreq()

if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None,u"Slider")
	app.MainLoop()
