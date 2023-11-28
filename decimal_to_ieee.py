# To convert decimal number to IEEE 754 format
import struct


def decimal_to_ieee754_32bit(decimal_number):
    # Pack the decimal number into its IEEE 754 single-precision representation
    ieee754_bytes = struct.pack('>f', decimal_number)
    # Convert the bytes to binary representation
    ieee754_binary = ''.join(f'{byte:08b}' for byte in ieee754_bytes)
    return ieee754_binary


def decimal_to_ieee754_64bit(decimal_number):
    # Pack the decimal number into its IEEE 754 double-precision representation
    ieee754_bytes = struct.pack('>d', decimal_number)

    # Convert the bytes to binary representation
    ieee754_binary = ''.join(f'{byte:08b}' for byte in ieee754_bytes)

    return ieee754_binary


Fine_structure = 0.0072973525693
speed_of_light = 299792458.0
newtons_constant = 6.67430e-8
plancks_constant = 4.135667696e-15
boltzmann_constant = 8.617333262145e-5
hubble_constant = 2.25e-18
mass_of_the_sun = 1.988500*10*33

ieee754_32bit_representation = decimal_to_ieee754_32bit(Fine_structure)
ieee754_64bit_representation = decimal_to_ieee754_64bit(Fine_structure)

print(f"The 32-bit IEEE 754 representation of Fine structure constant is: {ieee754_32bit_representation}")
print(f"The 64-bit IEEE 754 representation of Fine structure constant is: {ieee754_64bit_representation}")

ieee754_32bit_representation = decimal_to_ieee754_32bit(speed_of_light)
ieee754_64bit_representation = decimal_to_ieee754_64bit(speed_of_light)

print(f"The 32-bit IEEE 754 representation of speed_of_light is: {ieee754_32bit_representation}")
print(f"The 64-bit IEEE 754 representation of speed_of_light is: {ieee754_64bit_representation}")

ieee754_32bit_representation = decimal_to_ieee754_32bit(newtons_constant)
ieee754_64bit_representation = decimal_to_ieee754_64bit(newtons_constant)

print(f"The 32-bit IEEE 754 representation of newtons_constant is: {ieee754_32bit_representation}")
print(f"The 64-bit IEEE 754 representation of newtons_constant is: {ieee754_64bit_representation}")

ieee754_32bit_representation = decimal_to_ieee754_32bit(plancks_constant)
ieee754_64bit_representation = decimal_to_ieee754_64bit(plancks_constant)

print(f"The 32-bit IEEE 754 representation of plancks_constant is: {ieee754_32bit_representation}")
print(f"The 64-bit IEEE 754 representation of plancks_constant is: {ieee754_64bit_representation}")

ieee754_32bit_representation = decimal_to_ieee754_32bit(boltzmann_constant)
ieee754_64bit_representation = decimal_to_ieee754_64bit(boltzmann_constant)

print(f"The 32-bit IEEE 754 representation of boltzmann_constant is: {ieee754_32bit_representation}")
print(f"The 64-bit IEEE 754 representation of boltzmann_constant is: {ieee754_64bit_representation}")

ieee754_32bit_representation = decimal_to_ieee754_32bit(hubble_constant)
ieee754_64bit_representation = decimal_to_ieee754_64bit(hubble_constant)

print(f"The 32-bit IEEE 754 representation of hubble_constant is: {ieee754_32bit_representation}")
print(f"The 64-bit IEEE 754 representation of hubble_constant is: {ieee754_64bit_representation}")

ieee754_32bit_representation = decimal_to_ieee754_32bit(mass_of_the_sun)
ieee754_64bit_representation = decimal_to_ieee754_64bit(mass_of_the_sun)

print(f"The 32-bit IEEE 754 representation of mass_of_the_sun is: {ieee754_32bit_representation}")
print(f"The 64-bit IEEE 754 representation of mass_of_the_sun is: {ieee754_64bit_representation}")
