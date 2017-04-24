import threading
from PyQt5 import QtCore

import SignalMng
from Signal import Signal


class TimeControl(Signal):
    left_time = 0

    def start(self, time: int):
        self.left_time = time
        SignalMng.TICK += self.onTick

    def stop(self):
        SignalMng.TICK -= self.onTick

    def reset(self):
        self.left_time = 0
        SignalMng.TICK -= self.onTick

    def onTick(self, step):
        self.left_time -= step
        if self.left_time <= 0:
            SignalMng.TICK -= self.onTick
            self.dispatch()


class EditorModelDict(QtCore.QAbstractListModel):
    def __init__(self, data, parent=None, label_field="name"):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.label_field = label_field
        self._data = data
        self.data_list = list(data.items())

    def rowCount(self, parent=None):
        return len(self.data_list)

    def columnCount(self, parent=None):
        return 1

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return self.data_display_role(index)
            elif role == QtCore.Qt.UserRole:
                return self.data_role(index)
        return None

    def data_display_role(self, index):
        return getattr(self.data_list[index.row()][1], self.label_field)

    def data_role(self, index):
        return self.data_list[index.row()][1]

    def flags(self, index):
        if index.isValid():
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled
