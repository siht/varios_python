#Boa:Frame:Frame1

import wx
from calculadora import calculadora

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1CHK_ACTIVAR, 
 wxID_FRAME1LBL_HOSTS, wxID_FRAME1LBL_IP, wxID_FRAME1LBL_SUBNETS, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICLINE1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1TXT_HOSTS, wxID_FRAME1TXT_IP, wxID_FRAME1TXT_MS, 
 wxID_FRAME1TXT_RESULTADOS, wxID_FRAME1TXT_SUBNETS, 
] = [wx.NewId() for _init_ctrls in range(14)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(353, 82), size=wx.Size(275, 528),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Calculadora de ip')
        self.SetClientSize(wx.Size(267, 493))
        self.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.SetBackgroundColour(wx.Colour(234, 200, 149))
        self.SetIcon(wx.Icon(u'./Boa.ico',
              wx.BITMAP_TYPE_ICO))

        self.lbl_ip = wx.StaticText(id=wxID_FRAME1LBL_IP,
              label=u'ingrese su ip', name=u'lbl_ip', parent=self,
              pos=wx.Point(24, 16), size=wx.Size(60, 13), style=0)

        self.txt_ip = wx.TextCtrl(id=wxID_FRAME1TXT_IP, name=u'txt_ip',
              parent=self, pos=wx.Point(24, 32), size=wx.Size(152, 21), style=0,
              value=u'')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'ingrese la mascara de subred', name='staticText1',
              parent=self, pos=wx.Point(24, 88), size=wx.Size(140, 13),
              style=0)

        self.txt_ms = wx.TextCtrl(id=wxID_FRAME1TXT_MS, name=u'txt_ms',
              parent=self, pos=wx.Point(24, 104), size=wx.Size(152, 21),
              style=0, value=u'')
        self.txt_ms.Enable(False)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'generar',
              name='button1', parent=self, pos=wx.Point(16, 248),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.lbl_hosts = wx.StaticText(id=wxID_FRAME1LBL_HOSTS,
              label=u'ingrese el numero de hosts que desea', name=u'lbl_hosts',
              parent=self, pos=wx.Point(24, 136), size=wx.Size(182, 13),
              style=0)

        self.txt_hosts = wx.TextCtrl(id=wxID_FRAME1TXT_HOSTS, name=u'txt_hosts',
              parent=self, pos=wx.Point(24, 152), size=wx.Size(152, 21),
              style=0, value=u'')
        self.txt_hosts.Enable(True)

        self.txt_resultados = wx.StaticText(id=wxID_FRAME1TXT_RESULTADOS,
              label=u'', name=u'txt_resultados', parent=self, pos=wx.Point(16,
              280), size=wx.Size(88, 13), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1, label=u'',
              name='staticBox1', parent=self, pos=wx.Point(16, 56),
              size=wx.Size(224, 176), style=0)
        self.staticBox1.SetHelpText(u'')

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(17, 130),
              size=wx.Size(223, 2), style=0)

        self.chk_activar = wx.CheckBox(id=wxID_FRAME1CHK_ACTIVAR,
              label=u'activar', name=u'chk_activar', parent=self,
              pos=wx.Point(176, 72), size=wx.Size(48, 13), style=0)
        self.chk_activar.SetValue(False)
        self.chk_activar.Show(True)
        self.chk_activar.Bind(wx.EVT_CHECKBOX, self.OnChk_activarCheckbox,
              id=wxID_FRAME1CHK_ACTIVAR)

        self.lbl_subnets = wx.StaticText(id=wxID_FRAME1LBL_SUBNETS,
              label=u'ingrese el numero de subredes que desea',
              name=u'lbl_subnets', parent=self, pos=wx.Point(24, 184),
              size=wx.Size(200, 13), style=0)

        self.txt_subnets = wx.TextCtrl(id=wxID_FRAME1TXT_SUBNETS,
              name=u'txt_subnets', parent=self, pos=wx.Point(24, 200),
              size=wx.Size(152, 21), style=0, value=u'')
        self.txt_subnets.Enable(True)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        ip = str(self.txt_ip.GetLabel())
        ms = str(self.txt_ms.GetLabel())
        ms = None if ms =="" else ms
        hosts = int(self.txt_hosts.Value) if not self.txt_hosts.IsEmpty() else 0
        subnets = int(self.txt_subnets.Value) if not self.txt_subnets.IsEmpty() else 0
        respuestas = []
        try:
            if self.chk_activar.Value:
                red = calculadora.Red(ip,ms)
            else:
                red = calculadora.Red(ip)
        except Exception, e:
            dlg = wx.MessageDialog(self, str(e), 'hay errores en tus datos', wx.OK | wx.ICON_INFORMATION)
            try:
                result = dlg.ShowModal()
            finally:
                dlg.Destroy()
        res = ''
        if self.chk_activar.Value:
            res += 'ip:\n' + str(red.Ip) + '\n'
            res += 'ip clase:\n' + str(red.Ip.Clase) + '\n'
            res += 'mascara:\n' + str(red.Mascara) + '\n'
            res += 'mascara clase:\n' + str(red.Mascara.Clase) + '\n'
            res += 'numero hosts por segmento:\n' + str(red.N_hosts_por_segmento) + '\n'
            res += 'numero de subredes:\n' + str(red.Subredes) +'\n'
            res += 'numero de redes:\n' + str(red.N_redes) + '\n'
            res += 'identificador de la red:\n' + str(red.get_ids())
        else:
            if red:
                longitud ={'A': 8*3,'B': 8*2,'C':8}
                redes_maximas = ( 1 << subnets.bit_length() ) - 1
                if hosts > 0 :
                    hosts_maximos = 1 << int(hosts + 2).bit_length()
                if hosts == (1 << hosts.bit_length()) -2 & hosts != 2:
                    hosts_maximos = hosts
##                hosts_maximos = (1 << int(hosts + 2).bit_length()) if hosts > 0 else 0
##                hosts_maximos = hosts_maximos if (hosts + 2) > (1<< hosts.bit_length()+1) else hosts
                aux = redes_maximas << hosts_maximos.bit_length()
                completo = 0
                out = []
                respuestas.append(hosts_maximos)
                try:
                    if redes_maximas and hosts_maximos:
                        if longitud[red.Mascara.Clase] > aux.bit_length():
                            diferencia = longitud[red.Mascara.Clase] - aux.bit_length()
                            faltante = ((1 << diferencia) - 1) ^ ((1 << aux.bit_length()) - 1)
                            recorrimiento = int(hosts_maximos - 1).bit_length()
                            completo = (1 << 32) - 1
                            completo = completo >> recorrimiento
                            completo = completo << recorrimiento
                            if red.Mascara.Clase == 'A':
                                out = [255]
                                out.append(int(completo >> (8*2) & 255))
                                out.append(int((completo >> 8) & 255))
                                out.append(int(completo & 255))
                            elif red.Mascara.Clase == 'B':
                                out = [255,255]
                                out.append(int((completo >> 8) & 255))
                                out.append(int(completo & 255))
                            elif red.Mascara.Clase == 'C':
                                out = [255,255,255]
                                out.append(int(completo & 255))
                            ms = '.'.join(["%i" %i for i in out])
                            red.Mascara = ms
                            respuestas.append(((1<<32) - 1) >> recorrimiento)
                        else:
                            raise Exception, "reduce tus hosts o tus redes"
                    else:
                        raise Exception, "ninguno de los valores debe ser cero"
                except Exception, e:
                    dlg = wx.MessageDialog(self, str(e), 'Caption', wx.OK | wx.ICON_INFORMATION)
                    try:
                        result = dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                    hosts = 'n/a'
                    subnets = 'n/a'
                    ms = 'n/a'
                res += 'mascara de subred:\n' + str(red.Mascara)+'\n'
                res += 'hosts pedidos:\n' + str(hosts) +'\n'
                res += 'subredes pedidas:\n' + str(subnets) + '\n'
                res += 'subredes disponibles:\n' + str(red.Subredes) + '\n'
                res += 'subredes desperdiciadas:\n' + str(red.Subredes - subnets) + '\n'
                res += 'numero hosts disponibles por segmento:\n' + str(red.N_hosts_por_segmento) + '\n'
                res += 'numero de hosts desperdiciados por segmento:\n' + str(red.N_hosts_por_segmento - hosts) + '\n'
                res += 'total de hosts desperdiciados:\n' + str((red.N_hosts_por_segmento - hosts) * red.Subredes)
        self.txt_resultados.Label = res
        event.Skip()

    def OnChk_activarCheckbox(self, event):
        if self.chk_activar.Value:
            self.txt_ms.Enable()
            self.txt_hosts.Disable()
            self.txt_subnets.Disable()
        else:
            self.txt_ms.Disable()
            self.txt_hosts.Enable()
            self.txt_subnets.Enable()
        event.Skip()
