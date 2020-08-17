import wx

class TestFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(300,200))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Creating controls
        self.rb1 = wx.RadioButton(self, -1, "12")
        self.rb2 = wx.RadioButton(self, -1, "14")
        self.rb3 = wx.RadioButton(self, -1, "18")
        self.txt = wx.StaticText(self, -1, "Python & wxPython")
        self.bt = wx.Button(self, -1, "Do")
        
        # Add controls to sizer
        self.sz.Add(self.rb1, 1, wx.EXPAND|wx.ALL, 5)
        self.sz.Add(self.rb2, 1, wx.EXPAND|wx.ALL, 5)
        self.sz.Add(self.rb3, 1, wx.EXPAND|wx.ALL, 5)
        self.sz.Add(self.txt, 1, wx.EXPAND|wx.ALL, 5)
        self.sz.Add(self.bt, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        
        # Bind events
        # ~ self.Bind(wx.EVT_RADIOBUTTON, self.OnClick)
        self.Bind(wx.EVT_BUTTON, self.OnButton)
        
        # Set sizer
        self.SetSizer(self.sz)
        
        # Centre and show frame
        self.Centre(True)
        self.Show()
        
    def OnClick(self,event):
        a = event.EventObject.GetLabel()
        ft = self.txt.GetFont()
        if a == "12":
            ft.SetPointSize(12)
        elif a == "14":
            ft.SetPointSize(14)
        elif a == "18":
            ft.SetPointSize(18)
        else:
            pass
        self.txt.SetFont( ft )
        
    def OnButton(self,event):
        if self.rb1.GetValue() == True:
            fsz = 12
        elif self.rb2.GetValue() == True:
            fsz = 14
        elif self.rb3.GetValue() == True:
            fsz = 18
        else:
            fsz = 12
            
        ft = self.txt.GetFont()
        ft.SetPointSize( fsz )
        self.txt.SetFont( ft )
        
        

if __name__=='__main__':
    app = wx.App()
    frame = TestFrame(None, "RB Demo")
    app.MainLoop()
