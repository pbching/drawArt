import time
import cv2
from PIL import Image
while(True):
	name = input("Người yêu bạn tên gì: ")

	age = int(input("Anh/Cô ấy bao nhiêu tuổi: "))

	if (name == "Hà" and age == 20):
		print("Bắt đầu vẽ...")

		for i in range(0, 100, 10):
			print(f"Đang chạy... {i+10}%")
			time.sleep(0.4)
		print("Đã xong")

		f = open("ascii-art.txt", "r")
		lines = f.readlines()

		for line in lines:
			print("{}".format(line.strip()))
			time.sleep(0.3)
		
		for i in range(0,5,1):
			print("")
			time.sleep(0.3)

		f = open("ascii-art2.txt", "r")
		lines = f.readlines()

		for line in lines:
			print("{}".format(line.strip()))
			time.sleep(0.3)

		cap = cv2.VideoCapture("cv-vid-ascii/input_video/MyLover.mp4")
		ret, frame = cap.read()
		while(1):
		    ret, frame = cap.read()
		    cv2.imshow('Frame',frame)
		    if cv2.waitKey(25) & 0xFF == ord('q') or ret==False :
		        cap.release()
		        cv2.destroyAllWindows()
		        break
		    cv2.imshow('frame',frame)
		break
	else: 
		print("Không có dữ liệu! Vui lòng nhập lại!")

