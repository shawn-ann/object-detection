import util.img_recognizer as ImageRecognizer


#方向键坐标
direction_recognizer = ImageRecognizer(debug=False)
direction_position = direction_recognizer.find_image_location('temp/screenshot.png', 'img/direction_icon.png')


