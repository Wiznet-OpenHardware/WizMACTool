# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import serial
import serial.tools.list_ports
import time
import threading
import os
import binascii


import wx
import wx.xrc

###########################################################################
## Class WIZnetMACTool
###########################################################################
class WIZnetMACTool ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"WIZnetMACTool", pos = wx.DefaultPosition, size = wx.Size( 646,435 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        bSizer_root = wx.BoxSizer( wx.VERTICAL )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_serialPort = wx.StaticText( self, wx.ID_ANY, u"Serial Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_serialPort.Wrap( -1 )
        bSizer5.Add( self.m_staticText_serialPort, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_serialCOMChoices = []
        self.m_comboBox_serialCOM = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_serialCOMChoices, 0 )
        bSizer5.Add( self.m_comboBox_serialCOM, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_baudrate = wx.StaticText( self, wx.ID_ANY, u"Baudrate", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_baudrate.Wrap( -1 )
        bSizer5.Add( self.m_staticText_baudrate, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBox_baudrateChoices = [ u"4800", u"9600", u"14400", u"19200", u"38400", u"57600", u"115200" ]
        self.m_comboBox_baudrate = wx.ComboBox( self, wx.ID_ANY, u"57600", wx.DefaultPosition, wx.DefaultSize, m_comboBox_baudrateChoices, 0 )
        bSizer5.Add( self.m_comboBox_baudrate, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_SerialConnect = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button_SerialConnect, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_SerialClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_SerialClose.Enable( False )
        
        bSizer5.Add( self.m_button_SerialClose, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer_root.Add( bSizer5, 0, wx.EXPAND, 5 )
        
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText_mac_addr = wx.StaticText( self, wx.ID_ANY, u"MAC", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_mac_addr.Wrap( -1 )
        bSizer2.Add( self.m_staticText_mac_addr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_mac_addr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl_mac_addr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_ReqHeader = wx.StaticText( self, wx.ID_ANY, u"Request", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_ReqHeader.Wrap( -1 )
        bSizer2.Add( self.m_staticText_ReqHeader, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_ReqHeader = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl_ReqHeader, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_RespHeader = wx.StaticText( self, wx.ID_ANY, u"Response", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_RespHeader.Wrap( -1 )
        bSizer2.Add( self.m_staticText_RespHeader, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_RespHeader = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl_RespHeader, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText_commandTail = wx.StaticText( self, wx.ID_ANY, u"Tail", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_commandTail.Wrap( -1 )
        bSizer2.Add( self.m_staticText_commandTail, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl_commandTail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl_commandTail, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer_root.Add( bSizer2, 0, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_mac_type1 = wx.CheckBox( self, wx.ID_ANY, u"Type1 : 00:08:DC:00:00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_mac_type1.SetValue(True) 
        bSizer7.Add( self.m_checkBox_mac_type1, 0, wx.ALL, 5 )
        
        self.m_checkBox_mac_type2 = wx.CheckBox( self, wx.ID_ANY, u"Type2 : 0008DC000000", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_checkBox_mac_type2, 0, wx.ALL, 5 )
        
        self.m_button_writeMAC = wx.Button( self, wx.ID_ANY, u"Write MAC", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button_writeMAC, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_checkBox_write_WIZ107SR_MAC = wx.CheckBox( self, wx.ID_ANY, u"For Writing WIZ107SR MAC", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_checkBox_write_WIZ107SR_MAC, 0, wx.ALL, 5 )
        
        self.m_checkBox_rewrite_WIZ107SR_MAC = wx.CheckBox( self, wx.ID_ANY, u"For ReWriting WIZ107SR MAC", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_checkBox_rewrite_WIZ107SR_MAC, 0, wx.ALL, 5 )
        
        
        bSizer6.Add( bSizer8, 1, wx.EXPAND, 5 )
        
        
        bSizer_root.Add( bSizer6, 0, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl_SerialMonitor = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
        bSizer3.Add( self.m_textCtrl_SerialMonitor, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer_root.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl_SerialInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_textCtrl_SerialInput, 1, wx.ALL, 5 )
        
        self.m_button_SendSerial = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button_SendSerial, 0, wx.ALL, 5 )
        
        
        bSizer_root.Add( bSizer4, 0, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer_root )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.file = wx.Menu()
        self.m_menuItem_save = wx.MenuItem( self.file, wx.ID_ANY, u"Save_Config", wx.EmptyString, wx.ITEM_NORMAL )
        self.file.AppendItem( self.m_menuItem_save )
        
        self.m_menubar1.Append( self.file, u"File" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_comboBox_serialCOM.Bind( wx.EVT_LEFT_DOWN, self.onSerialPort )
        self.m_button_SerialConnect.Bind( wx.EVT_BUTTON, self.onSerialConnect )
        self.m_button_SerialClose.Bind( wx.EVT_BUTTON, self.onSerialClose )
        self.m_checkBox_mac_type1.Bind( wx.EVT_CHECKBOX, self.onCheckBox_Type1 )
        self.m_checkBox_mac_type2.Bind( wx.EVT_CHECKBOX, self.onCheckBox_Type2 )
        self.m_button_writeMAC.Bind( wx.EVT_BUTTON, self.onWriteMAC )
        self.m_checkBox_write_WIZ107SR_MAC.Bind( wx.EVT_CHECKBOX, self.onWriteWIZ107SR_MAC )
        self.m_checkBox_rewrite_WIZ107SR_MAC.Bind( wx.EVT_CHECKBOX, self.onReWriteWIZ107SR_MAC )
        self.m_button_SendSerial.Bind( wx.EVT_BUTTON, self.onSerialSend )
        self.Bind( wx.EVT_MENU, self.onSaveMenu, id = self.m_menuItem_save.GetId() )
        
        # Connect Events
        self.m_comboBox_serialCOM.Bind( wx.EVT_LEFT_DOWN, self.onSerialPort )
        self.m_button_SerialConnect.Bind( wx.EVT_BUTTON, self.onSerialConnect )
        self.m_button_SerialClose.Bind( wx.EVT_BUTTON, self.onSerialClose )
        self.m_checkBox_mac_type1.Bind( wx.EVT_CHECKBOX, self.onCheckBox_Type1 )
        self.m_checkBox_mac_type2.Bind( wx.EVT_CHECKBOX, self.onCheckBox_Type2 )
        self.m_button_writeMAC.Bind( wx.EVT_BUTTON, self.onWriteMAC )
        self.m_checkBox_write_WIZ107SR_MAC.Bind( wx.EVT_CHECKBOX, self.onWriteWIZ107SR_MAC )
        self.m_checkBox_rewrite_WIZ107SR_MAC.Bind( wx.EVT_CHECKBOX, self.onReWriteWIZ107SR_MAC )
        self.m_button_SendSerial.Bind( wx.EVT_BUTTON, self.onSerialSend )
        self.Bind( wx.EVT_MENU, self.onSaveMenu, id = self.m_menuItem_save.GetId() )

        
        # User
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.SerialMonitoring, self.timer)
    
        self.GetComPortList()

        if os.path.isfile("config.ini"):
            f = open("config.ini","r")
            while True:
                str_config = f.readline()
                if len(str_config) == 0:
                    f.close()
                    wx.MessageBox("File information is wrong", 'Warning',wx.OK | wx.ICON_ERROR)
                    return

                if str_config[0] != '#':
                    break

            f.close()
        else:
            f = open("config.ini","w")
            f.write("# MAC_ADDRESS,BAUD_RATE,REQUEST_HEADER,RESPONSE_HEADER,TAIL_COMMAND\r\n")
            str_config = "0008DC000000,115200,S,R,,"
            f.write(str_config)
            f.close()
        
        if str_config.count(',') != 5:
            print str_config
            wx.MessageBox("File information is wrong(Count of Seperate)", 'Warning',wx.OK | wx.ICON_ERROR)
            return

        mac_addr = str_config.split(',')[0]
        if mac_addr.count(':') == 5:
            self.m_checkBox_mac_type1.SetValue(True)
            self.m_checkBox_mac_type2.SetValue(False)
        elif mac_addr.count(':') == 0:
            self.m_checkBox_mac_type1.SetValue(False)
            self.m_checkBox_mac_type2.SetValue(True)
        else:
            wx.MessageBox("File information is wrong", 'Warning',wx.OK | wx.ICON_ERROR)
            return

        self.m_textCtrl_mac_addr.SetValue(str_config.split(',')[0])
        self.m_comboBox_baudrate.SetValue(str_config.split(',')[1])
        self.m_textCtrl_ReqHeader.SetValue(str_config.split(',')[2])
        self.m_textCtrl_RespHeader.SetValue(str_config.split(',')[3])
        self.m_textCtrl_commandTail.SetValue(str_config.split(',')[4])
        
        self.m_serialIsOpen = False
        self.m_button_SendSerial.Disable()
        
    
    def __del__( self ):
        if self.m_serialIsOpen == True:
            self.ser.close();
    
    
    # Virtual event handlers, overide them in your derived class
    def onSerialPort( self, event ):
        self.GetComPortList()
    
    def onSerialConnect( self, event ):
        com = self.m_comboBox_serialCOM.GetValue()
        baud = int(self.m_comboBox_baudrate.GetValue())
        if com =='':
            wx.MessageBox("Please Select Serial Port", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        self.ser = serial.Serial(com, baud, timeout = 0.3)
        if(self.ser == -1):
            self.ser.close()
            wx.MessageBox("Serial Open Error.\r\n", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        self.m_button_SerialConnect.Disable()
        self.m_button_SerialClose.Enable()
        self.m_serialIsOpen = True
        
        self.timer.Start(1000)
        

    def onSerialClose( self, event ):
        self.timer.Stop()
        self.ser.close()
        self.m_button_SerialConnect.Enable()
        self.m_button_SerialClose.Disable()
        self.m_serialIsOpen = False
    

    def onWriteMAC( self, event ):
        self.timer.Stop()

        if self.m_checkBox_rewrite_WIZ107SR_MAC.GetValue() == True:
            self.ReWrite_WIZ107SR_MAC()
        elif self.m_checkBox_write_WIZ107SR_MAC.GetValue() == True:
            self.Write_WIZ107SR_MAC()
        else:
            self.Write_MAC()

        self.timer.Start(1000)

        #Increase MAC address        
        if self.m_checkBox_mac_type1.IsChecked():   #00:08:DC:00:00:00 format
            mac = self.m_textCtrl_mac_addr.GetValue()
            r = int(mac.replace(':',''),16) + 1
            mac = '{:X}'.format(r).zfill(12)
            self.m_textCtrl_mac_addr.SetValue(":".join(x+y for x,y in zip(mac[::2],mac[1::2])))
        else:                                       #0008DC000000 format
            mac = self.m_textCtrl_mac_addr.GetValue()
            r = int(mac.replace(':',''),16) + 1
            mac = '{:X}'.format(r).zfill(12)
            self.m_textCtrl_mac_addr.SetValue(mac)
        
        self.SaveConfigFile()
            
            
    def onCheckBox_Type1( self, event ):
        mac = self.m_textCtrl_mac_addr.GetValue()
        self.m_textCtrl_mac_addr.SetValue(":".join(x+y for x,y in zip(mac[::2],mac[1::2])))
        self.m_checkBox_mac_type1.SetValue(True)
        self.m_checkBox_mac_type2.SetValue(False)
    
    def onCheckBox_Type2( self, event ):
        mac = self.m_textCtrl_mac_addr.GetValue()
        self.m_textCtrl_mac_addr.SetValue(mac.replace(':',''))
        self.m_checkBox_mac_type1.SetValue(False)
        self.m_checkBox_mac_type2.SetValue(True)


    def onWriteWIZ107SR_MAC( self, event ):
        if self.m_checkBox_write_WIZ107SR_MAC.IsChecked():
            self.m_checkBox_mac_type1.Disable()
            self.m_checkBox_mac_type2.Disable()
            self.m_textCtrl_ReqHeader.Disable()
            self.m_textCtrl_RespHeader.Disable()
            self.m_textCtrl_commandTail.Disable()
            self.m_checkBox_rewrite_WIZ107SR_MAC.SetValue(False)
            
            if self.m_checkBox_mac_type1.IsChecked():
                return

            self.onCheckBox_Type1(event)
        else:
            self.m_checkBox_mac_type1.Enable()
            self.m_checkBox_mac_type2.Enable()
            self.m_textCtrl_ReqHeader.Enable()
            self.m_textCtrl_RespHeader.Enable()
            self.m_textCtrl_commandTail.Enable()
    
    def onReWriteWIZ107SR_MAC( self, event ):
        if self.m_checkBox_rewrite_WIZ107SR_MAC.IsChecked():
            self.m_checkBox_mac_type1.Disable()
            self.m_checkBox_mac_type2.Disable()
            self.m_textCtrl_ReqHeader.Disable()
            self.m_textCtrl_RespHeader.Disable()
            self.m_textCtrl_commandTail.Disable()
            self.m_checkBox_write_WIZ107SR_MAC.SetValue(False)
            
            
            if self.m_checkBox_mac_type1.IsChecked():
                return

            self.onCheckBox_Type1(event)
        else:
            self.m_checkBox_mac_type1.Enable()
            self.m_checkBox_mac_type2.Enable()
            self.m_textCtrl_ReqHeader.Enable()
            self.m_textCtrl_RespHeader.Enable()
            self.m_textCtrl_commandTail.Enable()
        
            
    def onSerialSend( self, event ):
        cmd = self.m_textCtrl_SerialInput.GetValue()
        self.ser.write(str(cmd))

    def SerialMonitoring(self,event):
        try:
            if self.ser.readable():
                str = self.ser.readall()
                if len(str) == 0:
                    return
                
                self.m_textCtrl_SerialMonitor.AppendText(str)
                self.ser.flush()
        except:
            self.timer.Stop()
            self.ser.close()
            self.m_button_SerialConnect.Enable()
            self.m_button_SerialClose.Disable()
            self.m_serialIsOpen = False
        
    def GetComPortList(self):
        comboBox_serial_portChoices = []
        
        self.available_ports = list(serial.tools.list_ports.comports())
        for self.port in self.available_ports:
            if(self.port[2] != 'n/a'):
                comboBox_serial_portChoices.append(self.port[0])
                 
        self.m_comboBox_serialCOM.SetItems(comboBox_serial_portChoices)
        
    def onSaveMenu( self, event ):
        self.SaveConfigFile()
        
    def SaveConfigFile(self):
        f = open("config.ini","w")
        f.write("# MAC_ADDRESS,BAUD_RATE,REQUEST_HEADER,RESPONSE_HEADER,TAIL_COMMAND\r\n")
        data  = self.m_textCtrl_mac_addr.GetValue() + ","  + self.m_comboBox_baudrate.GetValue() + "," 
        data += self.m_textCtrl_ReqHeader.GetValue() + "," + self.m_textCtrl_RespHeader.GetValue() + "," 
        data += self.m_textCtrl_commandTail.GetValue() + ","
        f.write(data)
        f.close()
        
    def Write_WIZ107SR_MAC(self):
        command = "MC" + self.m_textCtrl_mac_addr.GetValue() +"\r\n"
        self.ser.write(str(command))
        str_resp = self.ser.readall()
        self.m_textCtrl_SerialMonitor.AppendText(str_resp)
        self.m_textCtrl_SerialMonitor.AppendText("Read MAC Address\r\n")
        self.ser.write("\r\nMC\r\n")
        str_resp = self.ser.readline()
        self.m_textCtrl_SerialMonitor.AppendText(str_resp)
        self.m_textCtrl_SerialMonitor.AppendText("Finish Write MAC Address\r\n")


    def ReWrite_WIZ107SR_MAC(self):
        str_resp = ""
        message = ""

        self.ser.write("K!\r\n")
        self.ser.write("wiznet\r\n")
        
        str_resp = self.ser.readall()
        self.m_textCtrl_SerialMonitor.AppendText(str_resp)
        command = "MC" + self.m_textCtrl_mac_addr.GetValue() +"\r\n"
        self.ser.write(str(command))
        self.m_textCtrl_SerialMonitor.AppendText("Read MAC Address\r\n")
        self.ser.write("\r\nMC\r\n")
        str_resp = self.ser.readline()
        self.m_textCtrl_SerialMonitor.AppendText(str_resp)
        self.m_textCtrl_SerialMonitor.AppendText("Finish Write MAC Address\r\n")

        return True

    
    def Write_MAC(self):
        str_resp = ""

        #Send Request Header
        command = self.m_textCtrl_ReqHeader.GetValue()
        self.ser.write(str(command))

        #Receive response header and Compare with wanted response header
        wanted_resp = self.m_textCtrl_RespHeader.GetValue()
        if len(wanted_resp) != 0:
            str_resp += self.ser.read()

        self.m_textCtrl_SerialMonitor.AppendText(str_resp)            
        if str_resp != wanted_resp:
            wx.MessageBox("Protocol Error", 'Warning',wx.OK | wx.ICON_ERROR)
            return
        
        #Send MAC Address
        command = self.m_textCtrl_mac_addr.GetValue()
        #If tail is existed, Send tail as 0x0d,0x0a
        #command += self.m_textCtrl_commandTail.GetValue()
        command += binascii.a2b_hex(self.m_textCtrl_commandTail.GetValue())
        self.ser.write(str(command))



if __name__ == "__main__":
    app = wx.App(0)
    wiz_mac_tool = WIZnetMACTool(None)
    app.SetTopWindow(wiz_mac_tool)
    wiz_mac_tool.Show()
    app.MainLoop()