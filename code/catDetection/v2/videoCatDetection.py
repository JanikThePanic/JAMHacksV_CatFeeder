import cv2, os, time

dirName = os.path.dirname(__file__)

def checkForCat():

	# img = cv2.imread('lena.png')
	capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
	capture.set(3, 640)
	capture.set(4, 480)

	# getting all the objects into a list
	classNames = []
	classFile = os.path.join(dirName, 'coco.names')
	with open(classFile, 'rt') as f:
		classNames = f.read().rstrip('\n').split('\n')

	configPath = os.path.join(dirName, 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
	weightsPath = os.path.join(dirName, 'frozen_inference_graph.pb')

	net = cv2.dnn_DetectionModel(weightsPath, configPath)
	net.setInputSize(320,320)
	net.setInputScale(1.0/127.5)
	net.setInputMean((127.5, 127.5, 127.5))
	net.setInputSwapRB(True)

	found = False

	while True:

		if found == True:
			time.sleep(2)
			cv2.destroyAllWindows()
			return True

		success, img = capture.read()

		classIds, confs, bbox = net.detect(img, confThreshold=0.55)

		if len(classIds) != 0:
			for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
				if classNames[classId-1] == 'cat':
					
					# we found a cat, display for 2 seconds and then return true
					cv2.rectangle(img, box, color=(255,0,0), thickness=3)
					cv2.putText(img, classNames[classId-1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0), 2)
					found = True

		cv2.imshow('Output', img)
		cv2.waitKey(1)

if __name__ == "__main__":
	checkForCat()