import pyautogui
import time 
import random
import string

pyautogui.FAILSAFE = True


BANNER = """
___________.__ __      __          __    
\\__    ___/|__|  | ___/  |_  ____ |  | __
  |    |   |  |  |/ /\\   __\\/  _ \\|  |/ /
  |    |   |  |    <  |  | (  <_> )    < 
  |____|   |__|__|_ \\ |__|  \\____/|__|_ \\
                   \\/                  \\/
                   
___________.__                         .__           .__       .___
\\__    ___/|  |_________   ____   _____|  |__   ____ |  |    __| _/
  |    |   |  |  \\_  __ \\_/ __ \\ /  ___/  |  \\ /  _ \\|  |   / __ | 
  |    |   |   Y  \\  | \\/\\  ___/ \\___ \\|   Y  (  <_> )  |__/ /_/ | 
  |____|   |___|  /__|    \\___  >____  >___|  /\\____/|____/\\____ | 
                \\/            \\/     \\/     \\/                  \\/

>>> V1.0

"""

print(BANNER)
time.sleep(2)


"""
    Documentation

    Get info
    >>> pyautogui.position()  # current mouse x and y
    >>> pyautogui.size()  # current screen resolution width and height
    >>> pyautogui.onScreen(x, y)  # True if x & y are within the screen.

    Stop the app
    >>> pyautogui.FAILSAFE = True # Stop the program

    Clicks
    >>> pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
    >>> pyautogui.rightClick(x=moveToX, y=moveToY)
    >>> pyautogui.middleClick(x=moveToX, y=moveToY)
    >>> pyautogui.doubleClick(x=moveToX, y=moveToY)
    >>> pyautogui.tripleClick(x=moveToX, y=moveToY)

    >>> pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
    >>> pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')

    Scroll
    >>> pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)

    Keyboard functions
    >>> pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter

    A list of key names can be passed too:
    >>> pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)

    Hotkeys
    >>> pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
    >>> pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste

    >>> pyautogui.keyDown(key_name)
    >>> pyautogui.keyUp(key_name)

    Message Box Functions
    >>> pyautogui.alert('This displays some text with an OK button.')
    >>> pyautogui.confirm('This displays text and has an OK and Cancel button.')
    >>> pyautogui.prompt('This lets the user type in a string and press OK.')

    Locate On Screen
    >>> pyautogui.locateOnScreen('looksLikeThis.png')  # returns (left, top, width, height) of first place it is found



"""


def click_btn(btn_name, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            button_location = pyautogui.locateOnScreen(
            btn_name, 
            grayscale = False, 
            confidence = .75)
        except BaseException:
            print(f"Button '{btn_name}' not found yet...")
            time.sleep(1)
            continue
        print(f"Button '{btn_name}' found at:", button_location)
        button_center = pyautogui.center(button_location)
        time.sleep(1)
        pyautogui.click(button_center)
        return True

    print(f"Timeout reached. Button '{btn_name}' not found.")
    return False

def wait(image_name, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            pyautogui.locateOnScreen(image_name)
            print(f"Image '{image_name}' found!")
        except BaseException:
            print(f"Image '{image_name}' not found yet...")
            time.sleep(1)
            continue
        return True

    print(f"Timeout reached. Image '{image_name}' not found.")
    return False

def write(txt):
    time.sleep(1)
    pyautogui.typewrite(txt, interval=.05)

def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    domain = "utmn"
    tld = "shop"
    return f"{username}@{domain}.{tld}"

def generate_password(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def enter():
    pyautogui.hotkey('enter')

def switch_window():
    pyautogui.hotkey('alt', 'tab')

def tab():
    pyautogui.hotkey('tab')
    
def check_button_exists(button_image_path):
    try:
        x = pyautogui.locateOnScreen(button_image_path)
        return True
    except:
        return False

# def captcha_detected():
#     try:
#         cp = pyautogui.locateOnScreen('captcha.png')
#         return True
#     except: return False

def main():
    # to do (connect to tunnelbear)
    click_btn('tunnelbear.png')
    click_btn('tunnelbear-on.png')
    wait('vpn-connected.png')
    # to do (connect to tunnelbear)

    # to do (create new profile on vision)
    click_btn('vision.png')
    click_btn('create-profile-1.png')
    time.sleep(.5)

    email = generate_email()
    password = f'@0xff{generate_password()}X'

    write(email)
    click_btn('smart-btn.png')
    pyautogui.move(-500, 300)
    pyautogui.scroll(-400)
    time.sleep(.5)
    click_btn('create-profile-2.png')
    # to do (create new profile on vision)

    # to do (create shopify account)
    pyautogui.move(10, 10)
    click_btn('start-profile.png')
    wait('google.png')
    time.sleep(.3)
    pyautogui.hotkey('win', 'up')
    time.sleep(1)
    SHOPIFY_URL = 'https://shopify.com/'
    write(SHOPIFY_URL)
    enter()
    time.sleep(3)
    click_btn('start-free-trial.png')
    while 1:
        if (check_button_exists('checkbox.png')):
            click_btn('checkbox.png')
            continue
        if (check_button_exists('skip-all.png')):
            click_btn('skip-all.png')
            break
        time.sleep(1)
    # to do (create shopify account)


    # to do (create tiktok account)
        #
    # to do (create tiktok account)

    pass

if __name__ == '__main__':
    main()