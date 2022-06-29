# OtaMultiUpdate

It's simple updater using (file.txt) the ip-adress list's.
All creates from one file .BIN ,adds  automatic next module name and uploads to the targets. 
This project can help you transfer the updates (no uart programmer) to thirty devices (ESP8266) in mine Compact Miner board.
Multi update at today it's quick and simple.
He Using PySimpleGui  for Graphic interface and espota.py (python ota commandline uploader) 
from:https://github.com/esp8266/Arduino/blob/master/tools/espota.py.
! WARNING! epota.py must must be next to OtaMultiUpdate.exe.
<br>
<br>
<br>
<b>GUI Style:</b>
![OTA UPDATER](https://user-images.githubusercontent.com/24864691/139673991-91cc3be2-51f0-4acc-b9c7-33ca461b6208.png)
![GUI_OTA](https://user-images.githubusercontent.com/24864691/139674038-dfb62d2d-2288-48d4-8ad9-1a8311c110db.png)  
<br>
<br>
<br>
How to use this:
1) Prepare arduino .bin files for OTA multi uploader:
![prepare](https://user-images.githubusercontent.com/24864691/139676054-eae22c08-3590-4db7-9edb-93fbc33c45f9.png)
After completing the .ino file, click on sketch -> export of the compiled program.
That's all your .BIN file for OtaMultiUploader.

2) Create your .txt (Internet Protocol list) file with your thirty devices adresses.

IP List Structure:

![OTA_IP_List_Structure](https://user-images.githubusercontent.com/24864691/139674993-27410fde-e140-4847-978c-136bdfd68f1f.png)
3) Give all files and click button "upload":
Your status in command prompt or the progress bar:


Thanks for using!  
<br>
<br>
<br>
Compact Miner generates some image and renders it: 

![Miner_Layer_A](https://user-images.githubusercontent.com/24864691/139735332-4e6abdec-339e-4197-8d83-5a85cce45a36.png)
![Miner_Layer_B](https://user-images.githubusercontent.com/24864691/139735383-3f151f10-dded-405a-a55f-82d2b47a529a.png)
![IMG_20211017_203918](https://user-images.githubusercontent.com/24864691/139735367-ee4ff7c0-6b5d-496b-930c-6e0c8cfe04f5.jpg)
