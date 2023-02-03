# coding:utf-8
import os
from dayu_widgets.qt import *
from dayu_widgets.label import MLabel
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.divider import MDivider
from dayu_widgets import dayu_theme


class BubbleLabel(QWidget):

    BackgroundColor = QColor(44, 49, 60)
    BorderColor = QColor(64, 69, 80)

    def __init__(self, parent=None):
        super(BubbleLabel, self).__init__(parent=parent)
        self.pos_offset = [0, 0]
        # 设置无边框置顶
        self.setWindowFlags(
            Qt.Window | Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.X11BypassWindowManagerHint)
        # 设置最小宽度和高度
        self.setMinimumWidth(200)
        self.setMinimumHeight(300)
        # self.setMaximumSize(300, 300)

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        layout = QVBoxLayout(self)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        # 左上右下的边距（下方16是因为包括了三角形）
        layout.setContentsMargins(8, 8, 8, 16)
        username_layout = QHBoxLayout()
        username_layout.addWidget(MLabel('wangdonghao'))
        username_layout.addWidget(MToolButton().svg(f'{os.environ["ROOTPATH"]}/icons/custom/recharge.svg').huge())
        layout.addLayout(username_layout)
        layout.addWidget(MDivider())

        tb1 = MToolButton().svg(f'{os.environ["ROOTPATH"]}/icons/custom/money_left.svg').text_beside_icon().huge()
        tb2 = MToolButton().svg(f'{os.environ["ROOTPATH"]}/icons/custom/change_personal_info.svg').text_beside_icon().huge()
        tb3 = MToolButton().svg(f'{os.environ["ROOTPATH"]}/icons/custom/online_helper.svg').text_beside_icon().huge()
        tb4 = MToolButton().svg(f'{os.environ["ROOTPATH"]}/icons/custom/log_out.svg').text_beside_icon().huge()
        tb1.setText('余额')
        tb2.setText('修改资料')
        tb3.setText('在线客服')
        tb4.setText('切换账号')
        layout.addWidget(tb1)
        layout.addWidget(tb2)
        layout.addWidget(tb3)
        layout.addWidget(tb4)
        # layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # self.label = QLabel(self)
        # self.label.setGeometry(QRect(328, 240, 329, 27 * 4))
        # self.label.setWordWrap(True)
        # self.label.setAlignment(Qt.AlignTop)
        # layout.addWidget(self.label)
        # self.setText(text)
        # 获取屏幕高宽
        self._desktop = QApplication.instance().desktop()
        self.start_pos = [500, 500]
        self.end_pos = [500, 600]

    # def setText(self, text):
    #     self.label.setText(text)
    #
    # def text(self):
    #     return self.label.text()

    def stop(self):
        self.hide()
        self.animationGroup.stop()
        self.close()

    def show(self):
        super(BubbleLabel, self).show()
        # 窗口开始位置
        startPos = QPoint(*self.start_pos)
        endPos = QPoint(*self.end_pos)# * 3 - 5)
        self.move(startPos)
        # 初始化动画
        self.initAnimation(startPos, endPos)

    def initAnimation(self, startPos, endPos):
        # 透明度动画
        opacityAnimation = QPropertyAnimation(self, b"opacity")
        opacityAnimation.setStartValue(0.0)
        opacityAnimation.setEndValue(1.0)
        # 设置动画曲线
        opacityAnimation.setEasingCurve(QEasingCurve.OutQuad)
        opacityAnimation.setDuration(1000)  # 在4秒的时间内完成
        # 往上移动动画
        moveAnimation = QPropertyAnimation(self, b"pos")
        moveAnimation.setStartValue(startPos)
        moveAnimation.setEndValue(endPos)
        moveAnimation.setEasingCurve(QEasingCurve.OutQuad)
        moveAnimation.setDuration(200)  # 在5秒的时间内完成
        # 并行动画组（目的是让上面的两个动画同时进行）
        self.animationGroup = QParallelAnimationGroup(self)
        self.opacity_animation_group = QParallelAnimationGroup(self)
        # self.animationGroup.addAnimation(opacityAnimation)
        self.animationGroup.addAnimation(moveAnimation)
        self.opacity_animation_group.addAnimation(opacityAnimation)
        self.opacity_animation_group.finished.connect(self.close)  # 动画结束时关闭窗口
        # moveAnimation.start()
        self.animationGroup.start()
        self.q_time = QTimer()
        # self.q_time.timeout.connect(self.opacity_animation_group.start)
        self.q_time.timeout.connect(self.close)
        self.q_time.start(1000)
        # self.opacity_animation_group.start()

        dayu_theme.apply(self)
        self.setStyleSheet(self.styleSheet().replace('3a3a3a', '2c313c').replace('323232', '2c313c').replace('494949', '2c313c'))



    def paintEvent(self, event):
        super(BubbleLabel, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿

        rectPath = QPainterPath()  # 圆角矩形
        triPath = QPainterPath()

        height = self.height()  # 往上偏移8
        rectPath.addRoundedRect(QRectF(0, 20, self.width(), height-20), 5, 5)
        x = (self.width() / 2) - 10
        triPath.moveTo(x, 20)
        # 画三角形
        triPath.lineTo(x + 10, 0)
        triPath.lineTo(x + 20, 20)

        rectPath.addPath(triPath)  # 添加三角形到之前的矩形上

        # 边框画笔
        painter.setPen(QPen(self.BorderColor, 2, Qt.SolidLine,
                            Qt.RoundCap, Qt.RoundJoin))
        # 背景画刷
        painter.setBrush(self.BackgroundColor)
        # 绘制形状
        painter.drawPath(rectPath)
        # 三角形底边绘制一条线保证颜色与背景一样
        painter.setPen(QPen(self.BackgroundColor, 2,
                            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(x, 20, x + 20, 20)

    def windowOpacity(self):
        return super(BubbleLabel, self).windowOpacity()

    def enterEvent(self,event):
        self.q_time.stop()

    def leaveEvent(self, event):
        self.q_time.start(500)

    def setWindowOpacity(self, opacity):
        super(BubbleLabel, self).setWindowOpacity(opacity)
    # 由于opacity属性不在QWidget中需要重新定义一个
    opacity = Property(float, windowOpacity, setWindowOpacity)


if __name__ == '__main__':
    import sys
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import QApplication

    os.environ["ROOTPATH"] = 'D:/dango_repo/renderfarm_client'
    app = QApplication(sys.argv)
    test = BubbleLabel()
    dayu_theme.apply(test)

    test.show()
    sys.exit(app.exec_())
