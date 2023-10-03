import qrcode
import os

user_name = os.getlogin()

# Declara la variable para almacenar la URL de la página web
url = input(f"Buen día, {user_name}. Introduce la URL de la página web: ")

# Crea un objeto QRCode con la URL como información
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Establece las opciones de personalización del QR
qr.add_data(url)
qr.make(fit=True)

# Guarda el QR como una imagen en el mismo lugar donde se ejecutó el programa
img = qr.make_image()
img.save("QRInstant.png")

print(f"{user_name}, su código QR ha sido creado exitosamente.")
input("Gracias por usar QRInstant, </BranDev>")
input("Presione ENTER para salir")

#python -m PyInstaller --onefile --icon="QRInstant.ico" QRInstant.py