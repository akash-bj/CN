def bit_destuffing(data):
    result = ""
    count = 0
    skip = False

    for i in range(len(data)):
        if skip:
            skip = False
            continue

        if data[i] == '1':
            count += 1
            result += '1'

            if count == 5:
                skip = True   # skip next stuffed 0
                count = 0
        else:
            result += '0'
            count = 0

    return result


# Input (16-bit stuffed data)
data = input("Enter 16-bit stuffed data: ")

if len(data) != 16 or any(b not in '01' for b in data):
    print("Invalid input. Enter exactly 16 bits.")
else:
    original = bit_destuffing(data)
    print("Destuffed Data :", original)
