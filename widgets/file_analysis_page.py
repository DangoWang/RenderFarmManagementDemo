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
from dayu_widgets.qt import *


class FileAnalysisTableView(MTableView):
    def __init__(self, size=dayu_theme.large, show_row_count=False, parent=None):
        super(FileAnalysisTableView, self).__init__(size=size, show_row_count=show_row_count, parent=parent)
        model_1 = MTableModel()
        model_1.set_header_list(mock.analysis_header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)

        # table_large = MTableView(size=dayu_theme.large, show_row_count=False)

        self.setModel(model_sort)
        model_sort.set_header_list(mock.analysis_header_list)
        self.set_header_list(mock.analysis_header_list)
        model_1.set_data_list(mock.analysis_data_list)


class FileAnalysisWin(QWidget):
    def __init__(self, parent=None):
        super(FileAnalysisWin, self).__init__(parent)
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

        self.reanalysis_tool_button = MToolButton()
        self.reanalysis_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/rerender.svg')
        toolbutton_layout.addWidget(self.reanalysis_tool_button)

        self.submit_tool_button = MToolButton()
        self.submit_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/submit_job.svg')
        toolbutton_layout.addWidget(self.submit_tool_button)

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

        text_edit = MTextEdit().autosize()
        text_edit.setReadOnly(True)
        text_edit.setText('开始分析example.ma\n'
                          '成功开启文件\n'
                          '发现了5个依赖文件：'
                          '\n   --C:/a.mb'
                          '\n   --C:/b.mb'
                          '\n   --C:/c.mb'
                          '\n   --C:/d.mb'
                          '\n   --C:/e.mb'
                          '\n发现贴图丢失：'
                          '\n   --D:/sourceimages/111.jpg'
                          '\n检查完成，发现1个警告。'
                          )

        table_large = FileAnalysisTableView()
        main_lay.addLayout(toolbutton_layout)

        splitter_1 = QSplitter(Qt.Vertical)
        splitter_1.addWidget(table_large)
        splitter_1.addWidget(text_edit)

        main_lay.addWidget(splitter_1)
        # main_lay.addWidget(text_edit)

        # main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = FileAnalysisWin()
    test.show()
    sys.exit(app.exec_())
