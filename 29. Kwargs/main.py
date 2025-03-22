# **kwargs
# Function yang bisa menginputkan banyak nilai untuk argumentnya dan menghasilkan dictionary

def pengguna(**data):
    nama = data["nama"]
    umur = data["umur"]
    asal = data["asal"]
    
    print(f"Nama {str(nama).title()} umur {umur} asal {asal}")
    

pengguna(nama = "aang solihin", umur = 19, asal = "Sumedang")