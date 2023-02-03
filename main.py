# coding:utf-8
import sys
import os
os.environ['ROOTPATH'] = os.path.realpath(sys._MEIPASS).replace('\\', '/') if hasattr(sys, "_MEIPASS") \
    else os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
sys.path.append(os.path.abspath(os.environ['ROOTPATH'] + '/thirdparty'))
import json
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
# GUI FILE
from app_modules import *
from widgets import asset_manage_page, file_analysis_page, render_tasks_page, global_settings_page, personal_info_widget
from thirdparty.dayu_widgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.root = os.environ['ROOTPATH']
        # print('System: ' + platform.system())
        # print('Version: ' +platform.release())

        UIFunctions.removeTitleBar(True)

        self.setWindowTitle(u'阿凡达渲染农场客户端')
        UIFunctions.labelTitle(self, '阿凡达渲染农场客户端')
        UIFunctions.labelDescription(self, '')

        startSize = QSize(1300, 900)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)

        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))

        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, u"资产管理", "btn_asset_mng", f"url({self.root}/icons/custom/asset.png)", True)
        UIFunctions.addNewMenu(self, u"文件分析", "btn_job_analysis", f"url({self.root}/icons/custom/analysis.png)", True)
        UIFunctions.addNewMenu(self, u"渲染任务", "btn_submit_job", f"url({self.root}/icons/custom/my_task.png)", True)
        UIFunctions.addNewMenu(self, "设置", "btn_global_settings", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)

        UIFunctions.selectStandardMenu(self, "btn_asset_mng")

        self.asset_mng_win = asset_manage_page.AssetManageWin()
        self.ui.stackedWidget.addWidget(self.asset_mng_win)

        self.file_analysis_win = file_analysis_page.FileAnalysisWin()
        self.ui.stackedWidget.addWidget(self.file_analysis_win)

        self.render_tasks_win = render_tasks_page.RenderTasksWin()
        self.ui.stackedWidget.addWidget(self.render_tasks_win)

        self.global_settings_win = global_settings_page.GlobalSettingsWin(self)
        self.ui.stackedWidget.addWidget(self.global_settings_win)

        self.ui.account_toolbutton.clicked.connect(self.show_account_info)

        UIFunctions.userIcon(self, "团队", "", True)


        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.show()

    def show_account_info(self):
        tb_pos = [self.ui.account_toolbutton.pos().x() + self.pos().x(),
                  self.ui.account_toolbutton.pos().y() + self.pos().y()
                  ]
        personal_widget = personal_info_widget.BubbleLabel(self.ui.account_toolbutton)
        personal_widget.start_pos = [tb_pos[0], tb_pos[1]+50]
        personal_widget.end_pos = [tb_pos[0], tb_pos[1]+70]
        personal_widget.show()

    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_asset_mng":
            self.ui.stackedWidget.setCurrentWidget(self.asset_mng_win)
            UIFunctions.resetStyle(self, "btn_asset_mng")
            # UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_job_analysis":
            self.ui.stackedWidget.setCurrentWidget(self.file_analysis_win)
            UIFunctions.resetStyle(self, "btn_job_analysis")
            # UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_submit_job":
            self.ui.stackedWidget.setCurrentWidget(self.render_tasks_win)
            UIFunctions.resetStyle(self, "btn_submit_job")
            # UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_global_settings":
            self.ui.stackedWidget.setCurrentWidget(self.global_settings_win)
            UIFunctions.resetStyle(self, "btn_global_settings")
            # UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    #     if event.buttons() == Qt.LeftButton:
    #         print('Mouse click: LEFT CLICK')
    #     if event.buttons() == Qt.RightButton:
    #         print('Mouse click: RIGHT CLICK')
    #     if event.buttons() == Qt.MidButton:
    #         print('Mouse click: MIDDLE BUTTON')

    # def keyPressEvent(self, event):
    #     print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))

    # def resizeEvent(self, event):
    #     self.resizeFunction()
    #     return super(MainWindow, self).resizeEvent(event)

    # def resizeFunction(self):
    #     print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('../aaa_from_other/Simple_PySide_Base/fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('../aaa_from_other/Simple_PySide_Base/fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
