import qrcode
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=2.5
)
qr.add_data("Targeted url") #Like My facebook profile link
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("Advanced.png")   #Save the qr named Advanced.png image 