
import wx

class Ventana4(wx.Frame):
    def __init__(self, parent, informacion="", subtotal1=0, informacion2="", subtotal2=0):
        # begin wxGlade: Ventana4.__init__
        super().__init__(parent, style= wx.DEFAULT_FRAME_STYLE)
        self.SetSize((702, 788))
        self.SetTitle("frame_3")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_1.SetBackgroundColour(wx.Colour(255, 119, 255))

        self.infoTaquilla = informacion
        self.infoDulceria = informacion2
        self.subtotalTaquilla = subtotal1
        self.subtotalDulceria = subtotal2
        self.lbtotal=self.subtotalTaquilla + self.subtotalTaquilla 

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_8 = wx.GridSizer(6, 1, 0, 0)
        sizer_1.Add(grid_sizer_8, 1, wx.EXPAND, 0)

        grid_sizer_9 = wx.GridSizer(2, 1, 0, 0)
        grid_sizer_8.Add(grid_sizer_9, 1, wx.EXPAND, 0)

        grid_sizer_12 = wx.GridSizer(1, 3, 0, 0)
        grid_sizer_9.Add(grid_sizer_12, 1, wx.EXPAND, 0)

        bitmap_1 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\nao1\\naa.jfif", wx.BITMAP_TYPE_ANY))
        grid_sizer_12.Add(bitmap_1, 0, 0, 0)

        label_6 = wx.StaticText(self.panel_1, wx.ID_ANY, "TICKET")
        label_6.SetFont(wx.Font(10, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Showcard Gothic"))
        grid_sizer_12.Add(label_6, 0, wx.ALIGN_CENTER, 0)

        bitmap_2 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\nao1\\naa.jfif", wx.BITMAP_TYPE_ANY))
        grid_sizer_12.Add(bitmap_2, 0, 0, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "TAQUILLA")
        label_1.SetFont(wx.Font(9, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Showcard Gothic"))
        grid_sizer_9.Add(label_1, 0, wx.ALIGN_CENTER, 0)

        lbTaquilla = wx.StaticText(self.panel_1, wx.ID_ANY, f"{self.infoTaquilla}", style=wx.ALIGN_CENTER_HORIZONTAL)
        grid_sizer_8.Add(lbTaquilla, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        grid_sizer_10 = wx.GridSizer(2, 1, 0, 0)
        grid_sizer_8.Add(grid_sizer_10, 1, wx.EXPAND, 0)

        lbSubtotalTaquilla = wx.StaticText(self.panel_1, wx.ID_ANY, f"SUBTOTAL: ${self.subtotalTaquilla}")
        grid_sizer_10.Add(lbSubtotalTaquilla, 0, 0, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "DULCERIA")
        label_2.SetFont(wx.Font(8, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Showcard Gothic"))
        grid_sizer_10.Add(label_2, 0, wx.ALIGN_CENTER, 0)

        lbDulceria = wx.StaticText(self.panel_1, wx.ID_ANY, f"{self.infoDulceria}", style=wx.ALIGN_CENTER_HORIZONTAL)
        grid_sizer_8.Add(lbDulceria, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        grid_sizer_11 = wx.GridSizer(2, 1, 0, 0)
        grid_sizer_8.Add(grid_sizer_11, 1, wx.EXPAND, 0)

        lbSubtotalDulceria = wx.StaticText(self.panel_1, wx.ID_ANY, f"SUBTOTAL: ${self.subtotalDulceria}")
        grid_sizer_11.Add(lbSubtotalDulceria, 0, 0, 0)

        lbTotal = wx.StaticText(self.panel_1, wx.ID_ANY, f"TOTAL : ${self.lbtotal}")
        grid_sizer_11.Add(lbTotal, 0, 0, 0)

        grid_sizer_13 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_8.Add(grid_sizer_13, 1, wx.EXPAND, 0)

        self.btnCancelar = wx.Button(self.panel_1, wx.ID_ANY, "CANCELAR\n")
        grid_sizer_13.Add(self.btnCancelar, 0, wx.ALIGN_CENTER, 0)

        self.btnFinalizar = wx.Button(self.panel_1, wx.ID_ANY, "FINALIZAR\n")
        grid_sizer_13.Add(self.btnFinalizar, 0, wx.ALIGN_CENTER, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.btnCancelar.Bind(wx.EVT_BUTTON, self.cancelarVenta)
        self.btnFinalizar.Bind(wx.EVT_BUTTON, self.finalizarVenta)
        # end wxGlade
        
    def cancelarVenta(self, event):  # wxGlade: Ventana4.<event_handler>
        pregunta = wx.MessageDialog(self, "Se cerrara la ventana.\n ¿Esta seguro que desea cancelar la venta?", "Confirmar salida",style=wx.YES_NO | wx.ICON_QUESTION)
        
        respuesta=pregunta.ShowModal()
        pregunta.Destroy()

        if respuesta == wx.ID_YES:
            print("Bye")
            self.Close()  
        event.Skip()

    def finalizarVenta(self, event):  # wxGlade: Ventana4.<event_handler>
        pregunta= wx.MessageDialog(
        self,
        f"Subtotal Taquilla: $ {self.subtotalTaquilla} \n"
        f"Subtotal Dulceria: $ {self.subtotalDulceria} \n\n",
        "Venta Finalizada",
        style=wx.YES_NO | wx.ICON_QUESTION
        )
        respuesta = pregunta.ShowModal()
        pregunta.Destroy()

        if respuesta ==  wx.ID_YES:
            print(f"Venta Realizada\n {self.subtotalTaquilla}, {self.subtotalDulceria} ")
            v2 = Ventana2(self)
            v2.Show()
            self.limpiarValores_Campos()
            self.Hide()
        elif respuesta ==  wx.ID_NO:
            self.limpiarValores_Campos()
        
        event.Skip()
# end of class Ventana4

class Ventana3(wx.Frame):
    def __init__(self, parent, informacion="", subtotal=0):
        super().__init__(parent, style=wx.DEFAULT_FRAME_STYLE) 
        self.SetSize((890, 820))
        self.SetTitle("Dulceria")
        print(f"Datos de la ventana 2:\n Informacion: {informacion} \n") 
        print(f"subtotal: {subtotal}")
        self.SetBackgroundColour(wx.Colour(255, 119, 255))  
        self.subtotalDulceria=0
        self.infoDulceria=""
        self.infoTaquilla=informacion
        self.subtotalTaquilla=subtotal 

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.GridSizer(1, 3, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        bitmap_4 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("E:/ADATA/dulces.jfif", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_4, 0, wx.ALIGN_CENTER, 0)

        label_1 = wx.StaticText(self, wx.ID_ANY, "Dulceria")
        label_1.SetFont(wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Showcard Gothic"))
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        bitmap_5 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("E:/ADATA/dulces.jfif", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_5, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_4 = wx.GridSizer(1, 6, 0, 0)
        sizer_1.Add(grid_sizer_4, 1, wx.EXPAND, 0)

        self.spComboB = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_4.Add(self.spComboB, 0, 0, 0)

        grid_sizer_5 = wx.GridSizer(3, 1, 0, 0)
        grid_sizer_4.Add(grid_sizer_5, 1, wx.EXPAND, 0)

        label_2 = wx.StaticText(self, wx.ID_ANY, "Basico $75")
        label_2.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_5.Add(label_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        label_3 = wx.StaticText(self, wx.ID_ANY, "Palomitas ch")
        label_3.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_5.Add(label_3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        label_4 = wx.StaticText(self, wx.ID_ANY, "Refresco ch")
        label_4.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_5.Add(label_4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        bitmap_6 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\nao1\\palooooo.jfif", wx.BITMAP_TYPE_ANY))
        grid_sizer_4.Add(bitmap_6, 0, wx.EXPAND, 0)

        self.spComboC = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_4.Add(self.spComboC, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_6 = wx.GridSizer(3, 1, 0, 0)
        grid_sizer_4.Add(grid_sizer_6, 1, wx.EXPAND, 0)

        label_5 = wx.StaticText(self, wx.ID_ANY, "Cuates $130")
        label_5.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_6.Add(label_5, 0, 0, 0)

        label_6 = wx.StaticText(self, wx.ID_ANY, "Palomitas md")
        label_6.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_6.Add(label_6, 0, 0, 0)

        label_7 = wx.StaticText(self, wx.ID_ANY, "2 Refrescos md")
        label_7.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_6.Add(label_7, 0, 0, 0)

        bitmap_7 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\nao1\\palooooo.jfif", wx.BITMAP_TYPE_ANY))
        grid_sizer_4.Add(bitmap_7, 0, wx.EXPAND, 0)

        grid_sizer_7 = wx.GridSizer(1, 3, 0, 0)
        sizer_1.Add(grid_sizer_7, 1, wx.EXPAND, 0)

        self.spComboF = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_7.Add(self.spComboF, 0, 0, 0)

        grid_sizer_8 = wx.GridSizer(4, 1, 0, 0)
        grid_sizer_7.Add(grid_sizer_8, 1, wx.EXPAND, 0)

        label_8 = wx.StaticText(self, wx.ID_ANY, "Familiar")
        label_8.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_8.Add(label_8, 0, 0, 0)

        label_9 = wx.StaticText(self, wx.ID_ANY, "Palomitas G")
        label_9.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_8.Add(label_9, 0, 0, 0)

        label_10 = wx.StaticText(self, wx.ID_ANY, "3 Refrescos grandes")
        label_10.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_8.Add(label_10, 0, 0, 0)

        label_11 = wx.StaticText(self, wx.ID_ANY, "1 Dulce")
        label_11.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_8.Add(label_11, 0, 0, 0)

        bitmap_9 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("E:/ADATA/dulces.jfif", wx.BITMAP_TYPE_ANY))
        grid_sizer_7.Add(bitmap_9, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)

        grid_sizer_9 = wx.GridSizer(1, 4, 0, 0)
        sizer_1.Add(grid_sizer_9, 1, wx.EXPAND, 0)

        label_12 = wx.StaticText(self, wx.ID_ANY, "Palomitas")
        label_12.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_9.Add(label_12, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)

        bitmap_2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\nao1\\palooooo.jfif", wx.BITMAP_TYPE_ANY))
        grid_sizer_9.Add(bitmap_2, 0, wx.EXPAND, 0)

        label_17 = wx.StaticText(self, wx.ID_ANY, "Refrescos")
        label_17.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_9.Add(label_17, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 0)

        bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\nao1\\pngrefresco.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_9.Add(bitmap_1, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_10 = wx.GridSizer(1, 3, 0, 0)
        sizer_1.Add(grid_sizer_10, 1, wx.EXPAND, 0)

        grid_sizer_13 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_10.Add(grid_sizer_13, 1, wx.EXPAND, 0)

        self.spPalomitasCh = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_13.Add(self.spPalomitasCh, 0, wx.ALIGN_CENTER, 0)

        label_13 = wx.StaticText(self, wx.ID_ANY, "Chicas")
        label_13.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_13.Add(label_13, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        grid_sizer_16 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_10.Add(grid_sizer_16, 1, wx.EXPAND, 0)

        label_18 = wx.StaticText(self, wx.ID_ANY, "Tamaño")
        label_18.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_16.Add(label_18, 0, wx.ALIGN_BOTTOM | wx.EXPAND, 0)

        label_19 = wx.StaticText(self, wx.ID_ANY, "Sabor")
        label_19.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_16.Add(label_19, 0, wx.ALIGN_BOTTOM | wx.EXPAND, 0)

        label_20 = wx.StaticText(self, wx.ID_ANY, "Cantidad")
        label_20.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_10.Add(label_20, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)

        grid_sizer_11 = wx.GridSizer(1, 3, 0, 0)
        sizer_1.Add(grid_sizer_11, 1, wx.EXPAND, 0)

        grid_sizer_14 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_11.Add(grid_sizer_14, 1, wx.EXPAND, 0)

        self.spPalomitasMd = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_14.Add(self.spPalomitasMd, 0, wx.ALIGN_CENTER, 0)

        label_14 = wx.StaticText(self, wx.ID_ANY, "Medianas")
        label_14.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_14.Add(label_14, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        grid_sizer_17 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_11.Add(grid_sizer_17, 1, wx.EXPAND, 0)

        self.cmbTamano = wx.ComboBox(self, wx.ID_ANY, choices=["Chico", "Mediano", "Grande"], style=wx.CB_DROPDOWN)
        grid_sizer_17.Add(self.cmbTamano, 0, wx.ALIGN_CENTER, 0)

        self.cmbSabor = wx.ComboBox(self, wx.ID_ANY, choices=["Limon", "Piña", "Tamarindo"], style=wx.CB_DROPDOWN)
        grid_sizer_17.Add(self.cmbSabor, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_2 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_11.Add(grid_sizer_2, 1, wx.EXPAND, 0)

        self.spCantidad = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100, style=wx.ALIGN_LEFT)
        grid_sizer_2.Add(self.spCantidad, 0, wx.ALIGN_CENTER, 0)

        self.btnAgregar = wx.Button(self, wx.ID_ANY, "Agregar\n")
        grid_sizer_2.Add(self.btnAgregar, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_12 = wx.GridSizer(1, 3, 0, 0)
        sizer_1.Add(grid_sizer_12, 1, wx.EXPAND, 0)

        grid_sizer_15 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_12.Add(grid_sizer_15, 1, wx.EXPAND, 0)

        self.spPalomitasG = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_15.Add(self.spPalomitasG, 0, wx.ALIGN_CENTER, 0)

        label_15 = wx.StaticText(self, wx.ID_ANY, "Grandes")
        label_15.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_15.Add(label_15, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        bitmap_10 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\nao1\\pngrefresco.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_12.Add(bitmap_10, 0, wx.ALIGN_CENTER, 0)

        bitmap_11 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\nao1\\pngrefresco.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_12.Add(bitmap_11, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_3 = wx.GridSizer(2, 1, 0, 0)
        sizer_1.Add(grid_sizer_3, 1, wx.EXPAND, 0)

        grid_sizer_19 = wx.GridSizer(1, 3, 0, 0)
        grid_sizer_3.Add(grid_sizer_19, 1, wx.EXPAND, 0)

        self.lbProductosAgregados = wx.StaticText(self, wx.ID_ANY, "Productos agregados:")
        self.lbProductosAgregados.SetFont(wx.Font(9, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Showcard Gothic"))
        grid_sizer_19.Add(self.lbProductosAgregados, 0, 0, 0)

        label_21 = wx.StaticText(self, wx.ID_ANY, "Subtotal Dulceria:")
        label_21.SetFont(wx.Font(9, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Showcard Gothic"))
        grid_sizer_19.Add(label_21, 0, 0, 0)

        self.lbSubtotal = wx.StaticText(self, wx.ID_ANY, "$00.00")
        self.lbSubtotal.SetFont(wx.Font(9, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Showcard Gothic"))
        grid_sizer_19.Add(self.lbSubtotal, 0, 0, 0)

        grid_sizer_18 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_3.Add(grid_sizer_18, 1, wx.EXPAND, 0)

        self.btnLimpiar = wx.Button(self, wx.ID_ANY, "Limpiar\n")
        grid_sizer_18.Add(self.btnLimpiar, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.btnSiguiente = wx.Button(self, wx.ID_ANY, "Siguiente\n")
        grid_sizer_18.Add(self.btnSiguiente, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.SetSizer(sizer_1)

        self.Layout()

        self.spComboB.Bind(wx.EVT_SPINCTRL, self.calcularComboBasico)
        self.spComboC.Bind(wx.EVT_SPINCTRL, self.calcularComboCuates)
        self.spComboF.Bind(wx.EVT_SPINCTRL, self.calcularComboFamiliar)
        self.spPalomitasCh.Bind(wx.EVT_SPINCTRL, self.calcularPalomitasCh)
        self.spPalomitasMd.Bind(wx.EVT_SPINCTRL, self.calcularPalomitasMd)
        self.btnAgregar.Bind(wx.EVT_BUTTON, self.agregarRefresco)
        self.spPalomitasG.Bind(wx.EVT_SPINCTRL, self.calcularPalomitasG)
        self.btnLimpiar.Bind(wx.EVT_BUTTON, self.limpiarDulceria)
        self.btnSiguiente.Bind(wx.EVT_BUTTON, self.siguienteDulceria)
        # end wxGlade

    def calcularComboBasico (self, event):  
        numero=int(self.spComboB.GetValue())
        subtotalcombo=numero*75
        self.subtotalDulceria=self.subtotalDulceria+subtotalcombo 
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria}")
        self.infoDulceria=self.infoDulceria + f"{numero} Combos Básicos \n" 
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()
    def calcularComboCuates(self, event):  #wxGlade: Ventana3.<event_handler>
        numero=int(self.spComboB.GetValue())
        subtotalcombo=numero*80
        self.subtotalDulceria=self.subtotalDulceria+subtotalcombo 
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria}")
        self.infoDulceria=self.infoDulceria + f"{numero} Combos Cuates \n" 
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def calcularComboFamiliar(self, event):  # wxGlade: Ventana3.<event_handler>
        numero=int(self.spComboB.GetValue())
        subtotalcombo=numero*100
        self.subtotalDulceria=self.subtotalDulceria+subtotalcombo 
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria}")
        self.infoDulceria=self.infoDulceria + f"{numero} Combos Familiar \n" 
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def calcularPalomitasCh(self, event):  # wxGlade: Ventana3.<event_handler>
        numero=int(self.spComboB.GetValue())
        subtotalcombo=numero*25
        self.subtotalDulceria=self.subtotalDulceria+subtotalcombo 
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria}")
        self.infoDulceria=self.infoDulceria + f"{numero} Combos Palomitas Ch \n" 
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def calcularPalomitasMd(self, event):  # wxGlade: Ventana3.<event_handler>
        numero=int(self.spComboB.GetValue())
        subtotalcombo=numero*30
        self.subtotalDulceria=self.subtotalDulceria+subtotalcombo 
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria}")
        self.infoDulceria=self.infoDulceria + f"{numero} Combos Palomitas Md \n" 
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def calcularPalomitasG(self, event):  # wxGlade: Ventana3.<event_handler>
        numero=int(self.spComboB.GetValue())
        subtotalcombo=numero*60
        self.subtotalDulceria=self.subtotalDulceria+subtotalcombo 
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria}")
        self.infoDulceria=self.infoDulceria + f"{numero} Combos Palomitas G \n" 
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def agregarRefresco(self, event):  # wxGlade: Ventana3.<event_handler>
        numero=int(self.spCantidad.GetValue())
        tamanyo=self.cmbTamano.GetValue()
        sabor=self.cmbSabor.GetValue()
        subtotalrefresco=0
        if tamanyo == "CHICO":
            subtotalrefresco=numero*25
        elif tamanyo == "MEDIANO":
            subtotalrefresco=numero*40
        elif tamanyo == "GRANDE":
            subtotalrefresco=numero*60

        self.subtotalDulceria=self.subtotalDulceria+subtotalrefresco
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria}")

        self.infoDulceria=self.infoDulceria + f"{numero} Refresco: {sabor} tamaño {tamanyo}\n"
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def limpiarD(self):  # wxGlade: Ventana3.<event_handler>
        self.subtotalDulceria=0
        self.infoDulceria=""

        self.spComboB.SetValue(0) 
        self.spComboC.SetValue(0) 
        self.spComboF.SetValue(0) 
        self.spPalomitasCh.SetValue(0) 
        self.spPalomitasMd.SetValue(0) 
        self.spPalomitasG.SetValue(0) 
        self.spCantidad.SetValue(0) 
        self.cmbSabor.SetSelection(wx.NOT_FOUND) 
        self.cmbTamano.SetSelection(wx.NOT_FOUND) 
        self.lbProductosAgregados.SetLabel("---") 
        self.lbSubtotal.SetLabel("$00.00")

    def limpiarDulceria(self, event):
        self.limpiarD()
        event.Skip


    def siguienteDulceria(self, event):  # wxGlade: Ventana3.<event_handler>
        pregunta = wx.MessageDialog(self,
            f"Confirmación de Dulcería.\n"
            f"¿Está seguro que desea adquirir?\n\n{self.infoDulceria}\n"
            f"Subtotal Dulceria: ${self.subtotalDulceria}",
            "Dulceria", style=wx.YES_NO | wx.ICON_QUESTION)
        
        respuesta = pregunta.ShowModal()
        pregunta.Destroy()  

        if respuesta == wx.ID_YES:
            v4 = Ventana4(self, informacion=self.infoTaquilla,
            subtotal1=self.subtotalTaquilla,
            informacion2=self.infoDulceria,
            subtotal2=self.subtotalTaquilla)
            v4.Show()
            self.limpiarD()
            self.Hide()
        elif respuesta == wx.ID_NO:
            self.limpiarD()
        event.Skip()

# end of class Ventana3

class Ventana2(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Ventana2.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((639, 748))
        self.SetTitle("Taquilla")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("E:\\ADATA\\CinePlusNaoRamirez3B\\cinemalogo.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_1.SetBackgroundColour(wx.Colour(0, 255, 0))

        grid_sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_2 = wx.GridSizer(1, 3, 0, 0)
        grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)

        bitmap_1 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\CinePlusNaoRamirez3B\\cinemalogo.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_2.Add(bitmap_1, 0, wx.ALIGN_CENTER, 0)

        lbTitulo = wx.StaticText(self.panel_1, wx.ID_ANY, "Taquilla", style=wx.ALIGN_CENTER_HORIZONTAL)
        lbTitulo.SetMinSize((50, 50))
        lbTitulo.SetForegroundColour(wx.Colour(243, 113, 243))
        lbTitulo.SetFont(wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_2.Add(lbTitulo, 0, wx.EXPAND, 0)

        bitmap_2 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\CinePlusNaoRamirez3B\\cinemalogo.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_2.Add(bitmap_2, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_4 = wx.GridSizer(1, 3, 0, 0)
        grid_sizer_1.Add(grid_sizer_4, 1, wx.EXPAND, 0)

        grid_sizer_5 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_4.Add(grid_sizer_5, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Pelicula:")
        grid_sizer_5.Add(label_1, 0, 0, 0)

        grid_sizer_6 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_4.Add(grid_sizer_6, 1, wx.EXPAND, 0)

        self.cmbPelicula = wx.ComboBox(self.panel_1, wx.ID_ANY, choices=["Intensa Mente2", "Sherk", "Spiderman"], style=wx.CB_DROPDOWN)
        grid_sizer_6.Add(self.cmbPelicula, 0, 0, 0)

        self.bmPelicula = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\nao1\\images.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_4.Add(self.bmPelicula, 0, 0, 0)

        grid_sizer_7 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_1.Add(grid_sizer_7, 1, wx.EXPAND, 0)

        grid_sizer_8 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_7.Add(grid_sizer_8, 1, wx.EXPAND, 0)

        grid_sizer_9 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_8.Add(grid_sizer_9, 1, wx.EXPAND, 0)

        grid_sizer_10 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_9.Add(grid_sizer_10, 1, wx.EXPAND, 0)

        grid_sizer_11 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_10.Add(grid_sizer_11, 1, wx.EXPAND, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Sala:")
        grid_sizer_11.Add(label_2, 0, 0, 0)

        self.lbSala = wx.StaticText(self.panel_1, wx.ID_ANY, "-------")
        grid_sizer_11.Add(self.lbSala, 0, 0, 0)

        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "Horario")
        grid_sizer_1.Add(label_3, 0, 0, 0)

        self.rbHorario1 = wx.RadioButton(self.panel_1, wx.ID_ANY, "00:00")
        grid_sizer_1.Add(self.rbHorario1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.rbHorario2 = wx.RadioButton(self.panel_1, wx.ID_ANY, "00:00")
        grid_sizer_1.Add(self.rbHorario2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.rbHorario3 = wx.RadioButton(self.panel_1, wx.ID_ANY, "00:00")
        grid_sizer_1.Add(self.rbHorario3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "Boletos")
        label_4.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_1.Add(label_4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, "Adultos($80):")
        grid_sizer_1.Add(label_5, 0, 0, 0)

        self.tfAdultos = wx.TextCtrl(self.panel_1, wx.ID_ANY,style=wx.TE_PROCESS_ENTER)
        grid_sizer_1.Add(self.tfAdultos, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        label_6 = wx.StaticText(self.panel_1, wx.ID_ANY, "Menores($70):")
        grid_sizer_1.Add(label_6, 0, 0, 0)

        self.tfMenores = wx.TextCtrl(self.panel_1, wx.ID_ANY, style=wx.TE_PROCESS_ENTER)
        grid_sizer_1.Add(self.tfMenores, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.lbSubtotal = wx.StaticText(self.panel_1, wx.ID_ANY, "Subtotal:$")
        grid_sizer_1.Add(self.lbSubtotal, 0, 0, 0)

        self.btnLimpiar = wx.Button(self.panel_1, wx.ID_ANY, "Limpiar")
        grid_sizer_1.Add(self.btnLimpiar, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.btnSiguiente = wx.Button(self.panel_1, wx.ID_ANY, "Siguiente")
        grid_sizer_1.Add(self.btnSiguiente, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.panel_1.SetSizer(grid_sizer_1)

        self.Layout()

        self.cmbPelicula.Bind(wx.EVT_COMBOBOX, self.seleccionPelicula)
        self.rbHorario1.Bind(wx.EVT_RADIOBUTTON, self.seleccionHorario1)
        self.rbHorario2.Bind(wx.EVT_RADIOBUTTON, self.seleccionHorario2)
        self.rbHorario3.Bind(wx.EVT_RADIOBUTTON, self.seleccionHorario3)
        self.tfAdultos.Bind(wx.EVT_TEXT_ENTER, self.sumarAdultos)
        self.tfMenores.Bind(wx.EVT_TEXT_ENTER, self.sumarMenores)
        self.btnLimpiar.Bind(wx.EVT_BUTTON, self.limpiarTaquilla)
        self.btnSiguiente.Bind(wx.EVT_BUTTON, self.siguienteVentana)
        # end wxGlade

    def cargar_imagen(self,ruta):
        print(f"Ruta: {ruta}")
        bitmap = wx.Bitmap(ruta, wx.BITMAP_TYPE_ANY) 
        self.bmPelicula.SetBitmap(bitmap)

    def seleccionPelicula(self, event):  # wxGlade: Ventana2.<event_handler>
        pelicula=self.cmbPelicula.GetValue()
        imagen=""
        sala=""
        horario1=horario2=horario3=""

        print(f"Pelicula seleccionada: {pelicula}")

        if pelicula=="Intensa Mente2":
            imagen="peliculauna.png"
            sala="1"
            horario1="14:00"
            horario2="17:00"
            horario3="19:00"

        elif pelicula=="Sherk":
            imagen="imageee.png"
            sala="3"
            horario1="13:00"
            horario2="16:00"
            horario3="19:00"

        elif pelicula=="Spiderman":
            imagen="images.png"
            sala="2"
            horario1="15:00"
            horario2="18:00"
            horario3="21:00"

        self.cargar_imagen(imagen)
        self.lbSala.SetLabel(sala)
        self.rbHorario1.SetLabel(horario1)
        self.rbHorario2.SetLabel(horario2)
        self.rbHorario3.SetLabel(horario3)
        self.informacion=f"Pelicula: {pelicula}  \n  Sala: {sala}"
        print(f"Listo para disfruta de \n {self.informacion}")
        event.Skip()

    def seleccionHorario1(self, event):  # wxGlade: Ventana2.<event_handler>
        self.HorarioSeleccionado=self.rbHorario1.GetLabelText()
        event.Skip()

    def seleccionHorario2(self, event):  # wxGlade: Ventana2.<event_handler>
        self.HorarioSeleccionado=self.rbHorario2.GetLabelText()
        event.Skip()

    def seleccionHorario3(self, event):  # wxGlade: Ventana2.<event_handler>
        self.HorarioSeleccionado=self.rbHorario3.GetLabelText()
        event.Skip()

    def sumarAdultos(self, event):  # wxGlade: Ventana2.<event_handler>
        try:
            self.adultos= int(self.tfAdultos.GetValue())
            subtotal_a = self.adultos*80
            self.subtotal=subtotal_a
            self.lbSubtotal.SetLabel(f"Subtotal:${subtotal_a:.2f}")
        except ValueError:
            wx.MessageBox("Por favor ingrese un numero valido", "Error", wx.OK | wx.ICON_ERROR)
        event.Skip()

    def sumarMenores(self, event):  # wxGlade: Ventana2.<event_handler>
        try:
            self.menores=int(self.tfMenores.GetValue())
            subtotal_b=self.menores * 70
            self.subtotal=(self.adultos*80)+ subtotal_b
            self.lbSubtotal.SetLabel(f"Subtotal: ${self.subtotal:.2f}")
        except ValueError:
            wx.MessageBox("Por favor ingrese un numero valido", "Error", wx.OK | wx.ICON_ERROR)
        event.Skip()

    def limpiarValores_Campos(self):
        self.subtotal=0
        self.adultos=0
        self.menores=0
        self.informacion=""
        self.horarioSeleccionado=""

        self.cargar_imagen("logo.png")
        self.rbHorario1.SetLabel("00:00")
        self.rbHorario2.SetLabel("00:00")
        self.rbHorario3.SetLabel("00:00")
        self.rbHorario1.SetValue(False)
        self.rbHorario2.SetValue(False)
        self.rbHorario3.SetValue(False)
        self.cmbPelicula.SetSelection(wx.NOT_FOUND)
        self.lbSala.SetLabel("---")
        self.tfAdultos.SetValue("0")
        self.tfMenores.SetValue("0")
        self.lbSubtotal.SetLabel("0")




    def limpiarTaquilla(self, event):  # wxGlade: Ventana2.<event_handler>
        self.limpiarValores_Campos()
        event.Skip()

    def siguienteVentana(self, event):  # wxGlade: Ventana2.<event_handler>
        self.informacion=f"{self.informacion}\n Horario:{self.HorarioSeleccionado}"
        self.informacion=f"{self.informacion}\n Adultos:{self.adultos}\n Menores de 12 años:{self.menores}"
        self.informacion=f"{self.informacion}\n Subtotal:{self.subtotal}"

        pregunta=wx.MessageDialog(
        self,
        f"Confirmacion de Taquilla.\n"
        f"¿Esta seguro que desea adquirir?\n\n{self.informacion}",
        "Taquilla",
        style=wx.YES_NO | wx.ICON_QUESTION
        )
        respuesta=pregunta.ShowModal()
        pregunta.Destroy()

        if  respuesta == wx.ID_YES:
            print(f"Venta de Taquilla realizada\n {self.informacion}")
            v3 = Ventana3(self, informacion=self.informacion, subtotal=self.subtotal)
            v3.Show()
            self.limpiarValores_Campos()
            self.Hide()
        elif respuesta == wx.ID_NO:
            self.limpiarValores_Campos()
        event.Skip()

# end of class Ventana2

class Ventana1(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Ventana1.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 555))
        self.SetTitle("Inicio de sesion-Cine Plus")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("E:\\ADATA\\CinePlusNaoRamirez3B\\logotipo.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_1.SetBackgroundColour(wx.Colour(3, 3, 3))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        lbTitulo = wx.StaticText(self.panel_1, wx.ID_ANY, "Bienvenido( a )CinePlus", style=wx.ALIGN_CENTER_HORIZONTAL)
        lbTitulo.SetMinSize((132, 35))
        lbTitulo.SetForegroundColour(wx.Colour(255, 119, 255))
        lbTitulo.SetFont(wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        sizer_1.Add(lbTitulo, 0, wx.EXPAND, 0)

        lbLogo = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("E:\\ADATA\\CinePlusNaoRamirez3B\\logotipo.png", wx.BITMAP_TYPE_ANY))
        sizer_1.Add(lbLogo, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        lbUsuario = wx.StaticText(self.panel_1, wx.ID_ANY, "Usuario:", style=wx.ALIGN_CENTER_HORIZONTAL)
        lbUsuario.SetMinSize((445, 20))
        lbUsuario.SetForegroundColour(wx.Colour(255, 255, 255))
        sizer_1.Add(lbUsuario, 0, 0, 0)

        self.tfUsuario = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.tfUsuario.SetMinSize((200, 27))
        self.tfUsuario.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Arial"))
        sizer_1.Add(self.tfUsuario, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        lbClave = wx.StaticText(self.panel_1, wx.ID_ANY, u"Contraseña:", style=wx.ALIGN_CENTER_HORIZONTAL)
        lbClave.SetMinSize((200, 27))
        lbClave.SetForegroundColour(wx.Colour(255, 255, 255))
        sizer_1.Add(lbClave, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.tfClave = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        self.tfClave.SetMinSize((200, 27))
        sizer_1.Add(self.tfClave, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.btnSalir = wx.Button(self.panel_1, wx.ID_ANY, "Salir")
        sizer_1.Add(self.btnSalir, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.btnEntrar = wx.Button(self.panel_1, wx.ID_ANY, "Entrar")
        sizer_1.Add(self.btnEntrar, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 4)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.btnSalir.Bind(wx.EVT_BUTTON, self.cerrar_programa)
        self.btnEntrar.Bind(wx.EVT_BUTTON, self.confirmar_usuario_clave)
        # end wxGlade

    def cerrar_programa(self, event):  # wxGlade: Ventana1.<event_handler>
        pregunta = wx.MessageDialog(self, "Se cerrara la ventana.\n ¿Esta seguro que desea salir?", "Confirmar salida",style=wx.YES_NO | wx.ICON_QUESTION)
        
        respuesta=pregunta.ShowModal()
        pregunta.Destroy()

        if respuesta == wx.ID_YES:
            print("Bye")
            self.Close()  
        event.Skip()

    def confirmar_usuario_clave(self, event):  # wxGlade: Ventana1.<event_handler>
        nombre =self.tfUsuario.GetValue()
        clave =self.tfClave.GetValue()

        if nombre == "Nao" and clave == "123":
            print(f"Bienvenida, {nombre}! Acceso autorizado.")
            v2=Ventana2(self)
            v2.Show()
            self.Hide()
            
        else:
            print("Acceso denegado. Usuario o clave incorrectos.")
        event.Skip()

# end of class Ventana1

class MyAppCinePlus(wx.App):
    def OnInit(self):
        self.frame = Ventana1(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyAppCinePlus

if __name__ == "__main__":
    appCinePlus = MyAppCinePlus(0)
    appCinePlus.MainLoop()
