import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QPushButton, QFileDialog,
                             QWidget, QLabel, QHBoxLayout, QLineEdit)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from kalman_filter import KalmanFilter

class EEGKalmanApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Filtro di Kalman per EEG')

        layout = QVBoxLayout()
        self.plot_canvas = FigureCanvas(plt.Figure())
        layout.addWidget(self.plot_canvas)
        self.ax = self.plot_canvas.figure.subplots()

        btn_layout = QHBoxLayout()
        self.load_button = QPushButton('Carica File EEG')
        self.load_button.clicked.connect(self.load_file)
        btn_layout.addWidget(self.load_button)

        self.q_input = QLineEdit("1e-5")
        self.r_input = QLineEdit("0.01")
        btn_layout.addWidget(QLabel("Q:"))
        btn_layout.addWidget(self.q_input)
        btn_layout.addWidget(QLabel("R:"))
        btn_layout.addWidget(self.r_input)

        self.filter_button = QPushButton('Applica Filtro')
        self.filter_button.clicked.connect(self.apply_filter)
        btn_layout.addWidget(self.filter_button)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Apri file EEG', '', 'CSV Files (*.csv)')
        if path:
            self.data = np.loadtxt(path, delimiter=',')
            self.ax.clear()
            self.ax.plot(self.data, label='Segnale Grezzo')
            self.ax.legend()
            self.plot_canvas.draw()

    def apply_filter(self):
        if hasattr(self, 'data'):
            Q = float(self.q_input.text())
            R = float(self.r_input.text())
            kf = KalmanFilter(Q=Q, R=R)
            filtered = kf.filter(self.data)
            self.ax.clear()
            self.ax.plot(self.data, label='Originale')
            self.ax.plot(filtered, label='Filtrato')
            self.ax.legend()
            self.plot_canvas.draw()

def run_gui():
    app = QApplication(sys.argv)
    win = EEGKalmanApp()
    win.show()
    sys.exit(app.exec_())
