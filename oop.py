class Kalkulator:
	"""contoh kelas kalkulator sederhana"""

	def __init__(self, nilai=0):
		self.nilai = nilai

	def tambah_angka(self, angka1, angka2):
		self.nilai = angka1 + angka2
		if self.nilai > 9: # Kalkulator sederhana hanya sampai 9
			print('Kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
		return self.nilai

class KalkulatorKali(Kalkulator):
	"""Contoh pewarisan kelas kalokator"""

	def kali_angka(self, angka1, angka2):
		self.nilai = angka1 * angka2
		return self.nilai

	def tambah_angka(self, angka1, angka2):
		self.nilai = angka1 + angka2
		return self.nilai

class KalkulatorTambah(Kalkulator):
	"""contoh pewarisan"""

	def tambah_angka(self, angka1, angka2):
		if angka1 + angka2 <= 9: 
			super().tambah_angka(angka1, angka2)
		else:
			self.nilai = angka1 + angka2
		return self.nilai

kk = KalkulatorTambah()
a = kk.tambah_angka(10, 4) # fitur kali angka
print(a)