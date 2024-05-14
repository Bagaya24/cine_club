from PySide2 import QtWidgets, QtCore

import movies


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cine club")
        
        self.setup_ui()
        self.setup_connection()
        self.populate_movies()
        self.css_mode()

    def setup_connection(self):
        self.btn_aujouter_movie.clicked.connect(self.add_movie)
        self.btn_supprimer_movie.clicked.connect(self.remove_movie)
        self.le_nom_movie.returnPressed.connect(self.add_movie)

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        self.le_nom_movie = QtWidgets.QLineEdit()
        self.le_nom_movie.setPlaceholderText("Nom du film")
        self.btn_aujouter_movie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_liste_movie = QtWidgets.QListWidget()
        self.lw_liste_movie.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_supprimer_movie = QtWidgets.QPushButton("Supprimer le(s) films")

        self.layout.addWidget(self.le_nom_movie)
        self.layout.addWidget(self.btn_aujouter_movie)
        self.layout.addWidget(self.lw_liste_movie)
        self.layout.addWidget(self.btn_supprimer_movie)

    def populate_movies(self):
        films = movies.get_movies()
        for film in films:
            lw_item = QtWidgets.QListWidgetItem(film.m_movie)
            lw_item.setData(QtCore.Qt.UserRole, film)
            self.lw_liste_movie.addItem(film.m_movie)

    def add_movie(self):
        movie_title = self.le_nom_movie.text()
        if not movie_title:
            return False
        movie = movies.Movie(movie_title)

        if movie.add_to_movies():
            lw_item = QtWidgets.QListWidgetItem(movie.m_movie)
            lw_item.movie = movie
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_liste_movie.addItem(movie.m_movie)
        self.le_nom_movie.setText("")

    def remove_movie(self):
        for selected_item in self.lw_liste_movie.selectedItems():
            movie = movies.Movie(selected_item.text())
            movie.remove_from_movies()
            self.lw_liste_movie.takeItem(self.lw_liste_movie.row(selected_item))

    def css_mode(self):
        self.setStyleSheet("""
            background-color:#F5F5F5;
            color:#4D4C7D;
            
        """)
        self.btn_supprimer_movie.setStyleSheet("""
            background-color:#F99417;
            color: #fff;
            font-weight: 600;
            border-radius: 8px;
            border: 1px solid #FFCD4B;
            padding: 5px 15px;
            margin-top: 10px;
            outline: 0px;
        """)
        self.btn_aujouter_movie.setStyleSheet("""
            background-color:#F99417;
            color: #fff;
            font-weight: 600;
            border-radius: 8px;
            border: 1px solid #FFCD4B;
            padding: 5px 15px;
            margin-top: 10px;
            outline: 0px;
                """)

        self.le_nom_movie.setStyleSheet("""
            border-radius: 8px;
            border: 1px solid #687EFF;
            padding: 5px 15px;
            """)

        self.lw_liste_movie.setStyleSheet("""
            border-radius: 8px;
            border: 1px solid #C1D8C3;
        """)




app = QtWidgets.QApplication([])
fenetre = App()
fenetre.show()

app.exec_()
