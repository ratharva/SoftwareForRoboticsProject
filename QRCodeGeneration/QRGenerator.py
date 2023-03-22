import qrcode
import uuid

myDat = "Robot_" + str(uuid.uuid4())

myQrImage = qrcode.make(myDat)

myQrImage.save("./TempQr.png")
