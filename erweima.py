# from MyQR import myqr
# myqr.run(words='{"name":"F4:EB:81:BE:58:9C", "MAC":"F4:EB:81:BE:58:9C"}',picture='1.jpg')
import qrcode
qr = qrcode.QRCode(
        version = 7,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
def chage(data):
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('./__pycache__/'+'1.png')
# data = '{"name":"F4:EB:81:BE:58:9C", "MAC":"F4:EB:81:BE:58:9C"}'
# qr.add_data(data)
# qr.make( fit=True)
# img = qr.make_image()
# img.save('1.png')

# data = '{"name":"F4:EB:81:BE:58:9C", "MAC":"F4:EB:81:BE:58:9C"}'
# img_file = r'./1.png'
# img = qrcode.make(data)
# img.save(img_file)
# img.show()
