# -*- coding: utf-8 -*-
import wx

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))
        sz = wx.BoxSizer(wx.VERTICAL)
        
        self.sld1 = wx.Slider(self, -1, 0, 0, 10, style=wx.SL_VERTICAL)
        self.sld2 = wx.Slider(self, -1, 0, 0, 10, style=wx.SL_AUTOTICKS|wx.SL_LABELS)
        self.txt = wx.StaticText(self, -1)
        
        self.SetBackgroundColour(self.sld1.GetBackgroundColour())
        
        sz.Add(self.sld1, 1, wx.EXPAND)
        sz.Add(self.sld2, 1, wx.EXPAND)
        sz.Add(self.txt, 1, wx.EXPAND)
        
        self.Bind(wx.EVT_SLIDER, self.OnSlider, self.sld1)
        
        self.SetSizer(sz)
        self.Centre(True)
        self.Show()
        
    def OnSlider(self,event):
        a = self.sld1.GetValue()
        b = self.sld2.GetValue()
        self.txt.SetLabel("%s"%(a+b))
        

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None,"Slider Demo")
    app.MainLoop()
