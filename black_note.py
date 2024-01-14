from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


# root = Tk()
#
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
#
# root.geometry(f'{screen_width}x{screen_height}')

class VidPlayer(Tk):
    def main_screen(self) -> None:
        """" Getting our screen size """
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        """ Setting screen size """
        self.geometry(f'{self.screen_width}x{self.screen_height}')

        """ VidPlayer title """
        self.title('VidPlayer')

        """ VidPlayer background  """  # TODO making changeable image on bg
        self.path = 'images/background_image/wallpaperflare.com_wallpaper.jpg'
        self.canvas = Canvas(self, height=self.screen_height, width=self.screen_width, highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        """ Introducing Screen Content """
        self.screen_content()

        self.bind('<Configure>', self.resizer)

    """ Screen Content """
    def screen_content(self) -> None:
        width = 700
        height = 350
        x = (self.screen_width / 2) - (width / 2)
        y = (self.screen_height / 2) - (height / 1.5)
        self.canvas.create_rectangle(x, y, x + width, y + height, fill='gray', outline='gray')
        self.canvas.pack()

    """ Resizing stuff """
    def resizer(self, obj):
        global bg, resized_bg, bg_image
        bg = Image.open(self.path)
        resized_bg = bg.resize((obj.width, obj.height), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(resized_bg)
        self.canvas.create_image(0, 0, anchor=NW, image=bg_image)



if __name__ == '__main__':
    """ Creating an instance of our class """
    start_player = VidPlayer()

    """ Starting our app """
    start_player.main_screen()
    start_player.mainloop()
