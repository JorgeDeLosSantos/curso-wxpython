# -*- coding: utf-8 -*-
import wx
import glob
import os

class MiAplicacion(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))
		sz = wx.BoxSizer(wx.VERTICAL)
		
		opciones = glob.glob("*.txt")
		
		self.lista = wx.ListBox(self, -1, choices=opciones)
		
		sz.Add(self.lista, 1, wx.EXPAND|wx.ALL, 10)
		
		self.Bind(wx.EVT_LISTBOX, self.on_click, self.lista)
		
		self.SetSizer(sz)
		self.Centre(True)
		self.Show()
		
	def on_click(self,event):
		archivo = self.lista.GetStringSelection()
		os.startfile(archivo)

if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None,u"ListBox")
	app.MainLoop()
