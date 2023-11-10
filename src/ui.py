import wx
import wx.lib.scrolledpanel as scrolled


def err(message):
    app = wx.App(0)
    resp = wx.MessageBox(message, 'Error',
                         wx.OK | wx.ICON_WARNING)


class App:
    def __init__(self):
        self.app = None
        self.ret = None

    def select_tables(self, tables):
        app = wx.App(0)
        self.app = app
        self.ret = None
        # frame = GridFrame(None)
        frame = Layout(None, "Mysql Export", tables, self)

        app.MainLoop()
        return self.ret

    def quit(self, tables):
        self.ret = tables
        self.app.ExitMainLoop()


class Layout(wx.Frame):

    def __init__(self, parent, title, tables, app):
        super(Layout, self).__init__(parent, title=title, size=(500, 300))
        self.tables = tables
        self.app = app
        self.save = None
        self.checkBoxes = []

        self.init_ui()
        self.Centre()
        self.Show()

    def init_ui(self):
        p_out = wx.Panel(self)

        vert = wx.BoxSizer(wx.VERTICAL)

        gs = wx.GridBagSizer(5, 5)
        gs.SetRows(len(self.tables) + 1)
        gs.SetCols(2)

        p_in = scrolled.ScrolledPanel(p_out, -1, style=wx.EXPAND)
        p_in.SetAutoLayout(1)
        p_in.SetupScrolling(False, True)

        gs.Add(wx.StaticText(p_in, label="Export"), pos=(0, 0))
        gs.Add(wx.StaticText(p_in, label="Table"), pos=(0, 1))
        for ix, table in enumerate(self.tables):
            cb = wx.CheckBox(p_in)
            self.checkBoxes.append((cb, table))
            gs.Add(cb, pos=(ix + 1, 0), flag=wx.ALIGN_CENTER)

            gs.Add(wx.StaticText(p_in, label=table), pos=(ix + 1, 1))

        p_in.SetSizer(gs)
        vert.Add(p_in, 1, wx.EXPAND, ).SetMinSize(500, 270)

        self.save = wx.Button(p_out, label="Save")
        self.save.Bind(wx.EVT_BUTTON, self.on_clicked)
        vert.Add(self.save, 0, wx.EXPAND)
        p_out.SetSizer(vert)

    def on_clicked(self, event):
        ret = []
        for (cb, table) in self.checkBoxes:
            if cb.GetValue():
                ret.append(table)

        self.app.quit(ret)
