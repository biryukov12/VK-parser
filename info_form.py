# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_info_form(object):
    def setupUi(self, info_form):
        info_form.setObjectName("info_form")
        info_form.resize(600, 380)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        info_form.setFont(font)
        info_form.setStyleSheet(" QPushButton\n"
"{\n"
"border-radius: 2px;\n"
"background: #c87243;\n"
"color: #fafbfc;\n"
"font: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"border-radius: 2px;\n"
"background: #b35d2e;\n"
"color: #fafbfc;\n"
"font: bold;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"border-radius: 2px;\n"
"background: #bc683a;\n"
"color: #fafbfc;\n"
"font: bold;\n"
"}\n"
"\n"
"*\n"
"{\n"
"background: #182635;\n"
"color: #fafbfc;\n"
"selection-color: #182635;\n"
"selection-background-color: #fafbfc;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"color: #fafbfc;\n"
"}\n"
"\n"
"QComboBox {\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 2em;\n"
"}\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 15px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"image: url(D:/YandexDisk/4 курс/Диплом/Main/icons/DropDownArrow.png);\n"
"width: 10px;\n"
"height: 10px;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"padding-top: 1px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* сдвиг стрелки когда выпадающий список раскрывается */\n"
"top: 1px;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"background-color: #182635;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"selection-background-color: #fafbfc;\n"
"background-color: #182635;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"min-width: 420px;\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"color: #d7dde3;\n"
"margin-top: 2ex; /* оставляем пространство вверху для заголовка */\n"
"}\n"
"\n"
"QGroupBox::title\n"
"{\n"
"subcontrol-origin: margin;\n"
"subcontrol-position: top center; /* помещаем вверху по центру */\n"
"padding: 0 3px;\n"
"}\n"
"\n"
"QListWidget\n"
"{\n"
"background-color: #fafbfc;\n"
"alternate-background-color: #7487a3;\n"
"color: #182635;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"border: 0 px;\n"
"background-color: #182635;\n"
"}\n"
"\n"
"QTableWidget\n"
"{\n"
"background-color: #fafbfc;\n"
"}\n"
"\n"
"QTableWidget:item\n"
"{\n"
"color: #182635;\n"
"}\n"
"\n"
"QHeaderView\n"
"{\n"
"color: #182635;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"border: 1px solid #7487a3;\n"
"border-radius: 2px;\n"
"background-color: #182635;\n"
"selection-background-color:#fafbfc;\n"
"padding: 0 8px;\n"
"}\n"
"\n"
"QMenu {\n"
"margin: 2px; /* немного пространства вокруг меню */\n"
"background-color: #121e36;\n"
" }\n"
"\n"
"QMenuBar:item:selected\n"
"{\n"
"color: #fafbfc;\n"
"background-color: #121e36;\n"
"}\n"
"\n"
"QMenu::item {\n"
"padding: 2px 25px 2px 20px;\n"
"border: 1px solid transparent; /* резерв пространства для границы выделения */\n"
"background-color: #121e36;\n"
"color: #fafbfc;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"border-color: 1px solid #fafbfc;\n"
"}")
        self.textBrowser = QtWidgets.QTextBrowser(info_form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 581, 361))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(info_form)
        QtCore.QMetaObject.connectSlotsByName(info_form)

    def retranslateUi(self, info_form):
        _translate = QtCore.QCoreApplication.translate
        info_form.setWindowTitle(_translate("info_form", "Справка"))
        self.textBrowser.setHtml(_translate("info_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Сообщества:</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Для поиска пользователей необходимо указать сообщества (ссылка / ID / заголовок). Также возможен поиск сообществ – необходимо указать фразы для поиска. При поиске сообществ доступен выбор сортировки и количества сообществ на каждую фразу.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Критерии активности:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">По умолчанию указаны рекомендуемые критерии для поиска целевой аудитории. Но, при необходимости, можно уменьшить или увеличить количество анализируемых публикаций в каждом сообществе. При анализе сообществ можно учитывать лайки / комментарии или лайки и комментарии. Доступно изменение глубины активности пользователей (количество повторяющихся публикаций по лайкам / комментариям на каждого пользователя).</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Фильтр:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">После успешного поиска целевой аудитории пользователь может воспользоваться фильтром. Фильтр следует применять, когда пользователь уверен в выбранных критериях фильтрации, т.к. аудитория со скрытыми полями указанных критериев отсеивается.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Сохранение и загрузка полученной аудитории:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Доступен может скопировать полученную аудиторию в буфер обмена или сохранить в отдельном файле. При необходимости, пользователь может загрузить полученную ранее целевую аудиторию для применения фильтра.</span></p></body></html>"))

