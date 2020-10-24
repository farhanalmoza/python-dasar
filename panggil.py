import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan nama Anda")
parser.add_argument('-t', '--tanggal', required=True, help="Masukkan tanggal Anda")
args = parser.parse_args()

print("Halo, kakak " + args.nama)