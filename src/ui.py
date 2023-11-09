import wx
import wx.grid


class App:
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
        super(Layout, self).__init__(parent, title=title, size=(300, 200))
        self.tables = tables
        self.app = app
        self.save = None
        self.checkBoxes = []

        self.init_ui()
        self.Centre()
        self.Show()

    def init_ui(self):
        p_out = wx.Panel(self)

        gs_out = wx.GridSizer(2, 1, 5, 5)

        gs_in = wx.GridSizer(len(self.tables) + 1, 2, 5, 5)

        p_in = wx.Panel(p_out)

        gs_in.Add(wx.StaticText(p_in, label="Kiválasztva"), 2, wx.EXPAND)
        gs_in.Add(wx.StaticText(p_in, label="Tábla név"), 2, wx.EXPAND)
        for table in self.tables:
            cb = wx.CheckBox(p_in)

            self.checkBoxes.append((cb, table))

            gs_in.Add(cb, 0)
            gs_in.Add(wx.StaticText(p_in, label=table), 2, wx.EXPAND)

        p_in.SetSizer(gs_in)
        gs_out.Add(p_in, 0, wx.EXPAND)

        self.save = wx.Button(p_out, label="Save")
        self.save.Bind(wx.EVT_BUTTON, self.on_clicked)

        gs_out.Add(self.save, 0, wx.EXPAND)
        p_out.SetSizer(gs_out)

    def on_clicked(self, event):
        ret = []
        for (cb, table) in self.checkBoxes:
            if cb.GetValue():
                ret.append(table)

        self.app.quit(ret)


class GridFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        # Create a wxGrid object
        grid = wx.grid.Grid(self, -1)

        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(20, 10)

        # We can set the sizes of individual rows and columns
        # in pixels
        grid.SetRowSize(0, 60)
        grid.SetColSize(0, 120)

        # And set grid cell contents as strings
        grid.SetCellValue(0, 0, 'wxGrid is good')

        # We can specify that some cells are read.only
        grid.SetCellValue(0, 3, 'This is read.only')
        grid.SetReadOnly(0, 3)

        # Colours can be specified for grid cell contents
        grid.SetCellValue(3, 3, 'green on grey')
        grid.SetCellTextColour(3, 3, wx.GREEN)
        grid.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)

        # We can specify the some cells will store numeric
        # values rather than strings. Here we set grid column 5
        # to hold floating point values displayed with width of 6
        # and precision of 2
        grid.SetColFormatFloat(5, 6, 2)
        grid.SetCellValue(0, 6, '3.1415')

        self.Show()
