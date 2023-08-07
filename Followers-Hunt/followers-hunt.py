import time
import pyautogui


time.sleep(3)
pyautogui.hotkey('alt', 'tab')
pyautogui.moveTo(x=1005, y=76, duration=2)
pyautogui.click()
##opening Like4like
time.sleep(3)
pyautogui.typewrite('like4like.org')
pyautogui.hotkey('enter')
time.sleep(2)
####Free credits#####
pyautogui.moveTo(x=1065, y=140)
time.sleep(1)
####Method = Twitter Followers ###
pyautogui.click(x=907, y=626, duration=2)
time.sleep(3)
 
###TwitterFollowers
for _ in range(10):
 ###Position 1###
 ###PageFollow Button 1###
 pyautogui.click(x=537, y=878, duration=1)
 time.sleep(8)
 ###AccFollow Button 1###
 pyautogui.click(x=1022, y=631, duration=1)
 time.sleep(1)
 ###closing unnecessary tab
 pyautogui.click(x=1459, y=75, duration=2)
 time.sleep(2)
 ###Confirm Points
 pyautogui.moveTo(x=527, y=827,  duration=1)
 pyautogui.click(x=527, y=827)
 time.sleep(3)
 ###Position 2 
 ###PageFollow Button 2###
 pyautogui.click(x=841, y=885)
 time.sleep(8)
 ###AccFollow Button 2###
 pyautogui.click(x=1022, y=631, duration=1)
 time.sleep(1)
 ###Close tab
 pyautogui.click(x=1459, y=75, duration=2)
 ###Confirm Points
 pyautogui.moveTo(x=855, y=824,  duration=1)
 pyautogui.click(x=855, y=824)
 time.sleep(3)


#####Twitter Likes
for _ in range(10):
####Free credits#####
 pyautogui.moveTo(x=1065, y=140)
 time.sleep(1)

####Method = Twitter Likes ###
 pyautogui.click(x=876, y=725, duration=2)
 time.sleep(3)
###Position 1###
###PostLike Button 1###
 pyautogui.click(x=537, y=878, duration=1)
 time.sleep(8)
###PostLike Button 1###
 pyautogui.typewrite('l')
 time.sleep(1)
###closing unnecessary tab
 pyautogui.click(x=1459, y=75, duration=2)
 time.sleep(2)
###Confirm Points
 pyautogui.moveTo(x=527, y=827,  duration=1)
 pyautogui.click(x=527, y=827)
 time.sleep(3)
###Position 2 
###PageLike Button 2###
 pyautogui.click(x=841, y=885)
 time.sleep(8)
###PostLike Button 2###
 pyautogui.typewrite('l')
 time.sleep(1)
###Close tab
 pyautogui.click(x=1459, y=75, duration=2)
###Confirm Points
 pyautogui.moveTo(x=855, y=824,  duration=1)
 pyautogui.click(x=855, y=824)
 time.sleep(3)


####TikTok Likes
for _ in range(10):
####Free credits#####
 pyautogui.moveTo(x=1065, y=140)
 time.sleep(1)

####Method = TikTok Likes ###
 pyautogui.click(x=1203, y=455, duration=2)
 time.sleep(3)
 ###Position 1###
###PostLike Button 1###
 pyautogui.click(x=537, y=878, duration=1)
 time.sleep(8)
 ###PostLike Button 1###
 pyautogui.click(x=1000, y=569, clicks=2)
 time.sleep(1)
###closing unnecessary tab
 pyautogui.click(x=1459, y=75, duration=2)
 time.sleep(2)
###Confirm Points
 pyautogui.moveTo(x=527, y=827,  duration=1)
 pyautogui.click(x=527, y=827)
 time.sleep(3)
###Position 2 
###PageLike Button 2###
 pyautogui.click(x=841, y=885)
 time.sleep(8)
###PostLike Button 2###
 pyautogui.click(x=1000, y=569, clicks=2)
 time.sleep(1)
###Close tab
 pyautogui.click(x=1459, y=75, duration=2)
###Confirm Points
 pyautogui.moveTo(x=855, y=824,  duration=1)
 pyautogui.click(x=855, y=824)
 time.sleep(3)
