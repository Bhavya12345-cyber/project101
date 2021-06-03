import dropbox
class TransferData:
    def __init__ (self,accessToken):
        self.accessToken = accessToken

    def uploadfile(self,filefrom,fileDestination):
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(filefrom,'rb')

        dbx.files_upload(f.read(),fileDestination)

def main():
    accessToken = "4aJnPcGsMK0AAAAAAAAAAUZANWPhlJrKWpd2RdWPNw9_jpzPq9nP9o7z8LsM7sb-"
    #creating an object of the class TransferData
    tf = TransferData(accessToken)

    sourceFile = input("transfer the file: ")
    destFile = input("enter the path of the file: ")
    
    tf.uploadfile(sourceFile,destFile)
    print("the file has reachd the destination !!!")

main()