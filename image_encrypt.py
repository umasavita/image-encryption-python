import cv2

def encrypt_image(image_path, key):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found. Check path!")
        return
    
    encrypted_img = cv2.add(img, key)
    cv2.imwrite("encrypted.png", encrypted_img)
    print("Encrypted image saved as encrypted.png")


def decrypt_image(image_path, key):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found. Check path!")
        return
    
    decrypted_img = cv2.subtract(img, key)
    cv2.imwrite("decrypted.png", decrypted_img)
    print("Decrypted image saved as decrypted.png")


# MAIN PROGRAM
print("1. Encrypt Image")
print("2. Decrypt Image")

try:
    choice = int(input("Enter choice: "))
    key = int(input("Enter key (0-255): "))
except:
    print("Invalid input! Enter numbers only.")
    exit()

if choice == 1:
    path = input("Enter image path: ")
    encrypt_image(path, key)

elif choice == 2:
    path = input("Enter encrypted image path: ")
    decrypt_image(path, key)

else:
    print("Invalid choice")