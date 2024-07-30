import qrcode

# Get data from the user
data = input("Enter the data you want to encode in the QR code: ")

# Creating an instance of QRCode
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
    box_size=10,  # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes thick the border should be (the default is 4)
)

# Add data to the instance
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save it to a file
filename = "generated_qr.png"
img.save(filename)

print(f"QR code generated and saved as {filename}")
