import pyautogui
import datetime
def take_scrnshot():
    file_name = str(datetime.datetime.now().minute)
    screenshot = pyautogui.screenshot()
    screenshot_path = screenshot.save(f"C:\\Users\\JSP-NogorIT\\PycharmProjects\\AI assistant\\{file_name}.png")
    return

def email_taking_prompt():
    receiver_mail = pyautogui.prompt(text='', title='Type the receiver email address..', default='')
    return receiver_mail


