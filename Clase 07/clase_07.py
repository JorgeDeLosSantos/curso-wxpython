# -*- coding: utf-8 -*-
import wx

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title,size=(300,200))
        
        # Crear barra de menú
        barra_menu = wx.MenuBar()
        
        # Menú archivo
        menu_archivo = wx.Menu()
        m_abrir = wx.Menu() # Abrir PDF | Abrir HTML
        m_abrir.Append(-1, "HTML")
        m_abrir.Append(-1, "PDF")
        menu_archivo.AppendMenu(-1, "Abrir", m_abrir)
        m_salir = menu_archivo.Append(-1, "Salir\tCtrl-Q")
        
        # Menú editar
        menu_editar = wx.Menu()
        m_copiar = menu_editar.Append(-1, "Copiar")
        m_cortar = menu_editar.Append(-1, "Cortar")
        m_pegar = menu_editar.Append(-1, "Pegar")
        
        # Agregando al menú principal
        barra_menu.Append(menu_archivo, "Archivo")
        barra_menu.Append(menu_editar, "Editar")
        
        self.SetMenuBar(barra_menu)
        
        # Eventos
        self.Bind(wx.EVT_MENU, self.salir, m_salir)
        
        self.Centre(True)
        self.Show()
        
    def salir(self,event):
        self.Close(True)


if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None,"Menú")
    app.MainLoop()
