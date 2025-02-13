import cv2

path1 = r'C:\Users\MSI-PC\OneDrive - Hanoi University of Science and Technology\Pictures\Screenshots\Screenshot 2025-02-13 154057.png'
path2 = r'C:\Users\MSI-PC\OneDrive - Hanoi University of Science and Technology\Pictures\Screenshots\Screenshot 2025-02-13 153437.png'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

if img1 is None or img2 is None:
    print("Lỗi: Không thể đọc ảnh, kiểm tra đường dẫn!")
    exit()

height = min(img1.shape[0], img2.shape[0])
width = min(img1.shape[1], img2.shape[1])

img1_resized = cv2.resize(img1, (width, height))
img2_resized = cv2.resize(img2, (width, height))

img1_gray = cv2.cvtColor(img1_resized, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2_resized, cv2.COLOR_BGR2GRAY)

bitwise_and = cv2.bitwise_and(img1_gray, img2_gray)  # Phép AND
bitwise_or = cv2.bitwise_or(img1_gray, img2_gray)    # Phép OR
bitwise_xor = cv2.bitwise_xor(img1_gray, img2_gray)  # Phép XOR
bitwise_not1 = cv2.bitwise_not(img1_gray)            # Phép NOT trên ảnh 1
bitwise_not2 = cv2.bitwise_not(img2_gray)            # Phép NOT trên ảnh 2

cv2.imshow("Ảnh 1 (Grayscale)", img1_gray)
cv2.imshow("Ảnh 2 (Grayscale)", img2_gray)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT (Image 1)", bitwise_not1)
cv2.imshow("Bitwise NOT (Image 2)", bitwise_not2)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
