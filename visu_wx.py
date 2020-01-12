"""
Hello World, but with more meat.
"""

import wx
import wx.grid as gridlib

class npuzzle(wx.Frame):

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(npuzzle, self).__init__(*args, **kw)

#Panel
        panel = wx.Panel(self)
        panel.SetAutoLayout(True)
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panel_sizer = wx.BoxSizer( wx.VERTICAL )
        
#Grid
        grid = gridlib.Grid(panel)
        grid.CreateGrid(4,4)
        grid.SetRowLabelSize(0)
        grid.SetColLabelSize(0)
        sizer = wx.FlexGridSizer(4,4,0,0)
        sizer.Add(grid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)
#Columns

#Rows

#Label appearance

        

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = npuzzle(None, title='N-Puzzle')
    frm.Show()
    app.MainLoop()