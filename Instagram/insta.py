import json

# ==========================================================
# GANTI BAGIAN DI BAWAH INI DENGAN PATH LENGKAP FILE KAMU
# Gunakan huruf 'r' di depan tanda kutip agar tidak error
# ==========================================================
path_following = r"C:\VSCODEZ\Codez-Py\Instagram\following.json"
path_followers = r"C:\VSCODEZ\Codez-Py\Instagram\followers_1.json"

def ekstrak_data(path_file, is_following=False):
    usernames = set()
    try:
        with open(path_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Jika following, ambil dari 'relationships_following'
            # Jika followers, biasanya langsung berupa list
            if is_following:
                items = data.get('relationships_following', [])
            else:
                items = data if isinstance(data, list) else []

            for item in items:
                # BERDASARKAN JSON KAMU: Username ada di 'title'
                username = item.get('title')
                if username:
                    usernames.add(username)
                else:
                    # Backup: jika 'title' tidak ada, coba cari di 'string_list_data'
                    try:
                        username_alt = item['string_list_data'][0].get('value')
                        if username_alt:
                            usernames.add(username_alt)
                    except (KeyError, IndexError):
                        continue
            return usernames
    except Exception as e:
        print(f"❌ Gagal membaca {path_file}: {e}")
        return set()

# Eksekusi
print("Menganalisis data...")
set_following = ekstrak_data(path_following, is_following=True)
set_followers = ekstrak_data(path_followers, is_following=False)

# Hasil
tidak_follback = set_following - set_followers

print("="*40)
print(f"BERHASIL MEMBACA DATA:")
print(f"Total yang kamu ikuti (Following): {len(set_following)}")
print(f"Total yang mengikuti kamu (Followers): {len(set_followers)}")
print("-"*40)

if len(tidak_follback) > 0:
    print(f"Ada {len(tidak_follback)} akun tidak follback kamu:") 
    for i, user in enumerate(sorted(tidak_follback), 1):
        print(f"{i}. https://www.instagram.com/{user}")
else:
    print("Semua orang sudah follback kamu!")