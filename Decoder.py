from PIL import Image
import numpy as np

def main():
    image = Image.open('StegoCat.png', 'r')
    pixels = list(image.getdata())
    pixels_binary_val = pixelDecToBin(pixels)
    decodedmessage = extractMessage(pixels_binary_val, 100)
    print(decodedmessage)

def pixelDecToBin(Dec_pixels):
    bin_pixels = []
    for pixel in range(0, len(Dec_pixels)):
        List = []
        List.append(format(Dec_pixels[pixel][0], '08b'))
        List.append(format(Dec_pixels[pixel][1], '08b'))
        List.append(format(Dec_pixels[pixel][2], '08b'))
        bin_pixels.append(List)
    return bin_pixels

def extractMessage(new_binary_pixels, pixelswithdata):
    secret_message_bits = []
    for i in range(0, pixelswithdata):
        for j in range(0, 3):
            secret_message_bits.append(new_binary_pixels[i][j][7])

    secret_message_binary = []
    index = 0
    pixel_val = []
    for i in range(0, len(secret_message_bits)):
        pixel_val.append(secret_message_bits[i])
        index += 1
        if(index == 8):
            result = "".join(pixel_val)
            secret_message_binary.append(result)
            index = 0
            pixel_val.clear()

    secret_message_decimal = []
    for i in range(0, len(secret_message_binary)):
        secret_message_decimal.append(int(secret_message_binary[i], 2))

    secret_message_ASCII = []
    for i in range(0, len(secret_message_decimal)):
        asciichar = chr(int(secret_message_decimal[i]))
        if(int(secret_message_decimal[i]) == 4):
            break
        else:
            secret_message_ASCII.append(asciichar)

    message = "".join(secret_message_ASCII)
    print("The secret message hidden in the image was: ")
    return message

if __name__== "__main__":
    main()