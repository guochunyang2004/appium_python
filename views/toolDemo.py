#-*- coding: utf-8 -*-

import wx
import win32api
import sys, os

APP_TITLE = u'菜单、工具栏、状态栏'
APP_ICON = 'res/python.ico'

class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''
    
    id_open = wx.NewId()
    id_save = wx.NewId()
    id_quit = wx.NewId()
    
    id_help = wx.NewId()
    id_about = wx.NewId()
    
    def __init__(self, parent):
        '''构造函数'''
        
        wx.Frame.__init__(self, parent, -1, APP_TITLE)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((800, 600))
        self.Center()
        
        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
            exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        else :
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        
        self.Maximize()
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE)
        
        self._CreateMenuBar()         # 菜单栏
        self._CreateToolBar()         # 工具栏
        self._CreateStatusBar()       # 状态栏
    
    def _CreateMenuBar(self):
        '''创建菜单栏'''
        
        self.mb = wx.MenuBar()
        
        # 文件菜单
        m = wx.Menu()
        m.Append(self.id_open, u"打开文件")
        m.Append(self.id_save, u"保存文件")
        m.AppendSeparator()
        m.Append(self.id_quit, u"退出系统")
        self.mb.Append(m, u"文件")
        
        self.Bind(wx.EVT_MENU, self.OnOpen, id=self.id_open)
        self.Bind(wx.EVT_MENU, self.OnSave, id=self.id_save)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=self.id_quit)
        
        # 帮助菜单
        m = wx.Menu()
        m.Append(self.id_help, u"帮助主题")
        m.Append(self.id_about, u"关于...")
        self.mb.Append(m, u"帮助")
        
        self.Bind(wx.EVT_MENU, self.OnHelp,id=self.id_help)
        self.Bind(wx.EVT_MENU, self.OnAbout,id=self.id_about)
        
        self.SetMenuBar(self.mb)
    
    def _CreateToolBar(self):
        '''创建工具栏'''
        
        bmp_open = wx.Bitmap('res/open_16.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        bmp_save = wx.Bitmap('res/save_16.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        bmp_help = wx.Bitmap('res/help_16.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        bmp_about = wx.Bitmap('res/about_16.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        
        self.tb = wx.ToolBar(self)
        self.tb.SetToolBitmapSize((16,16))
        
        self.tb.AddLabelTool(self.id_open, u'打开文件', bmp_open, shortHelp=u'打开', longHelp=u'打开文件')
        self.tb.AddLabelTool(self.id_save, u'保存文件', bmp_save, shortHelp=u'保存', longHelp=u'保存文件')
        self.tb.AddSeparator()
        self.tb.AddLabelTool(self.id_help, u'帮助', bmp_help, shortHelp=u'帮助', longHelp=u'帮助')
        self.tb.AddLabelTool(self.id_about, u'关于', bmp_about, shortHelp=u'关于', longHelp=u'关于...')
        
        #self.Bind(wx.EVT_TOOL_RCLICKED, self.OnOpen, id=self.id_open)
        
        self.tb.Realize()
    
    def _CreateStatusBar(self):
        '''创建状态栏'''
        
        self.sb = self.CreateStatusBar()
        self.sb.SetFieldsCount(3)
        self.sb.SetStatusWidths([-2, -1, -1])
        self.sb.SetStatusStyles([wx.SB_RAISED, wx.SB_RAISED, wx.SB_RAISED])
        
        self.sb.SetStatusText(u'状态信息0', 0)
        self.sb.SetStatusText(u'', 1)
        self.sb.SetStatusText(u'状态信息2', 2)
    
    def OnOpen(self, evt):
        '''打开文件'''
        
        self.sb.SetStatusText(u'打开文件', 1)
    
    def OnSave(self, evt):
        '''保存文件'''
        
        self.sb.SetStatusText(u'保存文件', 1)
    
    def OnQuit(self, evt):
        '''退出系统'''
        
        self.sb.SetStatusText(u'退出系统', 1)
        self.Destroy()
    
    def OnHelp(self, evt):
        '''帮助'''
        
        self.sb.SetStatusText(u'帮助', 1)
    
    def OnAbout(self, evt):
        '''关于'''
        
        self.sb.SetStatusText(u'关于', 1)
        
class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame(None)
        self.Frame.Show()
        return True

if __name__ == "__main__":
    app = mainApp()
    app.MainLoop()
