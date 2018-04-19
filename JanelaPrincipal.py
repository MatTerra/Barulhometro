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

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QPushButton, QStackedLayout, QVBoxLayout, QMainWindow, QWidget, QLabel


class VideoWindow(QMainWindow):

    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)
        self.setWindowTitle("Barulhômetro")
        videos = {'leve':'endereco',
                  'medio':'endereco',
                  'forte':'endereco',
                  'mega':'endereco'}

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
        options_widget = QWidget(self)
        # Cria imagem de fundo
        options_widget.setStyleSheet(".QWidget{border-image: url(recursos/fotinha.jpeg) 0 0 0 0 stretch stretch;}")
        # Cria o layout do widget das opções
        layout_widgets = QVBoxLayout(options_widget)
        titulo = QLabel("Barulhômetro")
        titulo.setStyleSheet("font-size:48px;")
        leve = QLabel("Aqui entra descrição rápida do terremoto leve")
        medio = QLabel("Aqui entra descrição rápida do terremoto medio")
        pesado = QLabel("Aqui entra descrição rápida do terremoto pesado")
        mega = QLabel("Aqui entra descrição rápida do terremoto mega")
        video = QPushButton("Vídeo")
        video.clicked.connect(self.openFile)
        layout_widgets.setAlignment(Qt.AlignCenter)
        layout_widgets.addWidget(titulo)
        layout_widgets.addWidget(leve)
        layout_widgets.addWidget(medio)
        layout_widgets.addWidget(pesado)
        layout_widgets.addWidget(mega)
        layout_widgets.addWidget(video)

        self.layout.addWidget(video_widget)
        self.layout.addWidget(options_widget)
        video_widget.setStyleSheet("background:rgba(0,0,0,0)")
        self.layout.setCurrentIndex(1)
        self.mediaPlayer.setVideoOutput(video_widget)
        self.mediaPlayer.error.connect(self.handleError)

    def fadeout(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("/home/debian/Pictures/fotinha.jpeg")))

    def openFile(self):
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(os.path.abspath("recursos/example.mp4"))))
        self.mediaPlayer.play()
        self.layout.setCurrentIndex(0)

    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(os.path.abspath("recursos/example2.mp4"))))
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
