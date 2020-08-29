# -*- coding: utf-8 -*-
import wx

class TestFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(300,250))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Creating controls
        self.spin1 = wx.SpinCtrl(self, -1, min=1, max=10, initial=5)
        self.spin2 = wx.SpinCtrl(self, -1, min=1, max=10, initial=5)
        self.spin3 = wx.SpinCtrl(self, -1, min=1, max=10, initial=5)
        self.bt = wx.Button(self, -1, "Calcular")
        self.txt = wx.StaticText(self, -1, "")
        
        # Add controls to sizer
        self.sz.Add(self.spin1, 1, wx.EXPAND|wx.ALL, 10)
        self.sz.Add(self.spin2, 1, wx.EXPAND|wx.ALL, 10)
        self.sz.Add(self.spin3, 1, wx.EXPAND|wx.ALL, 10)
        self.sz.Add(self.txt, 1, wx.EXPAND|wx.ALL, 10)
        self.sz.Add(self.bt, 1, wx.EXPAND|wx.ALL, 10)
        
        # Bind events
        # ~ self.Bind(wx.EVT_SPINCTRL, self.OnSpin)
        self.Bind(wx.EVT_BUTTON, self.Calcular)
        
        # Set sizer
        self.SetSizer(self.sz)
        
        # Centre and show frame
        self.Centre(True)
        self.Show()
        
    def OnSpin(self,event):
        id_spin1 = self.spin1.GetId()
        id_spin2 = self.spin2.GetId()
        id_actual = event.GetId()
        
        if id_spin1 == id_actual:
            print("Spin 1")
        elif id_spin2 == id_actual:
            print("Spin 2")
            
    def Calcular(self,event):
        n1 = self.spin1.GetValue()
        n2 = self.spin2.GetValue()
        n3 = self.spin3.GetValue()
        self.txt.SetLabel( str(n1+n2+n3 ) )
        
    

if __name__=='__main__':
    app = wx.App()
    frame = TestFrame(None, "SpinCtrl Demo")
    app.MainLoop()
