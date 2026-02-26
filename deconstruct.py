import os

inpput_file = input("Enter the path to the file you want to deconstruct: ")
output_folder = "bit_folder"

os.makedirs(output_folder, exist_ok=True)

with open(input_file, "rb") as f:
    data = f.read()

counter = 0

for byte in data:
    binary_string = format(byte,"08b")

    for bit in binary_string:
        filename = os.path.join(output_folder, f"bit_{counter}.txt")

        with open(filename, "wb") as bit_file:
            if bit == "0":
                bit_file.write(bytes([0]))
            else:
                bit_file.write(bytes([1]))

        counter += 1


print(f"Jackhammerin' complete. {counter} pieces of rubble saved in '{output_folder}'.")