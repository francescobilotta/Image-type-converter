from PIL import Image
import glob

print(glob.glob("*.png"))

for file in glob.glob("../images-working-folder/*.png"):
    im = Image.open(file)
    #rgb_im = im.convert('RGB') #for jpg
    #rgb_im.save(file.replace("png", "jpg"), quality=95) #for jpg
    im.save(file.replace("png", "webp"), format="webp")

