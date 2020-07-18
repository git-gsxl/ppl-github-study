''' 解析验证码 '''
from PIL import Image           # 安装：Pioolw 库
import pytesseract              # 安装: pytesseract 库

image = Image.open('G:\\project_lyl\\study_day\\selenium_day\\muke\\1img.png')
text = pytesseract.image_to_string(image)
print(text)

'''
需第三方库收费的api进行图片识别
'''
