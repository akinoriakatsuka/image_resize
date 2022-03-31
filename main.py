from PIL import Image
from io import BytesIO
import os
import glob

COMPRESS_QUALITY = 30 # 圧縮のクオリティ

image_files = glob.glob("./original_images/**/*.*" , recursive=True)

for imagefile in image_files:
  dir_name = os.path.dirname(imagefile).strip("./original_images")
  os.makedirs('comp_images/' + dir_name ,exist_ok=True)
  file_name, ext = os.path.splitext(os.path.basename(imagefile))
  print(imagefile)
  if(ext == ".jpeg" or ext == ".jpg" or ext == ".JPG" or ext == ".JPEG"):
    with open(imagefile, 'rb') as inputfile:
      im = Image.open(inputfile)
      im_io = BytesIO()
      im.save(im_io, 'JPEG', quality = COMPRESS_QUALITY)
    with open('comp_images/' + dir_name + '/' + file_name + '.jpg', mode='wb') as outputfile:
      outputfile.write(im_io.getvalue())
  elif ( ext == ".png" ): 
    with open(imagefile, 'rb') as inputfile:
      im = Image.open(inputfile)
      im_io = BytesIO()
      im.save(im_io, 'PNG', quality = COMPRESS_QUALITY)
    with open('comp_images/' + dir_name + '/' + file_name + '.png', mode='wb') as outputfile:
      outputfile.write(im_io.getvalue())
  else:
    with open('comp_images/' + dir_name + '/' + file_name + ext, mode='wb') as outputfile:
      outputfile.write(im_io.getvalue())