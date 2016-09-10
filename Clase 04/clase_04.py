# -*- coding: utf-8 -*-
import wx
from random import randint

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))
        sz = wx.BoxSizer(wx.VERTICAL)
        boton1 = wx.Button(self, -1, u"OK")
        boton2 = wx.Button(self, -1, u"NO OK")
        
        # Sizer
        sz.Add(boton1, 1, wx.EXPAND|wx.ALL, 10)
        sz.Add(boton2, 1, wx.EXPAND|wx.ALL, 10)
        
        # Evento
        self.Bind(wx.EVT_BUTTON, self.onClick)
        
        self.SetSizer(sz)
        self.Centre(True)
        self.Show()
        
    def onClick(self,event):
        label = event.GetEventObject().GetLabel()
        if label==u"OK":
            print "Hemos presionado OK"
        elif label==u"NO OK":
            print "Hemos presionado NO OK"


if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None,u"Botón")
    app.MainLoop()
