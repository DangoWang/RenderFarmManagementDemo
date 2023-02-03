#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import _test_data as mock
import os
from dayu_widgets import dayu_theme
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.item_model import MTableModel, MSortFilterModel
from dayu_widgets.item_view import MTableView
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.text_edit import MTextEdit
from dayu_widgets.divider import MDivider
from dayu_widgets.drawer import MDrawer
from dayu_widgets.label import MLabel
from dayu_widgets.line_tab_widget import MLineTabWidget
from dayu_widgets.qt import *


class RenderTableView(MTableView):
    def __init__(self, size=dayu_theme.large, show_row_count=False, parent=None):
        super(RenderTableView, self).__init__(size=size, show_row_count=show_row_count, parent=parent)
        model_1 = MTableModel()
        model_1.set_header_list(mock.render_tasks_header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)

        # table_large = MTableView(size=dayu_theme.large, show_row_count=False)

        self.setModel(model_sort)
        model_sort.set_header_list(mock.render_tasks_header_list)
        self.set_header_list(mock.render_tasks_header_list)
        model_1.set_data_list(mock.render_tasks_data_list)


class JobDetailTableView(MTableView):
    def __init__(self, size=dayu_theme.large, show_row_count=False, parent=None):
        super(JobDetailTableView, self).__init__(size=size, show_row_count=show_row_count, parent=parent)
        model_1 = MTableModel()
        model_1.set_header_list(mock.job_detail_header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)

        # table_large = MTableView(size=dayu_theme.large, show_row_count=False)

        self.setModel(model_sort)
        model_sort.set_header_list(mock.job_detail_header_list)
        self.set_header_list(mock.job_detail_header_list)
        model_1.set_data_list(mock.job_detail_data_list)


class RenderTaskDrawer(MDrawer):

    def __init__(self, title='', parent=None):
        super(RenderTaskDrawer, self).__init__(title=title, parent=parent)

        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        task_info_layout = QHBoxLayout()
        #  作业详情块
        task_info_widget = QWidget()
        task_info_widget.setStyleSheet('background-color:#394051')
        task_info_lay = QVBoxLayout()
        task_info_widget.setLayout(task_info_lay)
        task_info_bar_layout = QHBoxLayout()
        task_info_bar_layout.addWidget(MLabel(u'example.ma').h4())
        task_info_bar_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        status_label = MLabel(u'已完成').secondary()
        status_label.setStyleSheet('color:rgb(50, 255, 0);')
        task_info_bar_layout.addWidget(status_label)
        task_info_lay.addLayout(task_info_bar_layout)
        task_info_data_layout = QFormLayout()
        task_info_data_layout.addRow('作业ID', MLabel('2W546548'))
        task_info_data_layout.addRow('提交时间', MLabel('2021-5-19 14:56:12'))
        task_info_data_layout.addRow('软件配置', MLabel('Maya 2020'))
        task_info_data_layout.addRow('相机', MLabel('test_cam'))
        task_info_data_layout.addRow('分辨率', MLabel('512*512'))
        task_info_data_layout.addRow('渲染帧', MLabel('1-100[1]'))
        task_info_data_layout.addRow('一机多帧', MLabel('1'))
        task_info_lay.addLayout(task_info_data_layout)
        #  任务预览图块
        task_thumb = QWidget()
        task_thumb_lay = QHBoxLayout()
        task_thumb_lay.setContentsMargins(0, 0, 0, 0)
        task_thumb.setLayout(task_thumb_lay)
        task_thumb.setStyleSheet('background-color:#394051')
        left_button_lay = QVBoxLayout()
        left_button_lay.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        left_button_lay.addWidget(MToolButton().svg(f'{os.environ["ROOTPATH"]}/icons/custom/to_left.svg'))
        left_button_lay.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        task_thumb_lay.addLayout(left_button_lay)
        thumb_middle_layout = QVBoxLayout()
        thumb_middle_down_layout = QHBoxLayout()
        thumb_middle_down_layout.addWidget(MLabel('第3帧'))
        thumb_middle_down_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        thumb_middle_down_layout.addWidget(MLabel('用时：3分10秒'))
        thumb_middle_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        thumb_label = MLabel()
        pm = QPixmap(f'{os.environ["ROOTPATH"]}/images/render_img_demo.jpg').scaledToWidth(self.parent().width()/4)
        thumb_label.setPixmap(pm)
        thumb_middle_layout.addWidget(thumb_label)
        thumb_middle_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        thumb_middle_layout.addLayout(thumb_middle_down_layout)
        task_thumb_lay.addLayout(thumb_middle_layout)
        right_button_lay = QVBoxLayout()
        right_button_lay.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        right_button_lay.addWidget(MToolButton().svg(f'{os.environ["ROOTPATH"]}/icons/custom/to_right.svg'))
        right_button_lay.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        task_thumb_lay.addLayout(right_button_lay)
        task_info_layout.addWidget(task_info_widget)
        task_info_layout.addWidget(task_thumb)
        main_layout.addLayout(task_info_layout)

        #  任务详情页面
        line_tab_widget = MLineTabWidget(alignment=Qt.AlignLeft)
        line_tab_widget.setStyleSheet('background-color:#394051;')
        line_tab_widget.setMinimumHeight(self.parent().height())
        job_detail_widget = QWidget()
        job_detail_widget_lay = QVBoxLayout()
        job_detail_widget_lay.setContentsMargins(0, 0, 0, 0)
        job_detail_widget.setLayout(job_detail_widget_lay)
            #  上面的部分
        job_detail_top_lay = QHBoxLayout()
        job_detail_top_lay.addWidget(MLabel('实际扣费： C0.55 总时长： 8分16秒 平均任务耗时： 49秒\n已完成 10帧 渲染中 0帧 失败 0帧 停止 0帧'))
        job_detail_top_lay.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        search_widget = MLineEdit().search()
        search_widget.setStyleSheet('border: 1px solid #1e1e1e;')
        job_detail_top_lay.addWidget(search_widget)
        job_detail_top_lay.setContentsMargins(0, 0, 0, 0)
        job_detail_widget_lay.addLayout(job_detail_top_lay)
            #  下面的表格
        job_detail_table_view = JobDetailTableView()
        job_detail_widget_lay.addWidget(job_detail_table_view)
        line_tab_widget.add_tab(job_detail_widget, '任务详情')
        main_layout.addWidget(line_tab_widget)
        main_layout.addSpacing(20)

        self.setStyleSheet('border:none;background-color:#3c4455')
        self.set_widget(main_widget)


class RenderTasksWin(QWidget):
    def __init__(self, parent=None):
        super(RenderTasksWin, self).__init__(parent)
        self._init_ui()
        dayu_theme.apply(self)
        self.setStyleSheet(
            self.styleSheet().replace('3a3a3a', '2c313c').replace('323232', '2c313c').replace('494949', '2c313c'))
        self.setStyleSheet(
            self.styleSheet() +
            '\nMTableView::item:selected, \nMTableView::item:hover{background-color: #376ce4;}'
            '\nMTableView{border:none;}'
            '\nMTextEdit{border: 1px solid #1e1e1e;}')

    def _init_ui(self):
        main_lay = QVBoxLayout()
        toolbutton_layout = QHBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        toolbutton_layout.setContentsMargins(0, 0, 0, 0)

        self.rerender_tool_button = MToolButton()
        self.rerender_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/rerender.svg')
        toolbutton_layout.addWidget(self.rerender_tool_button)

        self.delete_tool_button = MToolButton()
        self.delete_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/delete.svg')
        toolbutton_layout.addWidget(self.delete_tool_button)

        self.stop_tool_button = MToolButton()
        self.stop_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/stop.svg')
        toolbutton_layout.addWidget(self.stop_tool_button)

        toolbutton_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.search_line_edit = MLineEdit().search().small()
        self.search_line_edit.setMaximumWidth(300)
        self.search_line_edit.setStyleSheet('border: 1px solid #1e1e1e;background-color: #313641;')
        toolbutton_layout.addWidget(self.search_line_edit)

        table_large = RenderTableView()
        table_large.doubleClicked.connect(self.show_drawer)
        main_lay.addLayout(toolbutton_layout)
        main_lay.addWidget(table_large)

        # main_lay.addStretch()
        self.setLayout(main_lay)

    def show_drawer(self):
        drawer = RenderTaskDrawer(title=u'作业详情', parent=self).right()
        drawer.setFixedWidth(self.width()/2)
        drawer.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = RenderTasksWin()
    test.show()
    sys.exit(app.exec_())
