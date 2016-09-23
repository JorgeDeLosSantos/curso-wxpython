# -*- coding: utf-8 -*-
import wx

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))
        sz = wx.BoxSizer(wx.VERTICAL)
        
        sld1 = wx.Slider(self, -1, 0, 0, 100, style=wx.SL_LABELS)
        sld2 = wx.Slider(self, -1, 0, 0, 100, style=wx.SL_VERTICAL)
        self.SetBackgroundColour(sld1.GetBackgroundColour())
        
        sz.Add(sld1, 1, wx.EXPAND)
        sz.Add(sld2, 1, wx.EXPAND)
        
        self.SetSizer(sz)
        self.Centre(True)
        self.Show()
        

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None,u"Slider Demo")
    app.MainLoop()
