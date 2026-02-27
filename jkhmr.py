import os
import shutil
from PIL import Image
from tqdm import tqdm
import sys


def deconsruct (input_file):

    output_folder = "rubble"
    os.makedirs(output_folder, exist_ok=True)

    with open(input_file, "rb") as f:
        data = f.read()
        total_bits = len(data) * 8

    counter = 0

    with tqdm(total=total_bits, desc="Jackhammerin'", unit="bit") as pbar:
        for byte in data:
            binary_string = format(byte,"08b")

            for bit in binary_string:
                filename = os.path.join(output_folder, f"bit_{counter:08d}.txt")

                with open(filename, "wb") as bit_file:
                    if bit == "0":
                        bit_file.write(bytes([0]))
                    else:
                        bit_file.write(bytes([1]))

                counter += 1
                pbar.update(1)

    print(f"Jackhammerin' complete. {counter} pieces of rubble saved in '{output_folder}'. It is now ready for reconstruction using the magic of python and glue and stuff idk.")


def reconstruct (output_file):
    input_folder = "rubble"

    files = sorted(
    os.listdir(input_folder),
    key=lambda x: int(x.split("_")[1].split(".")[0]) 
    )

    all_bits = ""

    with tqdm(total=len(files), desc="Gluing rubble w/ magic", unit="bit") as pbar:
        for filename in files:
            with open(os.path.join(input_folder, filename), "rb") as f:
                byte_value = f.read(1)[0]
                if byte_value == 0:
                    all_bits +=  "0"
                else:
                    all_bits += "1"
            pbar.update(1)

    byte_array = bytearray()

    for i in range(0,len(all_bits), 8):
        chunk = all_bits[i:i+8]
        if len(chunk) == 8:
            byte_array.append(int(chunk, 2))

    with open(output_file, "wb") as f:
        f.write(byte_array)

    shutil.rmtree(input_folder)

    img = Image.open(output_file)
    img.show()

    print(f"Reconstruction complete. The rock has been recreated using magic and stuff from the rubble using glue or something idk.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  jackhammer deconstruct <input_file>")
        print("  jackhammer reconstruct <input_folder>")
        sys.exit(1)

    command = sys.argv[1]
    target = sys.argv[2]

    if command == "deconstruct":
        deconstruct(target)
    elif command == "reconstruct":
        if not target.lower().endswith(".png"):
            print("Reconstruction output must be a .png file.")
            sys.exit(1)
        reconstruct(target)
    else:
        print("Unknown command. Use 'deconstruct' or 'reconstruct'.")