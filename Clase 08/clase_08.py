# -*- coding: utf-8 -*-
import wx

class wxEditor(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title,size=(400,300))
        # Archivo
        self.archivo = ""
        
        # TextCtrl
        self.initCtrls()
        
        # Crear menu
        self.initMenu()
        
        # Iniciar app
        self.initApp()
        
        self.Centre(True)
        self.Show()
        
    def initApp(self):
        if self.archivo != "":
            f = open(self.archivo, "r")
            txt = f.read().decode('utf8')
            f.close()
            self.editor.SetValue(txt)
        
    def initCtrls(self):
        self.editor = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        
    def initMenu(self):
        barra_menu = wx.MenuBar()
        
        # Menú archivo
        marchivo = wx.Menu()
        m_guardar = marchivo.Append(-1, "Guardar\tCtrl-S")
        m_salir = marchivo.Append(-1, "Salir\tCtrl-Q")
        
        # Agregar el Menú principal (BM)
        barra_menu.Append(marchivo, "Archivo")
        
        self.SetMenuBar(barra_menu)
        
        # Eventos menú
        self.Bind(wx.EVT_MENU, self.salir, m_salir)
        self.Bind(wx.EVT_MENU, self.guardar, m_guardar)
        
    def salir(self,event):
        self.Close(True)
        
    def guardar(self,event):
        self.archivo = raw_input("Nombre del archivo: ")
        txt = self.editor.GetValue()
        f = open(self.archivo, "w")
        f.write(txt.encode('utf8'))
        f.close()
        print "Guardado..."
        

if __name__=='__main__':
    app = wx.App()
    frame = wxEditor(None,u"Editor")
    app.MainLoop()
