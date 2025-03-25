from flask import Flask, request, jsonify, render_template, send_from_directory
import os

app = Flask(__name__)

class Song:
    def __init__(self, title, file_path):
        self.title = title
        self.file_path = file_path
        self.prev = None
        self.next = None
        self.is_favorite = False

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title, file_path):
        new_song = Song(title, file_path)
        if not self.head:
            self.head = self.tail = self.current = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song

    def remove_song(self, title):
        temp = self.head
        while temp:
            if temp.title == title:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                if temp == self.tail:
                    self.tail = temp.prev
                if temp == self.current:
                    self.current = temp.next or self.head
                return
            temp = temp.next

    def toggle_favorite(self, title, favorite_list):
        temp = self.head
        while temp:
            if temp.title == title:
                temp.is_favorite = not temp.is_favorite
                if temp.is_favorite:
                    favorite_list.add_song(temp.title, temp.file_path)
                else:
                    favorite_list.remove_song(temp.title)
                return
            temp = temp.next

playlist = DoublyLinkedList()
favorites = DoublyLinkedList()

def load_songs():
    songs_folder = "songs"
    if not os.path.exists(songs_folder):
        os.makedirs(songs_folder)
    for file in os.listdir(songs_folder):
        if file.endswith(".mp3"):
            title = os.path.splitext(file)[0]
            file_path = f"/songs/{file}"  
            playlist.add_song(title, file_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/songs", methods=["GET"])
def get_songs():
    temp = playlist.head
    songs = []
    while temp:
        songs.append({"title": temp.title, "file_path": temp.file_path})
        temp = temp.next
    return jsonify(songs)

@app.route("/favorite", methods=["POST"])
def toggle_favorite():
    data = request.json
    title = data.get("title")
    playlist.toggle_favorite(title, favorites)
    return jsonify({"message": "Estado de favorito cambiado"})

@app.route("/favorites", methods=["GET"])
def get_favorites():
    temp = favorites.head
    songs = []
    while temp:
        songs.append({"title": temp.title, "file_path": temp.file_path})
        temp = temp.next
    return jsonify(songs)

@app.route("/songs/<filename>")
def serve_song(filename):
    return send_from_directory("songs", filename)

if __name__ == "__main__":
    load_songs()
    app.run(debug=True)