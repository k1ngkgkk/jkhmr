import os

input_folder = "bit_folder"
output_file = "reconstructed.png"

files = sorted(
    os.listdir(input_folder),
    key=lambda x: int(x.split("_")[1].split(".")[0]) 
)

all_bits = ""

for filename in files:
    with open(os.path.join(input_folder, filename), "rb") as f:
        byte_value = f.read(1)[0]
        if byte_value == 0:
            all_bits +=  "0"
        else:
            all_bits += "1"

byte_array = bytearray()

for i in range(0,len(all_bits), 8):
    chunk = all_bits[i:i+8]
    if len(chunk) == 8:
        byte_array.append(int(chunk, 2))

with open(output_file, "wb") as f:
    f.write(byte_array)

print(f"Reconstruction complete. The rock has been recreated using magic and stuff from the rubble idk.")