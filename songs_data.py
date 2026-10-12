"""
songs_data.py — Curated song database for The Listening Tree.

Each song is a dict with:
    title      : Song name
    artist     : Artist / band name
    language   : "English" | "Hindi" | "Other"
    genre      : Pop | Rock | Devotional | Classical | Jazz | Indie | Bollywood
    style      : Acoustic | Electronic | Fusion | Lo-fi
    era        : "1950-1970" | "1970-1990s" | "1990-2010s" | "2010-2020s"
    popularity : "Trending" | "Classics"
"""

SONGS = [
    # ─────────────────────── ENGLISH · POP ───────────────────────
    {"title": "Yesterday", "artist": "The Beatles", "language": "English", "genre": "Pop", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Let It Be", "artist": "The Beatles", "language": "English", "genre": "Pop", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Wonderful Tonight", "artist": "Eric Clapton", "language": "English", "genre": "Pop", "style": "Acoustic", "era": "1970-1990s", "popularity": "Classics"},
    {"title": "Every Breath You Take", "artist": "The Police", "language": "English", "genre": "Pop", "style": "Acoustic", "era": "1970-1990s", "popularity": "Classics"},
    {"title": "Someone Like You", "artist": "Adele", "language": "English", "genre": "Pop", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Photograph", "artist": "Ed Sheeran", "language": "English", "genre": "Pop", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Drivers License", "artist": "Olivia Rodrigo", "language": "English", "genre": "Pop", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},

    {"title": "Blue (Da Ba Dee)", "artist": "Eiffel 65", "language": "English", "genre": "Pop", "style": "Electronic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "...Baby One More Time", "artist": "Britney Spears", "language": "English", "genre": "Pop", "style": "Electronic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Bad Guy", "artist": "Billie Eilish", "language": "English", "genre": "Pop", "style": "Electronic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Blinding Lights", "artist": "The Weeknd", "language": "English", "genre": "Pop", "style": "Electronic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Levitating", "artist": "Dua Lipa", "language": "English", "genre": "Pop", "style": "Electronic", "era": "2010-2020s", "popularity": "Trending"},

    {"title": "Shape of You", "artist": "Ed Sheeran", "language": "English", "genre": "Pop", "style": "Fusion", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Uptown Funk", "artist": "Bruno Mars ft. Mark Ronson", "language": "English", "genre": "Pop", "style": "Fusion", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Happy", "artist": "Pharrell Williams", "language": "English", "genre": "Pop", "style": "Fusion", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Smooth", "artist": "Santana ft. Rob Thomas", "language": "English", "genre": "Pop", "style": "Fusion", "era": "1990-2010s", "popularity": "Classics"},

    {"title": "Chill Vibes", "artist": "Lofi Hip Hop Radio", "language": "English", "genre": "Pop", "style": "Lo-fi", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Coffee Shop Beats", "artist": "ChilledCow", "language": "English", "genre": "Pop", "style": "Lo-fi", "era": "2010-2020s", "popularity": "Trending"},

    # ─────────────────────── ENGLISH · ROCK ───────────────────────
    {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "language": "English", "genre": "Rock", "style": "Acoustic", "era": "1970-1990s", "popularity": "Classics"},
    {"title": "Knockin' on Heaven's Door", "artist": "Bob Dylan", "language": "English", "genre": "Rock", "style": "Acoustic", "era": "1970-1990s", "popularity": "Classics"},
    {"title": "Wonderwall", "artist": "Oasis", "language": "English", "genre": "Rock", "style": "Acoustic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Fast Car", "artist": "Tracy Chapman", "language": "English", "genre": "Rock", "style": "Acoustic", "era": "1970-1990s", "popularity": "Classics"},

    {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "language": "English", "genre": "Rock", "style": "Electronic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "In the End", "artist": "Linkin Park", "language": "English", "genre": "Rock", "style": "Electronic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Numb", "artist": "Linkin Park", "language": "English", "genre": "Rock", "style": "Electronic", "era": "1990-2010s", "popularity": "Classics"},

    {"title": "Bohemian Rhapsody", "artist": "Queen", "language": "English", "genre": "Rock", "style": "Fusion", "era": "1970-1990s", "popularity": "Classics"},
    {"title": "Hotel California", "artist": "Eagles", "language": "English", "genre": "Rock", "style": "Fusion", "era": "1970-1990s", "popularity": "Classics"},
    {"title": "November Rain", "artist": "Guns N' Roses", "language": "English", "genre": "Rock", "style": "Fusion", "era": "1970-1990s", "popularity": "Classics"},

    # ─────────────────────── ENGLISH · JAZZ ───────────────────────
    {"title": "What a Wonderful World", "artist": "Louis Armstrong", "language": "English", "genre": "Jazz", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Fly Me to the Moon", "artist": "Frank Sinatra", "language": "English", "genre": "Jazz", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Feeling Good", "artist": "Nina Simone", "language": "English", "genre": "Jazz", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Take Five", "artist": "Dave Brubeck Quartet", "language": "English", "genre": "Jazz", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "So What", "artist": "Miles Davis", "language": "English", "genre": "Jazz", "style": "Fusion", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Autumn Leaves", "artist": "Bill Evans Trio", "language": "English", "genre": "Jazz", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "All of Me", "artist": "John Legend", "language": "English", "genre": "Jazz", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},

    # ─────────────────────── ENGLISH · INDIE ───────────────────────
    {"title": "Mr. Brightside", "artist": "The Killers", "language": "English", "genre": "Indie", "style": "Electronic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Do I Wanna Know?", "artist": "Arctic Monkeys", "language": "English", "genre": "Indie", "style": "Fusion", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Ribs", "artist": "Lorde", "language": "English", "genre": "Indie", "style": "Electronic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Stubborn Love", "artist": "The Lumineers", "language": "English", "genre": "Indie", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Ho Hey", "artist": "The Lumineers", "language": "English", "genre": "Indie", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Dog Days Are Over", "artist": "Florence + The Machine", "language": "English", "genre": "Indie", "style": "Fusion", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Skinny Love", "artist": "Bon Iver", "language": "English", "genre": "Indie", "style": "Acoustic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Sunset Lover", "artist": "Petit Biscuit", "language": "English", "genre": "Indie", "style": "Lo-fi", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Electric Feel", "artist": "MGMT", "language": "English", "genre": "Indie", "style": "Electronic", "era": "1990-2010s", "popularity": "Classics"},

    # ─────────────────────── ENGLISH · CLASSICAL ───────────────────────
    {"title": "Moonlight Sonata", "artist": "Ludwig van Beethoven", "language": "Other", "genre": "Classical", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Clair de Lune", "artist": "Claude Debussy", "language": "Other", "genre": "Classical", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Canon in D", "artist": "Johann Pachelbel", "language": "Other", "genre": "Classical", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Four Seasons – Spring", "artist": "Vivaldi", "language": "Other", "genre": "Classical", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},

    # ─────────────────────── HINDI · BOLLYWOOD ───────────────────────
    {"title": "Tum Hi Ho", "artist": "Arijit Singh", "language": "Hindi", "genre": "Bollywood", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Channa Mereya", "artist": "Arijit Singh", "language": "Hindi", "genre": "Bollywood", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Kabira", "artist": "Tochi Raina & Rekha Bhardwaj", "language": "Hindi", "genre": "Bollywood", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Kal Ho Naa Ho", "artist": "Sonu Nigam", "language": "Hindi", "genre": "Bollywood", "style": "Acoustic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Tujhe Kitna Chahne Lage", "artist": "Arijit Singh", "language": "Hindi", "genre": "Bollywood", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},

    {"title": "Rang De Basanti", "artist": "A.R. Rahman", "language": "Hindi", "genre": "Bollywood", "style": "Fusion", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Jai Ho", "artist": "A.R. Rahman", "language": "Hindi", "genre": "Bollywood", "style": "Fusion", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Dil Se Re", "artist": "A.R. Rahman", "language": "Hindi", "genre": "Bollywood", "style": "Fusion", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Kesariya", "artist": "Arijit Singh", "language": "Hindi", "genre": "Bollywood", "style": "Fusion", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Apna Bana Le", "artist": "Arijit Singh", "language": "Hindi", "genre": "Bollywood", "style": "Fusion", "era": "2010-2020s", "popularity": "Trending"},

    {"title": "Kaho Naa Pyaar Hai", "artist": "Udit Narayan", "language": "Hindi", "genre": "Bollywood", "style": "Electronic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Dhoom Again", "artist": "Uday Mazumdar & Dominique Cerejo", "language": "Hindi", "genre": "Bollywood", "style": "Electronic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Badtameez Dil", "artist": "Benny Dayal", "language": "Hindi", "genre": "Bollywood", "style": "Electronic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Lovely", "artist": "Kanika Kapoor & Shah Rukh Khan", "language": "Hindi", "genre": "Bollywood", "style": "Electronic", "era": "2010-2020s", "popularity": "Trending"},

    # ─────────────────────── HINDI · POP ───────────────────────
    {"title": "Tera Yaar Hoon Main", "artist": "Arijit Singh", "language": "Hindi", "genre": "Pop", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Ik Vaari Aa", "artist": "Arijit Singh", "language": "Hindi", "genre": "Pop", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Tu Hi Hai Aashiqui", "artist": "Dishoom", "language": "Hindi", "genre": "Pop", "style": "Acoustic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Paigam", "artist": "Jubin Nautiyal", "language": "Hindi", "genre": "Pop", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Teri Mitti", "artist": "B Praak", "language": "Hindi", "genre": "Pop", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},

    # ─────────────────────── HINDI · ROCK ───────────────────────
    {"title": "Dil Chahta Hai", "artist": "Shankar-Ehsaan-Loy", "language": "Hindi", "genre": "Rock", "style": "Fusion", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Rock On!!", "artist": "Farhan Akhtar", "language": "Hindi", "genre": "Rock", "style": "Fusion", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Zinda Hoon Main", "artist": "Farhan Akhtar", "language": "Hindi", "genre": "Rock", "style": "Acoustic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Dooba Dooba", "artist": "Silk Route", "language": "Hindi", "genre": "Rock", "style": "Acoustic", "era": "1990-2010s", "popularity": "Classics"},

    # ─────────────────────── HINDI · DEVOTIONAL ───────────────────────
    {"title": "Om Jai Jagdish Hare", "artist": "Anuradha Paudwal", "language": "Hindi", "genre": "Devotional", "style": "Acoustic", "era": "1970-1990s", "popularity": "Classics"},
    {"title": "Jai Maata Di", "artist": "Traditional", "language": "Hindi", "genre": "Devotional", "style": "Acoustic", "era": "1970-1990s", "popularity": "Classics"},
    {"title": "Man Ko Ati Bhave", "artist": "Pandit Jasraj", "language": "Hindi", "genre": "Devotional", "style": "Acoustic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Vaishnav Jana To", "artist": "Hari Om Sharan", "language": "Hindi", "genre": "Devotional", "style": "Acoustic", "era": "1970-1990s", "popularity": "Classics"},
    {"title": "Mahamrityunjay Mantra", "artist": "S. P. Balasubrahmanyam", "language": "Hindi", "genre": "Devotional", "style": "Fusion", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Shree Ram Chandra Kripalu", "artist": "Jagjit Singh", "language": "Hindi", "genre": "Devotional", "style": "Acoustic", "era": "1990-2010s", "popularity": "Classics"},

    # ─────────────────────── HINDI · CLASSICAL ───────────────────────
    {"title": "Raag Yaman", "artist": "Pandit Ravi Shankar", "language": "Hindi", "genre": "Classical", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Raag Bhairavi", "artist": "Ustad Bismillah Khan", "language": "Hindi", "genre": "Classical", "style": "Acoustic", "era": "1970-1990s", "popularity": "Classics"},
    {"title": "Raag Desh", "artist": "Pandit Hariprasad Chaurasia", "language": "Hindi", "genre": "Classical", "style": "Acoustic", "era": "1970-1990s", "popularity": "Classics"},

    # ─────────────────────── HINDI · INDIE ───────────────────────
    {"title": "Ik Kudi", "artist": "Diljit Dosanjh", "language": "Hindi", "genre": "Indie", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Bijlee Bijlee", "artist": "Harrdy Sandhu", "language": "Hindi", "genre": "Indie", "style": "Electronic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Khaabon Ke Parinday", "artist": "Mohit Chauhan & Alyssa Mendonsa", "language": "Hindi", "genre": "Indie", "style": "Acoustic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Pehla Nasha", "artist": "Udit Narayan & Sadhana Sargam", "language": "Hindi", "genre": "Indie", "style": "Acoustic", "era": "1990-2010s", "popularity": "Classics"},

    # ─────────────────────── OTHER LANGUAGES ───────────────────────
    {"title": "Bella Ciao", "artist": "Italian Folk", "language": "Other", "genre": "Indie", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "La Vie en Rose", "artist": "Édith Piaf", "language": "Other", "genre": "Jazz", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Despacito", "artist": "Luis Fonsi ft. Daddy Yankee", "language": "Other", "genre": "Pop", "style": "Fusion", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Lean On", "artist": "Major Lazer & DJ Snake", "language": "Other", "genre": "Pop", "style": "Electronic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Con Calma", "artist": "Daddy Yankee", "language": "Other", "genre": "Pop", "style": "Electronic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "La Bamba", "artist": "Ritchie Valens", "language": "Other", "genre": "Rock", "style": "Fusion", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Chan Chan", "artist": "Buena Vista Social Club", "language": "Other", "genre": "Jazz", "style": "Acoustic", "era": "1990-2010s", "popularity": "Classics"},
    {"title": "Gangnam Style", "artist": "PSY", "language": "Other", "genre": "Pop", "style": "Electronic", "era": "2010-2020s", "popularity": "Trending"},
    {"title": "Bamboleo", "artist": "Gipsy Kings", "language": "Other", "genre": "Indie", "style": "Acoustic", "era": "1970-1990s", "popularity": "Classics"},
    {"title": "Bésame Mucho", "artist": "Trio Los Panchos", "language": "Other", "genre": "Classical", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
    {"title": "Boum", "artist": "Charles Trenet", "language": "Other", "genre": "Pop", "style": "Acoustic", "era": "1950-1970", "popularity": "Classics"},
]
