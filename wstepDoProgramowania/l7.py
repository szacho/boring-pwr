from tkinter import Tk, Canvas
from math import sqrt, sin, cos
import time
from random import uniform, randint

rocket_size = 15

class Rocket:
    count_rockets = 0

    def __init__(self, canvas, velocity=50, coords=(0, 0)):
        self.__class__.count_rockets += 1 #zlicznie utworzonych rakiet, żeby przypisać etykietę
        self.start_position = coords
        self.x = coords[0]
        self.y = coords[1]
        self.velocity = max(min(velocity, 100), 10)/15 #prędkość z jaką porusza się rakieta, nie więcej niż 100 i nie mniej niż 10
        self.waypoints = [] #historia podróży, żeby odtworzyć animację
        self.travelled_distance = [] #przevyta ogległość po każdym etapie ruchu, potrzebna żeby policzyć wektor do animacji
        
        #inizjalizacja rakiety na canvie
        self.canvas = canvas
        self.id = self.__class__.count_rockets
        color = '#6200EE'
        if self.id == 5: color = '#cc5490'
        self.body = self.canvas.create_oval(self.x,self.y,self.x+rocket_size,self.y+rocket_size,fill=color)
        self.label = self.canvas.create_text(self.x+rocket_size/2,self.y+rocket_size/2,text=self.id, fill="white")
        self.canvas.update()

    def __repr__(self):
        return 'Rocket {}: position ({}, {})'.format(self.id, self.x, self.y)

    def move(self, v, animation=False):
        #vector v = (x, y)
        #gdy wyświetlamy animację to rakieta porusza się tylko na canvie, nie zmieniając swoich atrybutów
        if not animation:
            self.travelled_distance.append(self.calc_distance((self.x, self.y), (self.x+v[0], self.y+v[1])))
            self.waypoints.append(v)
            self.x += v[0]
            self.y += v[1]
            print(self)
        
        self.canvas.move(self.body, *v)
        self.canvas.move(self.label, *v)
    
    def get_position(self):
        print('Rocket at position ({:.2f}, {:.2f})'.format(self.x, self.y))

    def get_distance(self, rocket, step=0):
        if step>0:
            #żeby policzyć dystans po n-tym ruchu, nie zmieniając atrybutów rakiety
            l1 = min(len(self.waypoints), step)
            l2 = min(len(rocket.waypoints), step)
            x1 = self.start_position[0]+sum([coords[0] for coords in self.waypoints[:l1]])
            x2 = rocket.start_position[0]+sum([coords[0] for coords in rocket.waypoints[:l2]])
            y1 = self.start_position[1]+sum([coords[1] for coords in self.waypoints[:l1]]) 
            y2 = rocket.start_position[1]+sum([coords[1] for coords in rocket.waypoints[:l2]])
            dist = self.calc_distance((x1,y1), (x2, y2))
        else:
            dist = self.calc_distance((self.x, self.y), (rocket.x, rocket.y))

        print('The distance between Rocket #{} and Rocket #{} equals {:.2f}'.format(self.id, rocket.id, dist))

    def reset(self):
        #przywrócenie do pozycji startowej (tylko na canvie), żeby wyświetlić animację
        x, y = self.start_position[0], self.start_position[1]
        self.canvas.move(self.body, x-self.x, y-self.y)
        self.canvas.move(self.label, x-self.x, y-self.y)
    
    @staticmethod
    def calc_distance(p1, p2):
        return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2) 

    @staticmethod
    def launch(rockets, uni):
        #generowanie ścieżek po jakich poruszają się rakiety z uwzględnieniem ich prędkości
        #ścieżka składa się z wielu małych wektorów (kroków), którymi rakieta porusza się w jednostce czasu
        #długość kroku danej rakiety zależy od jej prędkości, a kierunek jest różny zależnie od etapu ruchu
        paths = []
        for rocket in rockets:
            rocket.reset() #przeniesienie rakiety na pozycję startową
            path = []
            for key, waypoint in enumerate(rocket.waypoints):
                k = rocket.travelled_distance[key]/rocket.velocity 
                v = (waypoint[0]/k, waypoint[1]/k) #wektor reprezentujący pojedynczy krok w jednostce czasu w danym etapie ruchu
                path.extend([v]*int(k)) #uzupełnienie ścieżki o ilość kroków dla danego etapu ruchu
            paths.append(path)
        
        for n in range(max([len(p) for p in paths])): #animacja się wyświetla do zatrzymania się ostatniej rakiety
            for key, rocket in enumerate(rockets):
                try:
                    rocket.move(paths[key][n], animation=True)
                except:
                    pass #ścieżki różnych rakiet mogą mieć różne długości, więc jak rakieta skończy latać to trzeba ją pominąć
                else:
                    uni.update()
            time.sleep(.02)

        return rockets


def randomCoords():
    return (uniform(400,600), uniform(400, 600))
def randomMove():
    return (uniform(-200,200), uniform(-200, 200))
def randomVelocity():
    return uniform(10,100)

def main():
    #inicjalizacja tkinter canvas
    uni = Tk()
    size = 1000
    uni.geometry("{}x{}".format(size,size))
    uni.title("Universe")

    canvas = Canvas(uni, width=size, height=size, bd=0, bg='#222')
    canvas.pack()

    #Zad. 3
    rocket1 = Rocket(canvas, randomVelocity(), randomCoords())
    rocket2 = Rocket(canvas, randomVelocity(), randomCoords())
    rocket3 = Rocket(canvas, randomVelocity(), randomCoords())
    rocket4 = Rocket(canvas, randomVelocity(), randomCoords())
    rocket5 = Rocket(canvas, 60, (500,333))

    stepsRange = (3,8)
    for _ in range(randint(*stepsRange)):
        rocket1.move(randomMove())
    for _ in range(randint(*stepsRange)):
        rocket2.move(randomMove())
    for _ in range(randint(*stepsRange)):
        rocket3.move(randomMove())
    for _ in range(randint(*stepsRange)):
        rocket4.move(randomMove())
    rocket5.move((83,-166))
    rocket5.move((166,0))
    rocket5.move((83,166))
    rocket5.move((0,166))
    rocket5.move((-333,333))
    rocket5.move((-333,-333))
    rocket5.move((0,-166))
    rocket5.move((83,-166))
    rocket5.move((166,0))
    rocket5.move((83,166))

    rockets =[ rocket1, rocket2, rocket3, rocket4, rocket5 ]
    Rocket.launch(rockets, uni)
    
    #odległości po każdym ruchu, zakładam że rakiety pojedynczy ruch wykonują jednocześnie
    maxSteps = max([len(rocket.waypoints) for rocket in rockets])
    for s in range(maxSteps):
        print("DISTANCE AFTER {}. STEP".format(s+1))
        for n in range(len(rockets)):
            for rocket in rockets[(n+1):]: #obcinam tablicę z rakietami, żeby nie powtarzać tych samych par
                rockets[n].get_distance(rocket, step=s+1)


    uni.mainloop()



main()