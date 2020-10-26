from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
import random
import string

image = ImageCaptcha()
code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
image.generate(code)
image.write(code, 'code.png')

