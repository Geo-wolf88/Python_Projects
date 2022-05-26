import qrcode


img = qrcode.make ('https://www.youtube.com/watch?v=04854XqcfCY')
img.save('myQRcode.png')
img.show()


