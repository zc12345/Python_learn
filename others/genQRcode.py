import qrcode
import image
import matplotlib.pyplot as plt
from os.path import exists
from PIL import Image

def show_qr(file):
    if exists(file):
        img = Image.open(file)
        plt.imshow(img)
        plt.show()

def default_qrgen(msg, path):
    '''
    default QRcode generating method
    :param msg: message
    :param path: save oath
    :return: None
    '''
    img = qrcode.make(msg)
    img.save(path)

if __name__ == "__main__":
    msg = 'hello world'
    target_path = 'test.png'
    #default_qrgen(msg, target_path)
    #show_qr(target_path)