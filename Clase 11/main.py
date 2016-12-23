# -*- coding: utf-8 -*-
import wx
from gui01 import TestFrame

if __name__ == '__main__':
    app = wx.App()
    fr = TestFrame(None)
    fr.Show()
    app.MainLoop()

