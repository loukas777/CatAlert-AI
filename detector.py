#!/usr/bin/python3

#import stuff I need
import jetson.inference
import jetson.utils
from playsound import playsound

#Set everything up
net = jetson.inference.detectNet("ssd-mobilenet-v2",threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput("file://cat_video.mp4")
mp3file = "Thundersound.mp3"

#Run the live stream
while True:
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS())) 

	#Get ClassID for the objects
	for detection in detections:
		class_idx = detection.ClassID 
		class_desc = net.GetClassDesc(class_idx)
		print(class_desc)

		#React if ClassID is that of a cat
		if class_desc == str("cat"):
			print("THERE IS A CAT!")
			playsound(mp3file)
