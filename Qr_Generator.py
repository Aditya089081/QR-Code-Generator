# code to get qr code in this repeal by using qrcode module
# import qrcode as Aditya
# img = Aditya.make("https://www.hackerrank.com/dashboard")
# img.save("Aditya_HackerRank_Performance.png")



import qrcode as Aditya
from PIL import Image

qr = Aditya.QRCcode(version = 1,
                   error_correction=Aditya.constants.ERROR_CORRECT_H,
                   box_size = 10, border = 4)
qr.add_data("https://www.hackerrank.com/dashboard")
qr.make(fit=True)
img = qr.make_image(fill_color = "Black",back_color="White")
img.save("Adity_HackerRank.png")
