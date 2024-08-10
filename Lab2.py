import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class PersonalInfoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.name_label = QLabel('Họ và tên:', self)
        self.phone_label = QLabel('Số điện thoại:', self)

        self.name_input = QLineEdit(self)
        self.phone_input = QLineEdit(self)

        self.save_button = QPushButton('Lưu thông tin', self)
        self.clear_button = QPushButton('Xóa thông tin', self)

        self.saved_name_label = QLabel('', self)
        self.saved_phone_label = QLabel('', self)

        # Bố cục
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.saved_name_label)
        layout.addWidget(self.saved_phone_label)

        self.setLayout(layout)

        # Kết nối các sự kiện
        self.save_button.clicked.connect(self.save_info)
        self.clear_button.clicked.connect(self.clear_info)

        # Thiết lập giao diện chính
        self.setWindowTitle('Quản lý thông tin cá nhân')
        self.setGeometry(100, 100, 300, 200)

    def save_info(self):
        # Lấy thông tin từ các ô nhập liệu và hiển thị trên các nhãn
        name = self.name_input.text()
        phone = self.phone_input.text()

        self.saved_name_label.setText(f'Họ và tên: {name}')
        self.saved_phone_label.setText(f'Số điện thoại: {phone}')

    def clear_info(self):
        # Xóa thông tin trong các ô nhập liệu và các nhãn
        self.name_input.clear()
        self.phone_input.clear()
        self.saved_name_label.setText('')
        self.saved_phone_label.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PersonalInfoApp()
    ex.show()
    sys.exit(app.exec_())
