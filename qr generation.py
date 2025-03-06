'''import qrcode 

qr = qrcode.make("Hey baby")

qr.save("myqr.png")

print("QR created successfully")'''

import qrcode

# Create a QRCode object with better settings
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
    box_size=10,
    border=4,
)

# Add data
qr.add_data("Hey baby, I Love you sm <3")
qr.make(fit=True)

# Create an image
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("myqr.png")

print("QR created successfully")
