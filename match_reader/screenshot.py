#-- include('examples/showgrabfullscreen.py') --#
import pyscreenshot as ImageGrab

if __name__ == '__main__':

    # grab fullscreen
    im = ImageGrab.grab()

    # save image file
    im.save('screenshot.png')

#-#