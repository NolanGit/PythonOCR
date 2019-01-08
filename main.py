from PIL import Image
import pytesseract
#上面都是导包，只需要下面这一行就能实现图片文字识别
text=pytesseract.image_to_string(Image.open('C:/Users/shr12/Documents/Github/PythonOCR/mjorcen.normal.exp0.jpg'),lang='chi_sim')
print(text)
