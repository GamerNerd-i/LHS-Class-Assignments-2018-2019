from run_length import encode, decode

print(encode("AABBCCDDEEE"))
print("2A2B2C2D3E")
print(encode("AAABCCDDDDAAB"))
print("3A1B2C4D2A1B")

print()
print(decode("3F2A1B4D1C"))
print("FFFAABDDDDC")
print(decode("1A1B1A1B1A2B2A"))
print("ABABABBAA")
