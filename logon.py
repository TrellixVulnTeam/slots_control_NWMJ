import wx
import psycopg2


class MyApp( wx.App ):




    def __init__(self, parent=None, id=-1):
        wx.App.__init__( self )
        frame = wx.Frame( parent=None, title='LOGIN', size=(320, 240) )

        panel = wx.Panel( frame, -1 )

        # 添加静态标签
        label_user = wx.StaticText( panel, -1, "USER ID:", pos=(40, 40) )
        label_pass = wx.StaticText( panel, -1, "PASSWORD:", pos=(40, 80) )
        # 添加文本输入框
        self.entry_user = wx.TextCtrl( panel, -1, size=(150, 30), pos=(130, 40) )
        # style 为设置输入
        self.entry_pass = wx.TextCtrl( panel, -1, size=(150, 30), pos=(130, 80), style=wx.TE_PASSWORD )
        # 添加按钮
        self.but_login = wx.Button( panel, -1, "LOGIN", size=(120, 30), pos=(30, 130) )
        self.but_cancel = wx.Button( panel, -1, "CANCEL", size=(120, 30), pos=(160, 130) )
        self.but_login.SetDefault()
        # 设置按钮的颜色
        # self.but_login.SetBackgroundColour("#0a74f7")
        # self.but_register.SetBackgroundColour("#282c34")
        # 给按钮绑定事件
        self.Bind( wx.EVT_BUTTON, self.on_but_login, self.but_login )
        self.Bind( wx.EVT_BUTTON, self.on_but_cancel, self.but_cancel )
        #
        frame.Center()
        #frame.Show( True )

    def show_message(self, word=""):
        dlg = wx.MessageDialog( None, word, u"错误", wx.OK | wx.ICON_QUESTION )

        if dlg.ShowModal() == wx.ID_OK:
            # self.Close(True)
            pass
        dlg.Destroy()


    def on_but_login(self, event):
        # 连接到本地数据库

        user_name = self.entry_user.GetValue()
        pass_word = self.entry_pass.GetValue()

        # 判断，查看用户名和密码名是否为空
        # 不为空之后在进行查询和判断
        # 不然当密码或用户名为空时会出现会导致出错
        if user_name and pass_word:
            try:
                con = psycopg2.connect( host="localhost",
                                        user=user_name,
                                        password=pass_word,
                                        database="postgres",
                                        port='5432' )
            except psycopg2.OperationalError as e:
                self.show_message( word='登录错误' )
                con = None
        else:
            self.show_message( word='用户名、密码不能为空' )

    def on_but_cancel(self, event):
        self.ExitMainLoop()




if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
