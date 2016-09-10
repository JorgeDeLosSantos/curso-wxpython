# -*- coding: utf-8 -*-
import wx

# wx.Panel

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))
        
        # Paneles 
        p1 = wx.Panel(self)
        p2 = wx.Panel(self)
        p3 = wx.Panel(p1)
        
        # Sizers 
        mainsz = wx.BoxSizer(wx.VERTICAL)
        p1sz = wx.BoxSizer(wx.HORIZONTAL)
        p2sz = wx.BoxSizer(wx.HORIZONTAL)
        p3sz = wx.BoxSizer(wx.VERTICAL)
        
        # Controles
        st1 = wx.StaticText(p1, -1, "Nombre")
        txtA = wx.TextCtrl(p3, -1)
        txtB = wx.TextCtrl(p3, -1)
        st2 = wx.StaticText(p2, -1, "Edad")
        txt2 = wx.TextCtrl(p2, -1)
        bt = wx.Button(self, -1, "OK")
        
        # Agregar elementos a los sizers
        p1sz.Add(st1, 1, wx.EXPAND|wx.ALL, 10)
        p1sz.Add(p3, 1, wx.EXPAND|wx.EXPAND, 10)
        p3sz.Add(txtA, 1, wx.EXPAND|wx.ALL, 10)
        p3sz.Add(txtB, 1, wx.EXPAND|wx.ALL, 10)
        p2sz.Add(st2, 1, wx.EXPAND|wx.ALL, 10)
        p2sz.Add(txt2, 3, wx.EXPAND|wx.ALL, 10)
        mainsz.Add(p1, 1, wx.EXPAND)
        mainsz.Add(p2, 1, wx.EXPAND)
        mainsz.Add(bt, 1, wx.ALIGN_CENTRE|wx.ALL, 10)
        
        # Conf. sizers
        p1.SetSizer(p1sz)
        p2.SetSizer(p2sz)
        p3.SetSizer(p3sz)
        self.SetSizer(mainsz)
        
        self.SetBackgroundColour(p1.GetBackgroundColour())
        
        self.Centre(True)
        self.Show()


if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None,u"Paneles")
    app.MainLoop()
