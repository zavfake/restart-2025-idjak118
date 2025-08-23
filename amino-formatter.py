import os
human_insulin_clean = "malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"
human_insulin_clean = human_insulin_clean.replace(" ","")
print(human_insulin_clean)

temp_data = {
    "isinsulin-seq-clean": "",
    "binsulin-seq-clean": "",
    "cinsulin-seq-clean": "",
    "ainsulin-seq-clean": ""
}

# Memasukkan karakter ke temp_data
for idx, char in enumerate(human_insulin_clean):
    seq = idx+1
    if(seq <= 24):
        temp_data["isinsulin-seq-clean"] += char
    elif(seq >= 25 and seq <= 54):
        temp_data["binsulin-seq-clean"] += char
    elif(seq >= 55 and seq <= 89):
        temp_data["cinsulin-seq-clean"] += char
    else:
        temp_data["ainsulin-seq-clean"] += char
       
# Buat folder jika belum tersedia
folder_path = "asam_amino_clean"
os.makedirs(folder_path, exist_ok=True)

# untuk cek panjang dan write ke file
for key, d in temp_data.items():
    print("Panjang {} adalah {}".format(key, len(d)))
    with open("asam_amino_clean/{}.txt".format(key), "w") as text_file:
        text_file.write(d)