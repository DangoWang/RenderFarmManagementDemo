# coding: utf-8
import functools
import os
from dayu_widgets.badge import MBadge
from dayu_widgets.label import MLabel
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from dayu_widgets.message import MMessage
from dayu_widgets.qt import QWidget, QVBoxLayout, QStackedWidget, QFormLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from dayu_widgets.tool_button import MToolButton
from dayu_widgets import dayu_theme
from dayu_widgets.divider import MDivider
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.spin_box import MSpinBox, MDoubleSpinBox
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.radio_button import MRadioButton
from dayu_widgets.line_edit import MLineEdit


class BasicSettingWidget(QWidget):
    def __init__(self, parent=None):
        super(BasicSettingWidget, self).__init__(parent)
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        lan_setting_lay = QFormLayout()
        language_list_widget = QWidget()
        language_list_layout = QHBoxLayout()
        language_list_layout.addWidget(MRadioButton(u'中文'))
        language_list_layout.addWidget(MRadioButton('English'))
        language_list_layout.addWidget(MRadioButton('日本语'))
        language_list_widget.setLayout(language_list_layout)
        language_list_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        lan_setting_lay.addRow(u'语言设置：', language_list_widget)
        main_layout.addLayout(lan_setting_lay)

        main_layout.addWidget(MDivider())

        setting_2_layout = QFormLayout()
        setting_2_layout.addRow('开机启动:', MCheckBox('开机自动启动'))
        setting_2_layout.addRow('登陆设置:', MCheckBox('自动登录'))
        setting_2_layout.addRow('更新设置:', MCheckBox('自动检查更新'))
        main_layout.addLayout(setting_2_layout)

        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))


class NetWorkSetting(QWidget):
    def __init__(self, parent=None):
        super(NetWorkSetting, self).__init__(parent)
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        download_path_layout = QFormLayout()
        download_path_layout.addRow('默认下载路径:', MLineEdit().folder().small())
        download_path_layout.addRow('', MCheckBox('开启自动下载'))
        main_layout.addLayout(download_path_layout)

        main_layout.addWidget(MDivider())

        speed_limit_layout = QHBoxLayout()
        speed_limit_layout.addWidget(MLabel('速度限制：'))
        speed_limit_layout.addWidget(MLabel('上传限速：'))
        speed_limit_layout.addWidget(MDoubleSpinBox())
        speed_limit_layout.addWidget(MLabel('Mbps'))
        speed_limit_layout.addWidget(MLabel('下载限速：'))
        speed_limit_layout.addWidget(MDoubleSpinBox())
        speed_limit_layout.addWidget(MLabel('Mbps'))
        speed_limit_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(speed_limit_layout)

        main_layout.addWidget(MDivider())

        para_counts_layout = QHBoxLayout()
        para_counts_layout.addWidget(MLabel('并行设置：'))
        para_counts_layout.addWidget(MLabel('上传并行：'))
        para_counts_layout.addWidget(MSpinBox())
        para_counts_layout.addWidget(MLabel('下载并行：'))
        para_counts_layout.addWidget(MSpinBox())
        para_counts_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(para_counts_layout)
        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))


class RenderSettingWidget(QWidget):
    def __init__(self, parent=None):
        super(RenderSettingWidget, self).__init__(parent)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        render_test_lay = QHBoxLayout()
        render_test_lay.addWidget(MLabel('测试帧：'))
        render_test_lay.addWidget(MCheckBox('首帧'))
        render_test_lay.addWidget(MCheckBox('中间帧'))
        render_test_lay.addWidget(MCheckBox('末帧'))
        render_test_lay.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(render_test_lay)

        main_layout.addWidget(MDivider())

        layer_render_lay = QHBoxLayout()
        layer_render_lay.addWidget(MCheckBox('【仅maya生效】每层一个任务'))
        layer_render_lay.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(main_layout)

        main_layout.addWidget(MDivider())

        auto_upload_lay = QHBoxLayout()
        auto_upload_lay.addWidget(MLabel('自动提交:'))
        auto_upload_lay.addWidget(MCheckBox('若结果正常则自动提交任务'))
        auto_upload_lay.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(auto_upload_lay)

        main_layout.addWidget(MDivider())

        multi_frames_lay = QHBoxLayout()
        multi_frames_lay.addWidget(MLabel('一机多帧:'))
        multi_frames_lay.addWidget(MSpinBox())
        multi_frames_lay.addWidget(MLabel('单帧超时停止:'))
        multi_frames_lay.addWidget(MSpinBox())
        multi_frames_lay.addWidget(MLabel('小时'))
        multi_frames_lay.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(multi_frames_lay)

        # main_layout.addWidget(MDivider())
        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))


class SoftWarePath(QWidget):
    def __init__(self, parent=None):
        super(SoftWarePath, self).__init__(parent)
        main_layout = QVBoxLayout()
        maya_layout = QHBoxLayout()
        maya_layout.addWidget(MLabel('MayaBath路径：'))
        maya_layout.addWidget(MLineEdit(r"C:\Program Files\Autodesk\Maya2020\bin\mayabatch.exe").file())
        maya_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(maya_layout)

        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(main_layout)





class SettingsStackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        super(SettingsStackedWidget, self).__init__(parent)
        self.addWidget(BasicSettingWidget())
        self.addWidget(NetWorkSetting())
        self.addWidget(RenderSettingWidget())
        self.addWidget(SoftWarePath())


class GlobalSettingsWin(QWidget):
    def __init__(self, parent=None):
        super(GlobalSettingsWin, self).__init__(parent)
        self.setWindowTitle('Examples for MMenuTabWidget')
        self._init_ui()

    def _init_ui(self):
        item_list = [
            {'text': '基本设置', 'svg': f'{os.environ["ROOTPATH"]}/icons/custom/basic_setting.svg',
             'clicked': functools.partial(self.set_central_widget, 0)},
            {'text': u'传输设置', 'svg': f'{os.environ["ROOTPATH"]}/icons/custom/network_setting.svg',
             'clicked': functools.partial(self.set_central_widget, 1)},
            {'text': u'渲染设置', 'svg': f'{os.environ["ROOTPATH"]}/icons/custom/render_setting.svg',
             'clicked': functools.partial(self.set_central_widget, 2)},
            {'text': u'软件路径', 'svg': f'{os.environ["ROOTPATH"]}/icons/custom/software_path_setting.svg',
             'clicked': functools.partial(self.set_central_widget, 3)},
        ]
        tool_bar = MMenuTabWidget()
        self.content_widget = SettingsStackedWidget()
        for index, data_dict in enumerate(item_list):
            tool_bar.add_menu(data_dict, index)
        tool_bar.tool_button_group.set_dayu_checked(0)

        main_lay = QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.addWidget(tool_bar)
        main_lay.addWidget(self.content_widget)

        self.setLayout(main_lay)
        dayu_theme.apply(self)
        self.setStyleSheet(self.styleSheet().replace('494949', '2c313c').replace('3a3a3a', '444c5d').replace('323232', '2c313c'))

    def set_central_widget(self, widget_index):
        self.content_widget.setCurrentIndex(widget_index)
        pass


if __name__ == '__main__':
    import sys
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = GlobalSettingsWin()
    dayu_theme.apply(test)

    test.show()
    sys.exit(app.exec_())
