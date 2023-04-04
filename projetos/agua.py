import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import QTimer

class Garrafa(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        # Define o tempo de espera em milissegundos (1 hora = 3600000 ms)
        self.timer.setInterval(3600000)
        # Conecta o sinal timeout do QTimer a função lembrete_agua
        self.timer.timeout.connect(self.lembrete_agua)
        # Inicia o QTimer
        self.timer.start()

        # Define as dimensões da janela
        self.width = 300
        self.height = 500
        self.setGeometry(100, 100, self.width, self.height)

        # Define o volume da garrafa
        self.volume = 2000
        self.agua = 0

        # Define os botões fechar e bebi água
        self.btn_fechar = QPushButton('Fechar', self)
        self.btn_fechar.move(20, 20)
        self.btn_fechar.clicked.connect(self.fechar)

        self.btn_agua = QPushButton('Bebi Água', self)
        self.btn_agua.move(160, 20)
        self.btn_agua.clicked.connect(self.adicionar_agua)

        # Define a label para exibir o total de água dentro da garrafa
        self.label_agua = QLabel('Água: {} ml'.format(self.agua), self)
        self.label_agua.resize(100, 20)
        self.label_agua.move(100, 420)

        # Define a cor da garrafa
        self.cor_garrafa = QColor(230, 230, 230)

        # Define as dimensões da garrafa
        self.x_garrafa = 50
        self.y_garrafa = 80
        self.width_garrafa = 200
        self.height_garrafa = 300

    def lembrete_agua(self):
        # Cria um QMessageBox para exibir o lembrete
        msgBox = QMessageBox()
        msgBox.setText("Hora de beber água!")
        msgBox.setInformativeText("Já passou 1 hora desde a sua última hidratação. Deseja reiniciar a contagem?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # Exibe o QMessageBox e espera pela resposta do usuário
        resposta = msgBox.exec_()
        if resposta == QMessageBox.Yes:
            # Reinicia a contagem de água
            self.agua = 0
            self.label_agua.setText('Água: {} ml'.format(self.agua))
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Desenha a garrafa
        self.desenhar_garrafa(painter)

        # Desenha a água dentro da garrafa
        self.desenhar_agua(painter)

    def desenhar_garrafa(self, painter):
        painter.setBrush(QBrush(self.cor_garrafa))
        painter.drawRect(self.x_garrafa, self.y_garrafa, self.width_garrafa, self.height_garrafa)
        painter.drawLine(self.x_garrafa, self.y_garrafa + self.height_garrafa, self.x_garrafa + self.width_garrafa, self.y_garrafa + self.height_garrafa)

    def desenhar_agua(self, painter):
        # Desenha a água na garrafa
        altura_agua = int(self.agua / self.volume * self.height_garrafa)
        painter.setBrush(Qt.blue)
        painter.drawRect(self.x_garrafa, self.y_garrafa + self.height_garrafa - altura_agua, self.width_garrafa, altura_agua)


    def adicionar_agua(self):
        if self.agua < self.volume:
            self.agua += 500
            self.label_agua.setText('Água: {} ml'.format(self.agua))

            # Redesenha a garrafa com a nova quantidade de água
            self.update()

    def fechar(self):
        # Fecha a aplicação
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    garrafa = Garrafa()
    garrafa.show()
    sys.exit(app.exec_())

