#ASCII
for i in range(1, 255):
	ch = chr(i)
	print(i, "=", ch)
#Convert ke ascii
Pesan = raw_input("Masukan Pesan Untuk COnvert Ke ASCII: ")
print "_________________________________________"
print "kode dalam ASCII: "
for ch in Pesan:
    print ord(ch),
    print " "
print " <Tekan Enter Untu Kelar> "
