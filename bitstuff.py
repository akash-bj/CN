def bit_stuffing(data):
    stuffed = ""
    count = 0

    for bit in data:
        if bit == '1':
            count += 1
            stuffed += bit

            if count == 5:
                stuffed += '0'   # Stuffing 0 after five 1s
                count = 0
        else:
            stuffed += bit
            count = 0

    return stuffed


# Input (8-bit data)
data = input("Enter 8-bit data: ")

if len(data) != 8 or any(b not in '01' for b in data):
    print("Invalid input. Enter exactly 8 bits.")
else:
    stuffed_data = bit_stuffing(data)
    print("Original Data :", data)
    print("Stuffed Data  :", stuffed_data)
