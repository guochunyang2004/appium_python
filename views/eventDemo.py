#-*- coding: utf-8 -*-

import wx
import win32api
import sys, os

APP_TITLE = u'控件事件、鼠标事件、键盘事件、系统事件'
APP_ICON = 'res/python.ico'

class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''
    
    def __init__(self, parent):
        '''构造函数'''
        
        wx.Frame.__init__(self, parent, -1, APP_TITLE)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((520, 220))
        self.Center()
        
        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
            exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        else :
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        
        wx.StaticText(self, -1, u'第一行输入框：', pos=(40, 50), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, u'第二行输入框：', pos=(40, 80), size=(100, -1), style=wx.ALIGN_RIGHT)
        self.tip = wx.StaticText(self, -1, u'', pos=(145, 110), size=(150, -1), style=wx.ST_NO_AUTORESIZE)
        
        self.tc1 = wx.TextCtrl(self, -1, '', pos=(145, 50), size=(150, -1), name='TC01', style=wx.TE_CENTER)
        self.tc2 = wx.TextCtrl(self, -1, '', pos=(145, 80), size=(150, -1), name='TC02', style=wx.TE_PASSWORD|wx.ALIGN_RIGHT)
        
        btn_mea = wx.Button(self, -1, u'鼠标左键事件', pos=(350, 50), size=(100, 25))
        btn_meb = wx.Button(self, -1, u'鼠标所有事件', pos=(350, 80), size=(100, 25))
        btn_close = wx.Button(self, -1, u'关闭窗口', pos=(350, 110), size=(100, 25))
        
        # 控件事件
        self.tc1.Bind(wx.EVT_TEXT, self.EvtText)
        self.tc2.Bind(wx.EVT_TEXT, self.EvtText)
        self.Bind(wx.EVT_BUTTON, self.OnClose, btn_close)
        
        # 鼠标事件 
        btn_mea.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        btn_mea.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        btn_mea.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseWheel)
        btn_meb.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)
        
        # 键盘事件
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        
        # 系统事件
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_SIZE, self.On_size)
        #self.Bind(wx.EVT_PAINT, self.On_paint)
        #self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
        
    def EvtText(self, evt):
        '''输入框事件函数'''
        
        obj = evt.GetEventObject()
        objName = obj.GetName()
        text = evt.GetString()
        
        if objName == 'TC01':
            self.tc2.SetValue(text)
        elif objName == 'TC02':
            self.tc1.SetValue(text)
    
    def On_size(self, evt):
        '''改变窗口大小事件函数'''
        
        self.Refresh()
        evt.Skip() # 体会作用
    
    def OnClose(self, evt):
        '''关闭窗口事件函数'''
        
        dlg = wx.MessageDialog(None, u'确定要关闭本窗口？', u'操作提示', wx.YES_NO | wx.ICON_QUESTION)
        if(dlg.ShowModal() == wx.ID_YES):
            self.Destroy()
    
    def OnLeftDown(self, evt):
        '''左键按下事件函数'''
        
        self.tip.SetLabel(u'左键按下')
    
    def OnLeftUp(self, evt):
        '''左键弹起事件函数'''
        
        self.tip.SetLabel(u'左键弹起')
    
    def OnMouseWheel(self, evt):
        '''鼠标滚轮事件函数'''
        
        vector = evt.GetWheelRotation()
        self.tip.SetLabel(str(vector))
    
    def OnMouse(self, evt):
        '''鼠标事件函数'''
        
        self.tip.SetLabel(str(evt.EventType))
    
    def OnKeyDown(self, evt):
        '''键盘事件函数'''
        
        key = evt.GetKeyCode() 
        self.tip.SetLabel(str(key))
        
class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame(None)
        self.Frame.Show()
        return True

if __name__ == "__main__":
    app = mainApp()
    app.MainLoop()
