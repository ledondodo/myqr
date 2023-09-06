import qrcode

def qr_generate(text,file):
	qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_M, # 15% error
			box_size=10,
			border=4
		)
	qr.add_data(text)
	qr.make(fit=True)
	img = qr.make_image(fill_color = 'red', back_color = 'white')
	img.save(file)

file = "myQR.png"
qr_generate(input("Text to QR generate: "),file)
print(f"QR saved as {file}")