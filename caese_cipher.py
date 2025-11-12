
import string

#These will be used as ou encryption and decryption references
keys =string.ascii_letters + string.digits + string.punctuation + " "

#function for encrypting messages
def encrypt():

    #reserved string for our encrypted text
    encrypted = ""

    message = input("Enter a message to be encrypted: ") #message to be encrypted
    shift = input("Enter an lock key: ") #encryption key

    if len(shift) != 4:
        print("Invalid Encryption Key, Must be 4 digits long")
        exit()
    else:
        shift = int(shift)
        unlock_key = shift * len(message)
        for i in range(len(message)):
            if message[i] in keys: #finding a char at position i in keys

                # finding the index of a corresponding char in keys
                index = keys.index(message[i])

                #defining an index for encryption
                enc_index = (index + shift)
                enc_index = int(enc_index) #convert it to integer
                #working on indices exceeding the length of the keys
                if enc_index > len(keys) or enc_index < -len(keys):
                    enc_index = enc_index % len(keys)

                key = keys[enc_index] #key is in encrypted text
                encrypted = encrypted + key #adding a new key to the encrypted text
        print(f"Your encrypted message is: {encrypted}")
        print(f"Unlock key is: {unlock_key}")

#function for decrypting messages
def dencrypt():

    #reservation for decrypted message
    message = ""
    encrypted = input("Enter a cipher text: ")
    unlock_key = input("Enter unlock key: ")
    if not unlock_key.isdigit():
        print("Invalid Unlock key")
        exit()

    unlock_key = int(unlock_key)
    shift = unlock_key/len(encrypted)
    if shift < 1000:
        print("Invalid Encryption Key, Must be 4 digits long")
        exit()
    else:
        shift = int(shift)
        for i in range(len(encrypted)):
            if encrypted[i] in keys:
                index = keys.index(encrypted[i])

                mes_index = (index - shift)
                mes_index = int(mes_index)
                if mes_index < -len(keys) or mes_index > len(keys):
                    mes_index = mes_index % len(keys)

                key = keys[mes_index]
                message = message + key
        print(f"Your original message is: {message}")



print("\nWelcome TwinoDev Caesar Cipher Master.")
print("\n1.Encrypt Message")
print("2.Decrypt Message")
mode = input("Enter a mode: ")
if mode == "1":
    encrypt()
elif mode == "2":
    dencrypt()
else:
    print("Invalid mode")