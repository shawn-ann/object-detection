import subprocess
import time
from util.img_recognizer import ImageRecognizer

screen_width = 1080
screen_height = 2240
ppi = 408

def get_connected_devices():
    devices = subprocess.check_output(['adb', 'devices']).decode('utf-8').split('\n')[1:]
    connected_devices = [device.split('\t')[0] for device in devices if device.strip() != '']
    return connected_devices

def connect_to_first_device():
    devices = get_connected_devices()
    if devices:
        subprocess.run(['adb', 'connect', devices[0]])

def execute_adb_command(command):
    subprocess.run(['adb', 'shell'] + command)


def take_screenshot():
    file_path="./temp/screenshot.png"
    subprocess.run(['adb', 'shell', 'screencap', '-p', '/sdcard/screenshot.png'])
    subprocess.run(['adb', 'pull', '/sdcard/screenshot.png', file_path])
    return file_path

def pixel_to_coordinate(pixel_x, pixel_y):
    # 计算屏幕的物理尺寸（单位：英寸）
    screen_width_inches = screen_width / ppi
    screen_height_inches = screen_height / ppi

    # 计算每英寸的像素数
    pixels_per_inch_x = screen_width / screen_width_inches
    pixels_per_inch_y = screen_height / screen_height_inches

    # 计算真实坐标
    coordinate_x = int(pixel_x * (pixels_per_inch_x / ppi))
    coordinate_y = int(pixel_y * (pixels_per_inch_y / ppi))

    return coordinate_x, coordinate_y


def tap_screen(x, y):
    execute_adb_command(['input', 'tap', str(x), str(y)])

def press_and_hold(x, y):
    execute_adb_command(['input', 'touchscreen', 'down', str(x), str(y)])

def swipe_screen(x_start, y_start, x_end, y_end, duration):
    execute_adb_command(['input', 'swipe', str(x_start), str(y_start), str(x_end), str(y_end), str(duration)])

# 示例用法
# connect_to_first_device()
# take_screenshot()
# #方向键坐标
# direction_recognizer = ImageRecognizer(debug=False)
# direction_position = direction_recognizer.find_image_location('temp/screenshot.png', 'img/direction_icon.png')
# center_x, center_y = direction_position
#
# tap_screen(center_x, center_y)


# 使用示例
recognizer = ImageRecognizer(debug=True)
center = recognizer.find_image_location('temp/screenshot.png', 'img/direction_icon.png')

if center:
    center_x, center_y = center
    print(f"识别出的位置中心点坐标为：({center_x}, {center_y})")



# pixel_x=285
# pixel_y=259
# # 调用函数进行转换
# coordinate_x, coordinate_y = pixel_to_coordinate(pixel_x, pixel_y)
# print(f"屏幕坐标为：({coordinate_x}, {coordinate_y})")
# time.sleep(1)
# press_and_hold(300, 300)
# time.sleep(2)
# swipe_screen(100, 100, 500, 500, 1000)