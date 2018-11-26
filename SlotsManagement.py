import wx
from ui.DailyReportForm import *


class SpaceManagement(wx.App):
    def OnInit(self):
        self.frame=DailyReport()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
def main():
    app=SpaceManagement()

    app.MainLoop()

if __name__=='__main__':
    main()