import wx

class TestFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(300,200))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Creating controls
        letras = list("abcdefghijklmopq")
        self.rbox = wx.RadioBox(self, -1, "Colores", choices=letras,
                    majorDimension = 3, style=wx.RA_SPECIFY_ROWS)
        
        # Add controls to sizer
        self.sz.Add(self.rbox, 1, wx.EXPAND|wx.ALL, 5)
        
        # Bind events
        self.Bind(wx.EVT_RADIOBOX, self.OnClick)
        
        # Set sizer
        self.SetSizer(self.sz)
        
        # Centre and show frame
        self.Centre(True)
        self.Show()
        
    def OnClick(self,event):
        idx = self.rbox.GetSelection()
        print( self.rbox.GetString(idx) )
    
        
    
if __name__=='__main__':
    app = wx.App()
    frame = TestFrame(None, "RB Demo")
    app.MainLoop()
