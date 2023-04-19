import qrcode

features=qrcode.QRCode(version=1,box_size=40,border=5)

features.add_data('https://www.linkedin.com/in/vedant-gajare-370097264/')
features.make(fit=True)
generate_image = features.make_image(fill_color="blue",black_color="white")
generate_image.save('2.png')
