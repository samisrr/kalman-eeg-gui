import numpy as np

class KalmanFilter:
    def __init__(self, A=1, B=0, H=1, Q=1e-5, R=0.01, x0=0, P0=1):
        self.A = A
        self.B = B
        self.H = H
        self.Q = Q
        self.R = R
        self.x = x0
        self.P = P0

    def update(self, z, u=0):
        x_pred = self.A * self.x + self.B * u
        P_pred = self.A * self.P * self.A + self.Q

        K = P_pred * self.H / (self.H * P_pred * self.H + self.R)
        self.x = x_pred + K * (z - self.H * x_pred)
        self.P = (1 - K * self.H) * P_pred
        return self.x

    def filter(self, data):
        return np.array([self.update(z) for z in data])
