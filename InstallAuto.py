import pyautogui
import time

# User manual:
# left side you need to set up config file folder half of your.
# right side you need to set ut your remote dekstop program.
# you need to configure "pyautogui.moveTo" commands bacouse of coursor need to click in the programs.
# import pyautogui # pyautogui.displayMousePosition() separeted py cmd bacouse need to know where are your corsor

pyautogui.size()
(1920, 1080)
pyautogui.PAUSE = 2 # scrip veldig rask for gui kan følge derfor etter hver call 2sec sleep

### Variables you need to configure ###

folderY = 177 ; folderX = 560  # kanskje du trenger configurerer click in folder
rdmY =880     ; rdmX =  880 # kanskje du trenger configurerer click in RDM
vmY = 1350    ; vmX = 670   # kanskje du trenger configurerer click in Virtual machine
Password = 'XXXXXXXXXX' # ditt remote desktop passord (PAM passord) er kreves her pga. log in.

### Variables you need to configure ###

def install(ServerNameInRDM, ServerConfigFolderName):
#----folder left side----
 pyautogui.moveTo(folderY, folderX)
 pyautogui.click()
 pyautogui.hotkey('ctrl', 'f')
 pyautogui.typewrite(ServerConfigFolderName) # ServerConfigFolderName variable
 pyautogui.press(['down'])
 pyautogui.press(['down'])
 pyautogui.press(['enter'])
 time.sleep(3)
 pyautogui.hotkey('ctrl', 'a')
 pyautogui.hotkey('ctrl', 'c')
 pyautogui.hotkey('alt', 'f4')
 pyautogui.press(['backspace'])
 # -----remote desktop manager right side----
 pyautogui.moveTo(rdmY, rdmX)
 pyautogui.click()
 pyautogui.hotkey('ctrl', 'f')
 pyautogui.typewrite(ServerNameInRDM) # ServerNameInRDM variable
 pyautogui.press(['enter'])
 time.sleep(10)
 pyautogui.typewrite(Password) #passordet ditt
 pyautogui.press(['enter'])
 time.sleep(10)
 pyautogui.typewrite('cd /etc')
 pyautogui.press(['enter'])
 time.sleep(5)
 pyautogui.typewrite('sudo curl -L -O https://artifacts.elastic.co/.../heartbeat-6.8.12-x86_64.rpm')
 pyautogui.press(['enter'])
 time.sleep(25)
 pyautogui.typewrite('sudo rpm -vi heartbeat-6.8.12-x86_64.rpm')
 pyautogui.press(['enter'])
 time.sleep(15)
 pyautogui.typewrite('sudo vi /etc/heartbeat/heartbeat.yml')
 pyautogui.press(['enter'])
 time.sleep(5)
 pyautogui.press(['enter'])
 pyautogui.press('d', presses=500)
 pyautogui.press('d', presses=500)
 time.sleep(15)
 pyautogui.typewrite('i')
 time.sleep(5)
 pyautogui.moveTo(vmY, vmX)
 pyautogui.rightClick()     #past in config text
 time.sleep(5)
 pyautogui.press('esc')
 pyautogui.typewrite(':wq')
 pyautogui.press(['enter'])
 pyautogui.typewrite('sudo heartbeat -c /etc/heartbeat/heartbeat.yml test config')
 pyautogui.press(['enter'])
 time.sleep(5)
 pyautogui.typewrite('sudo systemctl enable heartbeat')
 pyautogui.press(['enter'])
 pyautogui.typewrite('sudo systemctl start heartbeat')
 pyautogui.press(['enter'])
 pyautogui.hotkey('alt', 'f4')
 pyautogui.press(['enter'])
 # -----Test---------
install('ServerName', 'ConfigífolderName')