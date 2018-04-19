# coding=utf-8
# !/usr/bin/python

"""
Barulhômetro

Código do programa de interatividade do barulhômetro
desenvolvido para o SIS - Observatório Sismológico da UnB.

Contém trechos do exemplo: PyQt Video Player Widget Example
Disponível em - pythonprogramminglanguage.com

O Código está disponível sob uma liçenca GPL v3

@author Mateus Berardo de Souza Terra
@date 17/04/2018
"""

import os
import sys
import time

from PyQt5.QtCore import QEventLoop, QUrl, Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QApplication, QPushButton, QStackedLayout, QVBoxLayout, QMainWindow, QWidget, QLabel


class VideoWindow(QMainWindow):

    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)
        self.setWindowTitle("Barulhômetro")
        self.videos = {'leve':QMediaContent(QUrl.fromLocalFile(os.path.abspath("recursos/leve.mp4"))),
                  'medio':QMediaContent(QUrl.fromLocalFile(os.path.abspath("recursos/medio.mp4"))),
                  'forte':QMediaContent(QUrl.fromLocalFile(os.path.abspath("recursos/forte.mp4"))),
                  'mega':QMediaContent(QUrl.fromLocalFile(os.path.abspath("recursos/mega.mp4")))}
        self.acabou = False
        self.setStyleSheet("""QLabel{
                            margin: 40px;
                            qproperty-alignment: AlignCenter;
                            }
                            .QWidget{
                                border-image: url(recursos/fotinha.jpeg) 0 0 0 0 stretch stretch;
                            }
                            """)

        # Cria o player de video
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        video_widget = QVideoWidget()

        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)
        self.layout = QStackedLayout(wid)

        # Cria o widget das opções
        self.options_widget = QWidget(self)
        # Cria imagem de fundo
        self.options_widget.setStyleSheet(".QWidget{border-image: url(recursos/fotinha.jpeg) 0 0 0 0 stretch stretch;}")
        # Cria o layout do widget das opções
        layout_widgets = QVBoxLayout(self.options_widget)
        self.titulo = QLabel("Barulhômetro")
        self.titulo.setStyleSheet("font-size:48px;")
        leve = QLabel("Aqui entra descrição rápida do terremoto leve")
        medio = QLabel("Aqui entra descrição rápida do terremoto medio")
        pesado = QLabel("Aqui entra descrição rápida do terremoto pesado")
        mega = QLabel("Aqui entra descrição rápida do terremoto mega")
        video = QPushButton("Vídeo")
        video.clicked.connect(self.openFile)
        layout_widgets.setAlignment(Qt.AlignCenter)
        layout_widgets.addWidget(self.titulo)
        layout_widgets.addWidget(leve)
        layout_widgets.addWidget(medio)
        layout_widgets.addWidget(pesado)
        layout_widgets.addWidget(mega)
        layout_widgets.addWidget(video)

        self.layout.addWidget(video_widget)
        self.layout.addWidget(self.options_widget)
        video_widget.setStyleSheet("background:rgba(0,0,0,0)")
        self.layout.setCurrentIndex(1)
        self.mediaPlayer.setVideoOutput(video_widget)
        self.mediaPlayer.error.connect(self.handleError)

    def fadeout(self):
        # w is your widget
        eff = QGraphicsOpacityEffect(self)
        self.options_widget.setGraphicsEffect(eff)
        self.a = QPropertyAnimation(self)
        self.a.setPropertyName("opacity")
        self.a.setTargetObject(eff)
        self.a.setDuration(1300)
        self.a.setStartValue(1)
        self.a.setEndValue(0)
        self.a.setEasingCurve(QEasingCurve.OutBack)
        loop = QEventLoop()
        self.a.finished.connect(loop.quit)
        self.a.start()
        loop.exec_()  # Execution stops here until finished called
        # now implement a slot called hideThisWidget() to do
        # things like hide any background dimmer, etc.

    def openFile(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(os.path.abspath("recursos/leve.mp4"))))
        self.mediaPlayer.play()
        self.mediaPlayer.pause()
        self.fadeout()
        self.layout.setCurrentIndex(0)

    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.setMedia(videos.get('leve'))
            self.mediaPlayer.setPosition(2000)
            self.mediaPlayer.play()

    def handleError(self):
        #self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoWindow()
    player.showFullScreen()
    sys.exit(app.exec_())
