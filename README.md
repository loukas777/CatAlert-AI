# CatAlert-AI

The CatAlert-AI is a program that detects the presence of cats in a live video through the Jetson detectNet network.

##Purpose

This program is originally meant to keep cats out of your garden by sending the resident/user a notification saying a cat is in their garden. But
it can also be used for other intentions.

##The Algorithm

First it imports all the necessary tools:
![image](https://user-images.githubusercontent.com/110618644/183097777-490d470d-1775-4313-9c52-eb216b708de5.png)

Then it prepares for the live video feed by setting up detectNet and setting the video source (the camera). Additionally, it makes sure the video is saved as a file once it ends and names it. Plus, the sound file is defined: 
![image](https://user-images.githubusercontent.com/110618644/183097456-81e58c42-1c41-4ba6-81fb-f4263eefc92c.png)

Here it runs a live video feed. It tells the camera to capture, detect, and displays images:
![image](https://user-images.githubusercontent.com/110618644/183099735-a6d2bb96-9e54-425f-b524-40b9eab0a82a.png)

Still in the while loop (during the live feed), the program goes through all the objects it detects and gets their descriptions and prints them:
![image](https://user-images.githubusercontent.com/110618644/183100684-13628465-f5bc-466e-b0cb-f156b488c5c5.png)

Still in the for loop (going through the detected objects), it asks if an object's string (description/name) is "cat". If it is, it prints a statement and plays the defined sound file:

          
Steps:  1.  ssh into your nano;
        2.  Upload the script;
        3.  Set up your camera wherever you want to know when a cat's there;
        4.  Run the script
