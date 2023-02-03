# -*- coding: utf-8 -*-
import os
from dayu_widgets.divider import MDivider
from dayu_widgets.label import MLabel
from dayu_widgets import dayu_theme
from dayu_widgets.line_tab_widget import MLineTabWidget
from dayu_widgets.qt import QWidget, QVBoxLayout, Qt, QHBoxLayout, QSpacerItem, QSizePolicy, QMenu, QCursor, MIcon
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.item_model import MTableModel, MSortFilterModel
from dayu_widgets.item_view import MTreeView
from dayu_widgets.push_button import MPushButton
from dayu_widgets.message import MMessage
from . import _test_data as mock


class TreeView(MTreeView):
    def __init__(self, parent=None):
        super(TreeView, self).__init__(parent)
        self.data_model = MTableModel()
        self.data_model.set_header_list(mock.header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(self.data_model)

        self.setModel(model_sort)

        model_sort.set_header_list(mock.header_list)
        self.set_header_list(mock.header_list)
        # self.model.set_data_list(mock.tree_data_list)

        self.setStyleSheet("border:none;")


class TeamAssetWin(QWidget):
    def __init__(self, parent=None):
        super(TeamAssetWin, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_layout = QVBoxLayout()
        toolbutton_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        toolbutton_layout.setContentsMargins(0, 0, 0, 0)

        self.upload_tool_button = MToolButton()
        self.upload_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/upload.svg')
        toolbutton_layout.addWidget(self.upload_tool_button)

        self.new_folder_tool_button = MToolButton()
        self.new_folder_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/new_folder.svg')
        toolbutton_layout.addWidget(self.new_folder_tool_button)

        self.download_tool_button = MToolButton()
        self.download_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/download.svg')
        toolbutton_layout.addWidget(self.download_tool_button)

        self.move_tool_button = MToolButton()
        self.move_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/move.svg')
        toolbutton_layout.addWidget(self.move_tool_button)

        self.copy_tool_button = MToolButton()
        self.copy_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/copy.svg')
        toolbutton_layout.addWidget(self.copy_tool_button)

        self.rename_tool_button = MToolButton()
        self.rename_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/rename.svg')
        toolbutton_layout.addWidget(self.rename_tool_button)

        self.delete_tool_button = MToolButton()
        self.delete_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/delete.svg')
        toolbutton_layout.addWidget(self.delete_tool_button)

        toolbutton_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.search_line_edit = MLineEdit().search().small()
        self.search_line_edit.setMaximumWidth(300)
        self.search_line_edit.setStyleSheet('border: 1px solid #1e1e1e;background-color: #313641;')
        toolbutton_layout.addWidget(self.search_line_edit)

        main_layout.addLayout(toolbutton_layout)

        self.tv = TreeView()
        self.tv.data_model.set_data_list(mock.tree_data_list)
        # self.tv.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.tv.customContextMenuRequested.connect(self.show_menu)
        # self.tv.contextMenu = QMenu(self)

        main_layout.addWidget(self.tv)
        self.setLayout(main_layout)

    # def show_menu(self):
    #     self.tv.contextMenu.clear()
    #     self.tv.contextMenu.addAction(MIcon(f'{os.environ["ROOTPATH"]}/icons/custom/analysis.png',
    #                                           dayu_theme.primary_color), '分析文件')
    #     self.tv.contextMenu.popup(QCursor.pos())
    #     self.tv.contextMenu.show()
    #     pass

    def upload(self):
        # todo
        MMessage.config(3)
        MMessage.error(self, u'功能咱不可用，敬请期待！')

    def create_dir(self):
        # todo
        MMessage.error(self, u'功能咱不可用，敬请期待！')



class RenderOutput(QWidget):
    def __init__(self, parent=None):
        super(RenderOutput, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_layout = QVBoxLayout()
        toolbutton_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        toolbutton_layout.setContentsMargins(0, 0, 0, 0)

        self.download_tool_button = MToolButton()
        self.download_tool_button.set_dayu_svg(f'{os.environ["ROOTPATH"]}/icons/custom/download.svg')
        toolbutton_layout.addWidget(self.download_tool_button)

        toolbutton_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.search_line_edit = MLineEdit().search().small()
        self.search_line_edit.setMaximumWidth(300)
        toolbutton_layout.addWidget(self.search_line_edit)

        main_layout.addLayout(toolbutton_layout)
        render_output = TreeView()
        render_output.data_model.set_data_list(mock.tree_data_list_2)
        main_layout.addWidget(render_output)
        self.setLayout(main_layout)


class AssetManageWin(QWidget):
    def __init__(self, parent=None):
        super(AssetManageWin, self).__init__(parent)
        self._init_ui()
        dayu_theme.apply(self)
        self.setStyleSheet(self.styleSheet().replace('3a3a3a', '2c313c').replace('323232', '2c313c').replace('494949', '2c313c'))
        self.setStyleSheet(self.styleSheet()+'\nMTreeView::item:selected, \nMTreeView::item:hover{background-color: #3c414d;}')

    def _init_ui(self):
        main_lay = QVBoxLayout()

        tab_center = MLineTabWidget()

        tab_center.add_tab(TeamAssetWin(),
                           {'text': u'团队资产', 'svg': f'{os.environ["ROOTPATH"]}/icons/custom/team.svg'})

        # tab_center.add_tab(RenderOutput(),
        #                    {'text': u'渲染输出', 'svg': f'{os.environ["ROOTPATH"]}/icons/custom/render_output.svg'})
        tab_center.tool_button_group.set_dayu_checked(0)

        main_lay.addWidget(tab_center)
        main_lay.addSpacing(20)
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    from dayu_widgets import dayu_theme

    app = QApplication(sys.argv)
    test = AssetManageWin()

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
