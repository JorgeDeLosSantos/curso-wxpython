# -*- coding: utf-8 -*-
import wx

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))
        
        texto = wx.TextCtrl(self, style=wx.TE_MULTILINE, pos=(0,0), size=(100,100))
        texto2 = wx.TextCtrl(self, style=wx.TE_MULTILINE, pos=(100,0), size=(100,100))
        boton = wx.Button(self, -1, u"Botón", pos=(130,100), size=(100,30))
        
        self.Centre(True)
        self.Show()


if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None,u"Mi primera aplicación")
    app.MainLoop()
