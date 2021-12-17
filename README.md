# OtaMultiUpdate

It's simple gui OTA Multi Uploader from .txt ip-adress list's.

I'm Using PySimpleGui and espota.py (python ota commandline uplader) from : https://github.com/esp8266/Arduino/blob/master/tools/espota.py.

!WARNING! epota.py must must be next to  OtaMultiUpdate.exe .

GUI Style : 

![OTA UPDATER](https://user-images.githubusercontent.com/24864691/139673991-91cc3be2-51f0-4acc-b9c7-33ca461b6208.png)

![GUI_OTA](https://user-images.githubusercontent.com/24864691/139674038-dfb62d2d-2288-48d4-8ad9-1a8311c110db.png)


How to use this :

1) Prepare arduino .bin files for OTA multi uploader :

![prepare](https://user-images.githubusercontent.com/24864691/139676054-eae22c08-3590-4db7-9edb-93fbc33c45f9.png)

After completing the .ino file, click on sketch -> export of the compiled program.
That's all your .BIN file for OtaMultiUploader


2) Create your .txt IP_list file with your module 30's adress

IP List Structure :

![OTA_IP_List_Structure](https://user-images.githubusercontent.com/24864691/139674993-27410fde-e140-4847-978c-136bdfd68f1f.png)


3) Give all files and Upload :

Upload status in command prompt or progress bar.


Thanks for using ! 














