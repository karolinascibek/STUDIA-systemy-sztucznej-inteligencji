from blok2.lab7.hopfield_network import HopfieldNetwork


p1 = [
    [1, -1, 1, -1],
    [ 1, -1, 1, -1]
    ]
p2 = [
    [1, 1, 1, 1],
    [-1, -1, -1, -1]
]

pp=[p1,p2]

p1 = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1],
]

p2 = [
    [1,1,1,1,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,1],
]

p3 = [
    [1,1,1,1,1],
    [1,0,0,0,0],
    [1,1,1,0,0],
    [1,0,0,0,0],
    [1,1,1,1,1],
]



bitmaps_pattern = [p1, p2, p3]

t1=[[1,1,1,1],[1,-1,-1,-1]]
hn = HopfieldNetwork(bitmaps_pattern, p1)
hn.teach_list_pictures()
r = hn.recognize_the_picture()
print("wynik: ")
print(r)

