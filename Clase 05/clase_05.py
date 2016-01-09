# -*- coding: utf-8 -*-
import wx

# wx.TextCtrl()
# wx.StaticText()

class MiAplicacion(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))
		sz = wx.BoxSizer(wx.VERTICAL)
		
		# Controles
		self.input_text = wx.TextCtrl(self, -1, "")
		self.static_text = wx.StaticText(self, -1, u"")
		boton = wx.Button(self, -1, u"Botón")
		
		# Modificando fuente
		font1 = self.input_text.GetFont()
		font1.SetPointSize(16)
		self.input_text.SetFont(font1)
		self.static_text.SetFont(font1)
		
		# Modificando color de fondo
		self.static_text.SetBackgroundColour("#FFFFAA")
		
		# Modificando el color de fuente
		self.static_text.SetForegroundColour("#FF0000")
		
		# Agregar al sizer
		sz.Add(self.input_text, 1, wx.EXPAND|wx.ALL, 10)
		sz.Add(self.static_text, 1, wx.EXPAND|wx.ALL, 10)
		sz.Add(boton, 1, wx.EXPAND|wx.ALL, 10)
		
		# Eventos
		self.Bind(wx.EVT_BUTTON, self.onClick)
		
		self.SetSizer(sz)
		self.Centre(True)
		self.Show()
		
	def onClick(self,event):
		txt = self.input_text.GetValue()
		self.static_text.SetLabelText(txt)
		


if __name__=='__main__':
	app = wx.App()
	frame = MiAplicacion(None,u"Curso wxPython")
	app.MainLoop()
