# Project Title : raspberry Pi is a mask sheriff


# 0. Index

------
# 1. Background, Purpose, and Expected Outcomes
The spread of Corona 19 made it mandatory to wear a mask in public places.
We started to eliminate the trouble between employees and non-masks.
So, We hope that workers' emotional consumption will be less.

![계찰구사진](https://user-images.githubusercontent.com/57394605/97212004-2b93b100-1803-11eb-82e7-813d1f0659eb.png)

------
# 2. Overview


------
# 3. Description


------
# 4. Requirement
## 4-1. Hardware
* raspberry Pi 4 (8GB)
* raspberry Pi camera module v2
* raspberry Pi 7-inch touch screen
* power supply 5V 3~4a
* micro SD card 32GB
* micro SD card Reader
* Device case (SmartPi Touch 2 [SM-STV2])
* SG-90 Servo motor
* Test Socket Jumper Cable(M/F)

<img src="https://user-images.githubusercontent.com/57394605/97400188-05b8fa00-1932-11eb-900d-9abb1ab4906f.png" alt="drawing" width="600">


## 4-2. Environment
* Buster (Release date : 2020-08-20)
* tensorflow 2.2.0
* OpenCV 4.1.2
* numpy
* matplotlib
  
You can use this command. However, Some packages are not registered with pip. It will be imcomplete. So, you can refer to content 5-2.

    $ pip install -r requirements.txt
   
   
------
# 5. Install
## 5-1. Appliance assembly

### Step 1

Route the long end of the white cable under the display board. Attach the long end to the camera as shown. Install the display board onto the display with the supplied gold m3 screws. The standoffs that came with the display can be used to attach HAT boards to the Raspberry Pi.  Attach the short white cable to the display board. Make sure the writing on the cable and blue tab is facing up like the photo.

<img src="https://user-images.githubusercontent.com/57394605/97401836-e2437e80-1934-11eb-94ea-50b6a93bbe97.png" alt="drawing" width="600">


### Step 2

Mount the display into the case as shown and feed the camera and white cables as shown.

<img src="https://user-images.githubusercontent.com/57394605/97401845-e66f9c00-1934-11eb-837e-f6ae1d85c696.png" alt="drawing" width="600">


### Step 3

Screw in the display using the four silver countersink screws.

<img src="https://user-images.githubusercontent.com/57394605/97401859-eb345000-1934-11eb-8094-2719725d116d.png" alt="drawing" width="600">


### Step 4

Attach camera and front panel with six black screws.

<img src="https://user-images.githubusercontent.com/57394605/97401863-ec657d00-1934-11eb-9d0d-0157de7cefeb.png" alt="drawing" width="600">


### Step 5

Connect the cables as shown in the photo. If you connected them as shown in step one, the cable with the writing facing up should connect to the camera slot.

<img src="https://user-images.githubusercontent.com/57394605/97401864-ecfe1380-1934-11eb-9c57-002fc957a4f5.png" alt="drawing" width="600">


### Step 6

Assemble the fan onto the fan door. For best results the label should be facing toward the Raspberry Pi.

<img src="https://user-images.githubusercontent.com/57394605/97401865-ed96aa00-1934-11eb-8204-21068c926576.png" alt="drawing" width="600">


### Step 7

Connect the wire to the GPIO pins. We suggest starting with low speed as it is quieter. If you get the temperature icon in the display, you can always move up to the high speed.

<img src="https://user-images.githubusercontent.com/57394605/97401867-eec7d700-1934-11eb-8745-4cd1cbe1ae85.png" alt="drawing" width="600">


### Step 8

Assemble the door. Be careful not to pinch the white cables.

<img src="https://user-images.githubusercontent.com/57394605/97401869-eec7d700-1934-11eb-8bf3-03ae857a07cc.png" alt="drawing" width="600">


### Step 9

Assemble the housing onto the base. Important - Hold base on table while adjusting the display angle, then tighten the screws.

<img src="https://user-images.githubusercontent.com/57394605/97403769-5df2fa80-1938-11eb-9955-6c6a8ef39284.png" alt="drawing" width="600">

## 5-2. Build a Software Environment
### 1. OS
* Step 1 (Download Raspbian)
<img src="https://user-images.githubusercontent.com/57394605/97530822-45491a00-19f6-11eb-93ad-63f0428c7447.png" alt="drawing" width="600">
hop onto your computer and download the Raspbian disc image. you can find the lastest version of Raspbian on the Raspberry Pi Foundation's website [here](https://www.raspberrypi.org/downloads/raspberry-pi-os/, "Raspbian link").



* Step 2 (Unzip the file)

The Raspbian disc image is compressed, so you’ll need to unzip it. The file uses the ZIP64 format, so depending on how current your built-in utilities are, you need to use certain programs to unzip it. If you have any trouble, try these programs recommended by the Raspberry Pi Foundation
  - Windows users, you'll want 7-Zip.
  - Mac users, The Unarchiver is your best bet.
  - Linux users will use the appropriately named Unzip.
  


* Step 3 (Write the disc image to your microSD card)

Next, pop your microSD card into your computer and write the disc image to it. You’ll need a specific program to do this
  - Windows users, your answer is [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/, "Win32 link").
  - Mac users, you can use the disk utility that’s already on your machine.
  - Linux people, [Etcher](https://www.balena.io/etcher/, "Etcher link") – which also works on Mac and Windows – is what the Raspberry Pi Foundation recommends.
  


* Step 4 (Put the microSD card in your Pi and boot up)

Your default credentials are username **pi** and password **raspberry**.


### 2. SSH & VNC

### 3. Packages


------
# x. Plan for the Publication & Dissemination of Project Results

------
# x. Timeline



--------
### Reference
* https://thepi.io/how-to-install-raspbian-on-the-raspberry-pi/
* https://smarticase.com/pages/smartipi-touch-2-setup-1
* https://qengineering.eu/install-tensorflow-2.1.0-on-raspberry-pi-4.html
* https://webnautes.tistory.com/916
* https://biz.chosun.com/site/data/html_dir/2020/05/13/2020051301479.html
