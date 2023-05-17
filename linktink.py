import ctypes

directory = "c:\CuratedWallpaper"
imagePath = directory + "\Mario.bmp"

def changeBG(imagePath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imagePath , 0)
    return;

changeBG(imagePath)
