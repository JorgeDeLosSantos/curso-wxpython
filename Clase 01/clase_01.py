# -*- coding: utf-8 -*-
import wx

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))
        
        self.Centre(True)
        self.Show()
        

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None,u"Mi primera aplicación")
    app.MainLoop()
