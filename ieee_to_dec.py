# To convert IEEE 754 format to decimal number
import struct


def ieee754_64bit_to_decimal(ieee754_binary):
    # Convert the binary string to bytes
    ieee754_bytes = bytes(int(ieee754_binary[i:i + 8], 2) for i in range(0, len(ieee754_binary), 8))

    # Unpack the bytes into a double-precision floating-point number
    decimal_number = struct.unpack('>d', ieee754_bytes)[0]

    return decimal_number


ieee754_binary_representation = "0100000010101001001100000000000000000000000000000000000000000000"
decimal_result = ieee754_64bit_to_decimal(ieee754_binary_representation)
print(f"The decimal representation is: {decimal_result}")

ieee754_binary_representation = "1100000010101001001100000000000000000000000000000000000000000000"
decimal_result = ieee754_64bit_to_decimal(ieee754_binary_representation)
print(f"The decimal representation is: {decimal_result}")

ieee754_binary_representation = "0011111111110101001100000000000000000000000000000000000000000000"
decimal_result = ieee754_64bit_to_decimal(ieee754_binary_representation)
print(f"The decimal representation is: {decimal_result}")

ieee754_binary_representation = "0011111111110101001100000000000000000000000000000000000000000001"
decimal_result = ieee754_64bit_to_decimal(ieee754_binary_representation)
print(f"The decimal representation is: {decimal_result}")
