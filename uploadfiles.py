import dropbox
class TransferData:
    def __init__(self,access_token):
         self.access_token = access_token
         
    def upload_Files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = "sl.AxPBhZkG6iGfh880FE_pZ7psd7UTSpXEl9EM4cfx_YC2l36XPmNS50VQ37B26w9TcO_z0Y2xzmz-a8y_E1DPFaEWzyUP3Q6LlSpD5Km9r8fwRvCmzxqgDiVJ5M6frR1PPSe3oCZ-0970"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transefer: ")
    file_to = input("Enter the full file path to upload to dropbox: ")

    transferData.upload_Files(file_from,file_to)
    print("File has been moved succesfully")

main()
