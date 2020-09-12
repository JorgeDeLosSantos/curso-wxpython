# -*- coding: utf-8 -*-
import wx

class TestFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(200,150))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Creating controls
        self.red = wx.CheckBox(self, -1, "Red")
        self.green = wx.CheckBox(self, -1, "Green")
        self.blue = wx.CheckBox(self, -1, "Blue")
        
        # Add controls to sizer
        self.sz.Add(self.red, 1, wx.EXPAND|wx.LEFT, 20)
        self.sz.Add(self.green, 1, wx.EXPAND|wx.LEFT, 20)
        self.sz.Add(self.blue, 1, wx.EXPAND|wx.LEFT, 20)
        
        # Bind events
        self.Bind(wx.EVT_CHECKBOX, self.OnCheck)
        
        # Set sizer
        self.SetSizer(self.sz)
        # Centre and show frame
        self.Centre(True)
        self.Show()
        
    def OnCheck(self,event):
        R = float(self.red.GetValue())
        G = float(self.green.GetValue())
        B = float(self.blue.GetValue())
        color = wx.Colour(R*255,G*255,B*255)
        self.SetBackgroundColour(color)
        self.Refresh()
        

if __name__=='__main__':
    app = wx.App()
    frame = TestFrame(None, "wxCheckBox Demo")
    app.MainLoop()
