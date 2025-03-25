let songs = [];
let favorites = [];
let currentSongIndex = 0;
let playingFavorites = false;

const audio = document.getElementById("audio");
const songList = document.getElementById("songList");
const favoriteList = document.getElementById("favoriteList");
const searchInput = document.getElementById("search");
const toggleThemeButton = document.getElementById("toggleTheme");
const addSongForm = document.getElementById("addSongForm");
const songTitleInput = document.getElementById("songTitle");
const songFileInput = document.getElementById("songFile");

fetch("/songs")
    .then(response => response.json())
    .then(data => {
        songs = data;
        loadSongs();
    });

function loadSongs(filter = "") {
    songList.innerHTML = "";
    songs.filter(song => song.title.toLowerCase().includes(filter.toLowerCase()))
        .forEach((song, index) => {
            let li = document.createElement("li");
            li.textContent = song.title;
            li.onclick = () => playSong(index, false);

            let deleteButton = document.createElement("button");
            deleteButton.textContent = "Eliminar";
            deleteButton.onclick = (e) => {
                e.stopPropagation();
                deleteSong(index);
            };
            li.appendChild(deleteButton);

            let favButton = document.createElement("button");
            favButton.textContent = "❤";
            favButton.onclick = (e) => {
                e.stopPropagation();
                toggleFavorite(song);
            };
            li.appendChild(favButton);
            songList.appendChild(li);
        });
}

function playSong(index, isFavorite) {
    playingFavorites = isFavorite;
    currentSongIndex = index;
    const song = isFavorite ? favorites[index] : songs[index];
    
    audio.src = song.file_path;
    audio.play();

    audio.onended = () => {
        if (playingFavorites) {
            if (currentSongIndex < favorites.length - 1) {
                playSong(currentSongIndex + 1, true); 
            }
        } else {
            if (currentSongIndex < songs.length - 1) {
                playSong(currentSongIndex + 1, false); 
            }
        }
    };
}

function nextSong() {
    if (playingFavorites) {
        if (currentSongIndex < favorites.length - 1) {
            playSong(currentSongIndex + 1, true);
        }
    } else {
        if (currentSongIndex < songs.length - 1) {
            playSong(currentSongIndex + 1, false);
        }
    }
}

function prevSong() {
    if (currentSongIndex > 0) {
        playSong(currentSongIndex - 1, playingFavorites);
    }
}

function forward10() {
    audio.currentTime += 10;
}

function rewind10() {
    audio.currentTime -= 10;
}

function deleteSong(index) {
    songs.splice(index, 1);
    if (currentSongIndex >= index) {
        currentSongIndex = Math.max(currentSongIndex - 1, 0);
    }
    loadSongs();
}

function toggleFavorite(song) {
    const index = favorites.findIndex(fav => fav.title === song.title);
    if (index !== -1) {
        favorites.splice(index, 1);
    } else {
        favorites.push(song);
    }
    loadFavorites();
}

function loadFavorites() {
    favoriteList.innerHTML = "";
    favorites.forEach((song, index) => {
        let li = document.createElement("li");
        li.textContent = song.title;
        li.onclick = () => playSong(index, true);
        favoriteList.appendChild(li);
    });
}

addSongForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const title = songTitleInput.value;
    const file = songFileInput.files[0];
    if (title && file) {
        const filePath = URL.createObjectURL(file);
        const newSong = { title, file_path: filePath };
        songs.push(newSong);
        loadSongs();
        songTitleInput.value = "";
        songFileInput.value = "";
    }
});

searchInput.addEventListener("input", (e) => {
    loadSongs(e.target.value);
});

toggleThemeButton.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    toggleThemeButton.textContent = document.body.classList.contains("dark-mode") ? "Modo Claro" : "Modo Oscuro";
});