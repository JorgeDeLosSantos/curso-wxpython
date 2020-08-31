# -*- coding: utf-8 -*-
import wx

class TestFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(300,200))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        
        # Creating controls
        self.txt1 = wx.TextCtrl(self, -1, "")
        self.txt2 = wx.TextCtrl(self, -1, "")
        self.bt = wx.Button(self, -1, "Calcular")
        
        # Add controls to sizer
        self.sz.Add(self.txt1, 1, wx.EXPAND|wx.ALL, 10)
        self.sz.Add(self.txt2, 1, wx.EXPAND|wx.ALL, 10)
        self.sz.Add(self.bt, 1, wx.EXPAND|wx.ALL, 10)
        
        # Bind events
        self.Bind(wx.EVT_BUTTON, self.OnClick2)

        # Set sizer
        self.SetSizer(self.sz)
        
        # Centre and show frame
        self.Centre(True)
        self.Show()
        
    def OnClick(self,event):
        a = self.txt1.GetValue()
        b = self.txt2.GetValue()
        if a == "" or b == "":
            resp = wx.MessageBox("Inserte valores", caption="Mensaje", 
            style=wx.YES_NO | wx.CANCEL)
            
            if resp == wx.YES:
                print("Ha seleccionado Sí")
            elif resp == wx.NO:
                print("Ha seleccionado NO")
                
    def OnClick2(self,event):
        a = self.txt1.GetValue()
        b = self.txt2.GetValue()
        if a == "" or b == "":
            dlg = wx.MessageDialog(self, "Inserte valores", caption="Mensaje", 
            style = wx.YES_NO | wx.NO_DEFAULT)
            # ~ dlg.SetYesNoLabels("Aceptar","Rechazar")
            # ~ dlg.SetOKLabel("He entendido")
            resp = dlg.ShowModal()
            if resp == wx.ID_YES:
                print("Ha seleccionado SÍ")
            elif resp == wx.ID_NO:
                print("Ha rechazado la operación")


if __name__=='__main__':
    app = wx.App()
    frame = TestFrame(None, "MessageBox and MessageDialog Demo")
    app.MainLoop()
