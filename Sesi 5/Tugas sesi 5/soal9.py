useradmin, passadmin = "admin", "admin123"
useruser, passuser = "user", "user123"
userguest = "guest"

inuser = input("Masukkan username: ")
inpass = input("Masukkan password (lewati jika anda guest): ")
if inuser == useradmin and inpass == passadmin:
    kategori = "akses admin"
elif inuser == useruser and inpass == passuser:
    kategori = "akses terbatas"
elif inuser == userguest:
    kategori = "akses minimal"
else:
    kategori = "akses di tolak"
print("%s, adalah akses yang anda dapatkan." % (kategori))