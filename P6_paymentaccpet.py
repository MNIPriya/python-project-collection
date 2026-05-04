import qrcode
#taking UPi id as input 
upi_id = input("enter your Upi id = ")
#upi:/pay?pa = UPI_ID&apn=Name&am=Amount&cu=currency&tr=Message
#defining The payment URL based on the upi id

phonepe_url = f'upi://pay?pa ={upi_id}&pn=Recipient%20Name&mc=1234'
pytm_url = f'upi://pay?pa ={upi_id}&pn=Recipient%20Name&mc=1234'
gpay_url = f'upi://pay?pa ={upi_id}&pn=Recipient%20Name&mc=1234'
#create qr code for each payment app 
phonepe_qr = qrcode.make(phonepe_url)
pytm_qr = qrcode.make(pytm_url)
gpay_qr = qrcode.make(gpay_url)
#save the QR code
phonepe_qr.save('phonepe_qr.png')
pytm_qr.save('pytm_qr.png')
gpay_qr.save('gpay_qr.png')

#display the qr code
phonepe_qr.show()
pytm_qr.show()
gpay_qr.show()