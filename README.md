# cvzoneUsingPIcamera

I have been following https://www.kevsrobots.com/ , in particular his "MASTERING POSTURE DETECTION WITH CVZONE".

Tried getting his example to work on my PI5 and it did not. Eventually I watched the video and realised Kevin was using a web camera, I was using
a PI camera on a PI5 using 64 bit Raspberry PI OS. ( I can't get cvzone to install on 32 bit OS, do not know why)

I eventually realised I had to use the Picamera2 library, this reads an image, (on my set up anyway) as 4 channels, alpha and RGB not 3 channels of RGB.

This means the image has to be converted to RGB using cv2.cvtColor .

It works, thanks Kevin for a great tutorial, I was not aware of cvzone until I saw your post

