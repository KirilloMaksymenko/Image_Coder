import random
from PIL import Image
import PySimpleGUI as sg

def GUI_layout():
    # First the window layout in 2 columns

    file_list_column = [
        [
            sg.Text("Image Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]

    # For now will only show the name of the file that was chosen
    image_viewer_column = [
        [sg.Text("Choose an image from list on left:")],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Image(key="-IMAGE-")],
    ]

    # ----- Full layout -----
    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column),
        ]
    ]

    window = sg.Window("Image Viewer", layout)

    # Run the Event Loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Folder name was filled in, make a list of files in the folder
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith((".png", ".gif"))
            ]
            window["-FILE LIST-"].update(fnames)
        elif event == "-FILE LIST-":  # A file was chosen from the listbox
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                window["-TOUT-"].update(filename)
                window["-IMAGE-"].update(filename=filename)

            except:
                pass

    window.close()


def coding_img(path,txt,txt_seed):
	im = Image.open(path)

	data = []
	random.seed(create_seed(txt_seed))
	num = 0
	if im.height > im.width:
		num = im.width
	else:
		num = im.height

	for lt in txt:
		rn = random.randint(0,num)

		while rn in data:
			rn = random.randint(0,num)

		#print(rn)
		r2,g2,b2=0,0,0
		(r2,g2,b2) = im.getpixel((rn,rn))
		im.putpixel((rn, rn),( r2, g2, ord(lt)))

		
	rn = random.randint(0,num)
	while rn in data:
			rn = random.randint(0,num)

	r2,g2,b2=0,0,0
	(r2,g2,b2) = im.getpixel((rn,rn))
	im.putpixel((rn, rn),( 127, 127, 127))
	
	im.show()
	im.save("im_1.bmp")

def decode_img(path,txt_seed):
	im = Image.open(path)

	text = ""
	data = []
	random.seed(create_seed(txt_seed))
	num = 0
	if im.height > im.width:
		num = im.width
	else:
		num = im.height

	while True:
		rn = random.randint(0,num)

		while rn in data:
			rn = random.randint(0,num)

		#
		print(rn)
		r2,g2,b2=0,0,0
		(r2,g2,b2) = im.getpixel((rn,rn))

		if (r2,g2,b2) == (127,127,127): break
		text = text + chr(b2)
	return text

def create_seed(txt):
	seed_num = 0
	for t in txt:
		seed_num = (seed_num * 10000) + (ord(t) * 2)
	return seed_num



def main():
    GUI_layout()
	#print("You have to entre path absolutle or take img in folders with this program and enter name img")
	#if input("1.Coder 2.Decoder : ") == 1:
	#	coding_img(input("Path: "),"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lining Lorem Ipsum passage","кир")
	#else:
	#	print(decode_img(input("Path: "),"кир"))
	

if __name__ == '__main__':
	main()