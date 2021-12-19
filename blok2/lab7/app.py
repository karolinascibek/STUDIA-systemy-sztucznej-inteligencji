from tkinter import *
from tkinter import ttk
from blok2.lab7.hopfield_network import HopfieldNetwork
import copy



def set_size_bitmap(w, k):
    bitmap = []
    for i in range(w):
        bitmap_row = []
        for j in range(k):
            bitmap_row.append(0)
        bitmap.append(bitmap_row)
    return bitmap


def click_item_on_listbox(event):
    idx = event.widget.curselection()[0]
    window_bitmap = Tk()
    canvas_bitmap = Canvas(window_bitmap, bg="white", width=canvas_width, height=canvas_height, bd=0, highlightthickness=0,
                    relief=GROOVE)
    canvas_bitmap.pack()
    dispaly_on_canvas(BITMAPS[idx], canvas_bitmap)


def calculate_position_for_square(event):
    x_start = int(event.x / piksel)*piksel
    y_start = int(event.y / piksel)*piksel
    return x_start, y_start


def draw_on_canvas(event):
    x_start, y_start = calculate_position_for_square(event)
    # print("x,y", event.x, " , ", event.y)
    # print("x,y", x_start, " , ", y_start)
    DRAWN_BITMAP[int(y_start/piksel)][int(x_start/piksel)] = 1
    canvas.create_rectangle(x_start, y_start,
                            x_start+piksel, y_start+piksel,
                            fill="black", outline="")


def wipe_off_canvas(event):
    x_start, y_start = calculate_position_for_square(event)
    DRAWN_BITMAP[int(y_start/piksel)][int(x_start/piksel)] = 0
    canvas.create_rectangle(x_start, y_start,
                            x_start + piksel, y_start + piksel,
                            fill="white", outline="")

def add_bitmap():
    dc = copy.deepcopy(DRAWN_BITMAP)
    BITMAPS.append(dc)
    global counter_bitmaps
    counter_bitmaps += 1
    listbox.insert(counter_bitmaps, "bitmapa"+str(counter_bitmaps))
    infoLabel.config(text="", fg="red")


def dispaly_on_canvas(array, canvas):
    for i, row in enumerate(array):
        for j, el in enumerate(row):
            x = i * piksel
            y = j * piksel
            if el == 1:
                # print("X, y = (%i, %i), (%i, %i)"%(j,i, j*40, i*40))
                canvas.create_rectangle(y, x, y+piksel, x+piksel, fill="black", outline="")
            if el == 0:
                canvas.create_rectangle(y, x, y + piksel, x + piksel, fill="white", outline="")


def clear_canvas():
    global DRAWN_BITMAP
    DRAWN_BITMAP = set_size_bitmap(5, 5)
    dispaly_on_canvas(DRAWN_BITMAP, canvas)


def match_bitmap():
    global BITMAPS,  BITMAP_TEST
    bitmaps_pattern = copy.deepcopy(BITMAPS)
    bitmap_test = copy.deepcopy(BITMAP_TEST)
    if len(BITMAPS) != 0 and len(BITMAP_TEST) != 0:

        hn = HopfieldNetwork(bitmaps_pattern, bitmap_test)
        hn.teach_list_pictures()
        bitmap_result = hn.recognize_the_picture()

        #dispaly_on_canvas(bitmap_result, canvas_result)
        # przekopiowanie aktualnego wyniku na bitmape testowo
        BITMAP_TEST= copy.deepcopy(bitmap_result)
        dispaly_on_canvas(BITMAP_TEST, canvas_test)
        print(bitmap_result)
        # wyświeltenie na canvasie testowym, aktualny wynik algorytmu
        infoLabel.config(text="bitmapa", fg="green")
    else:
        infoLabel.config(text="Nie ustalono bitmap wzorcowych lub bimapy testowej!!", fg="red")


def dispaly_on_canvas_test():
    global BITMAP_TEST
    dispaly_on_canvas(DRAWN_BITMAP, canvas_test)
    BITMAP_TEST = copy.deepcopy(DRAWN_BITMAP)



# -------------------- Interfejs -------------------

BITMAPS = []
DRAWN_BITMAP = set_size_bitmap(5, 5)
BITMAP_TEST = set_size_bitmap(5, 5)
counter_bitmaps = 0

window_width = 600
window_height = 400

window = Tk()

# -------------------- first frame ---------------
frame1 = Frame(window)
frame1.pack()

add_button = Button(frame1, text="Dodaj do bazy", padx=10, pady=10, width=20, command=add_bitmap)
add_button.grid(row=0, column=0)

recognize_button = Button(frame1, text="Ustwa jako bitmapa testowa", padx=10, pady=10, width=20, command=dispaly_on_canvas_test)
recognize_button.grid(row=0, column=1)

# -------------------- second frame -------------
canvas_width = 200
canvas_height = 200
piksel = 40

frame2 = Frame(window, pady=10)
frame2.pack()


# -------------------- canvas section ------------
canvas = Canvas(frame2, bg="white", width=canvas_width, height=canvas_height, bd=0, highlightthickness=0, relief=GROOVE )
canvas.bind("<Button-1>", draw_on_canvas)
canvas.bind("<Button-3>", wipe_off_canvas)
canvas.grid(row=2, column=0)


# -------------------- List Box section ------------
list_items = StringVar()
listbox = Listbox(frame2, width=20, height=12, listvariable=list_items)
listbox.bind("<<ListboxSelect>>", click_item_on_listbox)
listbox.grid(row=2, column=1, )

# -------------------- Canvas Clear Bottom Section  ------------
algButton = Button(frame2, text="Wyczyść", padx=10, command=clear_canvas)
algButton.grid(row=3, column=0)


# -------------------- Separator Section  ------------
separator = ttk.Separator(frame2, orient='horizontal')
separator.grid(row=4, column=0, columnspan=2, sticky="we", pady=10)


# ------------------- Algorytm section ---------------

algButton = Button(frame2, text="Szukaj", padx=10, command=match_bitmap)
algButton.grid(row=5, column=0, columnspan=2)

# ---------------------- panel wyboru i wyniku
label_canvas_test = Label(frame2, text="bitmapa testowa")
label_canvas_test.grid(row=6, column=0)

label_canvas_result = Label(frame2, text="wynik")
label_canvas_result.grid(row=6, column=1)

canvas_test = Canvas(frame2, bg="white", width=canvas_width, height=canvas_height, bd=1, relief=GROOVE)
canvas_test.grid(row=7, column=0, sticky="nwse")

canvas_result = Canvas(frame2, bg="white", width=canvas_width, height=canvas_height, bd=1, relief=GROOVE)
canvas_result.grid(row=7, column=1, sticky="nwse")

infoLabel = Label(frame2, text="info", pady=10)
infoLabel.grid(row=8, column=0, columnspan=2)


window.mainloop()