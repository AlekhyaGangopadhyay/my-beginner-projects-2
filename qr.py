import qrcode
def generateqr(text):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color='black',back_color='white')
    img.save('op.png')
url=input('Bijayee bhava parth')
generateqr(url)
