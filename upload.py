import cv2
import dropbox
import time
import random
start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)

    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        img_name = 'img'+str(number)+'.png'

        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print('snapshot taken')
    videocaptureobject.release()
    cv2.destroyallwindows()
take_snapshot()
def upload_file(img_name):
    access_token = 'sl.BHX-7p4U5VUt48wLpdHlZOhSIT_IeB8ouC5Zb36Ecr4XqfjksqYdee-54JMAUoM9hTiKDUnG73fdB85A43_yqv63UoGKl1GW0IYJCSWQ7KABFKstiYGinrQJO-dv_ayOOPyG0thyR7t6'
    file = img_name
    file_from = file
    file_to = "/testfolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()