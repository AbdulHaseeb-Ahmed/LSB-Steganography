from PIL import Image
import numpy as np

def main():
    im = Image.open('cat.jpeg', 'r')
    pixels = list(im.getdata())
    secret_message = input('Enter secret message: ')
    print("Your secret message is: " + secret_message)
    valid = messagevalidation(secret_message, pixels)
    if(valid != True):
        main()
    secret_message_binary = secretmessageTobinary(secret_message)
    print("The secret message in binary is: " + str(secret_message_binary))
    pixels_binary_val = pixelDecToBin(pixels)
    concatenated_secret_message_bits = continousBitsOfSecretMessage(secret_message_binary)
    print(concatenated_secret_message_bits)
    pixel2Change = numberOfPixelstoChange(concatenated_secret_message_bits)
    print(pixel2Change)
    beforeEncodingPixelBinaryValues(pixels_binary_val, pixel2Change)
    beforeEncodingPixelDecimalValues(pixels_binary_val, pixel2Change)
    alteredpixels = insertingMessageinImage(pixels_binary_val, concatenated_secret_message_bits, pixel2Change)
    afterEncodingPixelBinaryValues(alteredpixels, pixel2Change)
    afterEncodingPixelDecimalValues(alteredpixels, pixel2Change)
    decodedmessage = extractMessage(alteredpixels, pixel2Change)
    print(decodedmessage)
    NewImagePixelsAllDecimal = getNewImagePixels(alteredpixels)
    im.save("StegoCat.jpeg")

def messagevalidation(message, size):
    total_bits = len(message) * 8
    print("There a total of " + str(total_bits) + " bits.")
    if(total_bits < len(size)):
        print("Your input is of correct size to fit into the image")
        return True
    else:
        print("Please restart the program to enter a new message because the current message is to large to fit in the image")
        return False

def secretmessageTobinary(message):
    sec_message_binary = []
    for character in message:
        sec_message_binary.append(format(ord(character), '08b'))
    return sec_message_binary

def pixelDecToBin(Dec_pixels):
    bin_pixels = []
    for pixel in range(0, len(Dec_pixels)):
        List = []
        List.append(format(Dec_pixels[pixel][0], '08b'))
        List.append(format(Dec_pixels[pixel][1], '08b'))
        List.append(format(Dec_pixels[pixel][2], '08b'))
        bin_pixels.append(List)
    print("All the pixels in the image have been converted from decimal to binary vlaues")
    return bin_pixels

def continousBitsOfSecretMessage(secret_message_bytes):
    sec_message_concat = []
    for i in range(0, len(secret_message_bytes)):
        for j in range(0, 8):
            sec_message_concat.append(secret_message_bytes[i][j])
    print("All the bits of the secret message concatenated together is: ")
    return sec_message_concat

def numberOfPixelstoChange(concatenatedSecretMessage):
    P2Change = 0
    if(len(concatenatedSecretMessage) % 3 != 0):
        P2Change = int(len(concatenatedSecretMessage)/3) + 1
    else:
        P2Change = int(len(concatenatedSecretMessage)/3)
    print("The number of pixels to change in the image is (each pixel will have 3 changes as there are 3 colors in each pixel rgb): ")
    return P2Change

def beforeEncodingPixelBinaryValues(binary_pixels ,pixelstochange):
    print("Before encoding the image with the message, the pixel values in binary are:")
    for i in range(0, pixelstochange):
        print(binary_pixels[i])

def beforeEncodingPixelDecimalValues(binary_pixels ,pixelstochange):
    print("Before encoding the image with the message the pixel values in decimal are:")
    dec_pixels_before = []
    for i in range(0,pixelstochange):
        dec = []
        dec.append(int(binary_pixels[i][0], 2))
        dec.append(int(binary_pixels[i][1], 2))
        dec.append(int(binary_pixels[i][2], 2))
        dec_pixels_before.append(dec)
    for i in range(0, pixelstochange):
        print(dec_pixels_before[i])

def insertingMessageinImage(binary_pixels, concatenatedSecretMessage, pixelstochange):
    bit_index = 7
    index = 0
    for pixel in range(0, pixelstochange):
        for rgb_index in range(0, 3):
            if(index == len(concatenatedSecretMessage)):
                break
            if(binary_pixels[pixel][rgb_index][bit_index] != concatenatedSecretMessage[index]):
                binary_pixels[pixel][rgb_index] = binary_pixels[pixel][rgb_index][:-1] + concatenatedSecretMessage[index]
            index += 1
    print("The pixels have been altered to hold the message!")
    return binary_pixels

def afterEncodingPixelBinaryValues(new_binary_pixels ,pixelstochange):
    print("After encodning the image with the message the pixel values in binary are:")
    for i in range(0, pixelstochange):
        print(new_binary_pixels[i])

def afterEncodingPixelDecimalValues(new_binary_pixels, pixelstochange):
    print("After encoding the image with the message the pixel values in decimal are:")
    dec_pixels_after = []
    for i in range(0, pixelstochange):
        dec = []
        dec.append(int(new_binary_pixels[i][0], 2))
        dec.append(int(new_binary_pixels[i][1], 2))
        dec.append(int(new_binary_pixels[i][2], 2))
        dec_pixels_after.append(dec)
    for i in range(0, pixelstochange):
        print(dec_pixels_after[i])

def getNewImagePixels(new_binary_pixels):
    dec_pixels_after_all = []
    for i in range(0, len(new_binary_pixels)):
        dec = []
        dec.append(int(new_binary_pixels[i][0], 2))
        dec.append(int(new_binary_pixels[i][1], 2))
        dec.append(int(new_binary_pixels[i][2], 2))
        dec_pixels_after_all.append(dec)
    return dec_pixels_after_all

def extractMessage(new_binary_pixels, pixelstochange):
    secret_message_bits = []
    for i in range(0, pixelstochange):
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
        secret_message_ASCII.append(chr(int(secret_message_decimal[i])))

    message = "".join(secret_message_ASCII)
    print("The secret message hidden in the image was: ")
    return message

if __name__== "__main__":
    main()