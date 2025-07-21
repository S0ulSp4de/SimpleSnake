#Simples Snake Spiel mit turtle by David Tretter

import turtle
from turtle import *
from random import randint
import time

#Erstelle einen einfachen Score Wert
score = 0
spiel_gestartet = True
""" erstelle_turtle() verkürzt die Schreibarbeit für
 die Erstellung der verschiedenen Turtles im Spiel.
 Den letzten zwei Parametern von erstelle_turtle() wurden sogenannte
 Standardwerte hinzugefügt. Standardwerte (auch: default values) werden
 für die jeweiligen Parameter beim Aufruf der Funktion automatisch
 eingesetzt, wenn der Funktion nicht explizit Argumente für diese Parameter
 mitgegeben werden. Da die Steuerungsdreiecke die Mehrheit der
 Turtle-Elemente darstellen, wurden eine Dreiecksform und eine grüne
 Füllfarbe als Standardwerte für die Parameter shape und color gewählt. """
def erstelle_turtle(x, y, rotationswinkel, shape="triangle", color="green"):
    element = turtle.Turtle()
    element.speed(0)  # Keine Animation, Turtle "springt" zum Zielpunkt
    element.shape(shape)
    element.color(color)
    element.right(rotationswinkel)  # Nur für grüne Steuerungsdreiecke relevant
    element.penup()
    element.goto(x, y)
    # Nur für Kopf relevant; "direction" ist nicht aus Turtle,
    # sondern eine Variable von uns, die wir "element" dynamisch zuweisen
    element.direction = "stop"

    return element

def nach_unten_ausrichten():
    if kopf.direction != "up":
        kopf.direction = "down"

def nach_rechts_ausrichten():
    if kopf.direction != "left":
        kopf.direction = "right"

def nach_links_ausrichten():
    if kopf.direction != "right":
        kopf.direction = "left"

def nach_oben_ausrichten():
    if kopf.direction != "down":
        kopf.direction = "up"

def interpretiere_eingabe(x, y):
    global spiel_gestartet
    if (x >= 150 and x <= 170 and y >= -190 and y <= -170):
        nach_unten_ausrichten()
        spiel_gestartet = True
    elif (x >= 170 and x <= 190 and y >= -170 and y <= -150):
        nach_rechts_ausrichten()
        spiel_gestartet = True
    elif (x >= 150 and x <= 170 and y >= -150 and y <= -130):
        nach_oben_ausrichten()
        spiel_gestartet = True
    elif (x >= 130 and x <= 150 and y >= -170 and y <= -150):
        nach_links_ausrichten()
        spiel_gestartet = True
        

onclick(interpretiere_eingabe)


def kopf_bewegen():
    if kopf.direction == "down":
        y = kopf.ycor()
        kopf.sety(y - 20)
    elif kopf.direction == "right":
        x = kopf.xcor()
        kopf.setx(x + 20)
    elif kopf.direction == "up":
        y = kopf.ycor()
        kopf.sety(y + 20)
    elif kopf.direction == "left":
        x = kopf.xcor()
        kopf.setx(x - 20)


def koerper_bewegen():
     #Überprüfe, ob Schlange nicht nur aus Kopf besteht
     if len(segmente) >= 1:
            for index in range(len(segmente) - 1, 0, -1):
                # Hole die Koordinaten des vorherigen Segments
                xc = segmente[index - 1].xcor()
                yc = segmente[index - 1].ycor()
            
                # Bewege das Segment zum vorherigen Segment
                segmente[index].goto(xc, yc)
            # Hole die Koordinaten des Kopfes
            kopf_x = kopf.xcor()
            kopf_y = kopf.ycor()
            # Bewege das erste Segment zum Kopf
            segmente[0].goto(kopf_x, kopf_y)

def segmente_entfernen():
# Verstecke und entferne Segmente
    for segment in segmente:
        segment.hideturtle()
        del segment
    segmente.clear()

def spiel_neustarten():
    global score, spiel_gestartet
    kopf.goto(0, 0)
    kopf.direction = "stop"  # Richtung auf "stop" setzen
    segmente_entfernen()
    spiel_gestartet = True
    print(f"Game over. Dein letzter Score lag bei {score} Segmenten")
    score = 0

def checke_kollision_mit_fensterrand():
    if kopf.xcor() > 190 or kopf.xcor() < -190 or kopf.ycor() > 190 or kopf.ycor() < -190:
        spiel_neustarten()

def checke_kollision_mit_segmenten():
    for segment in segmente:
        if segment.distance(kopf) < 20:
            spiel_neustarten()

def checke_kollision_mit_essen():
    global score
    if kopf.distance(essen) < 20:
        x = randint(-9, 6) * 20
        y = randint(-6, 9) * 20
        essen.goto(x, y)
        neues_segment = Turtle()
        neues_segment.shape("circle")
        neues_segment.color("green")
        neues_segment.penup()
        speed(0)
        segmente.append(neues_segment)
        score = score + 1


def wiederhole_spiellogik():
    # Damit das Spiel bis zu einer Niederlage läuft, wird der folgende
    # Code von wiederhole_spiellogik() in einer Endlosschleife aufgerufen
    while True:
        if spiel_gestartet == True:  # Schlange bewegt sich nur, wenn das Spiel gestartet wurde
            checke_kollision_mit_essen()
            checke_kollision_mit_fensterrand()
            koerper_bewegen()
            kopf_bewegen()
            checke_kollision_mit_segmenten()

        # Position der verschiedenen Turtle-Elemente aktualisieren
        turtle.update()

        # time.sleep() unterbricht die Ausführung des weiteren
        # Codes für die angegebene Anzahl an Sekunden
        # An dieser Stelle verlangsamt sleep() das Spiel, damit die Schlange
        # nicht aus dem Bildschirm laufen kann, bevor man sie sehen kann.
        time.sleep(0.15)


# Auf dem Spielfeld sichtbare Elemente definieren
rechts = erstelle_turtle(180, -160, 0)
unten = erstelle_turtle(160, -180, 90)
links = erstelle_turtle(140, -160, 180)
oben = erstelle_turtle(160, -140, 270)
essen = erstelle_turtle(0, 100, 0, "circle", "yellow")
kopf = erstelle_turtle(0, 0, 0, "square", "red")
segmente = []

# Spielbereich (das sich öffnende Fenster beim Ausführen dieser Datei) definieren
spielbereich = turtle.Screen()
spielbereich.title("Mein Snake-Spiel")
spielbereich.setup(width=430, height=430)

# Drücken der Pfeiltasten zur Richtungssteuerung registrieren
spielbereich.onkeypress(nach_oben_ausrichten, "Up")
spielbereich.onkeypress(nach_links_ausrichten, "Left")
spielbereich.onkeypress(nach_unten_ausrichten, "Down")
spielbereich.onkeypress(nach_rechts_ausrichten, "Right")
spielbereich.listen()

# Registrierung der Richtungssteuerung über das Anklicken der grünen Dreiecke
turtle.onscreenclick(interpretiere_eingabe)

# Turtle in der Mitte verbergen
turtle.hideturtle()

# Automatisches Aktualisieren der Turtle-Elemente ausschalten
turtle.tracer(False)

# Try-Except-Block fängt Beenden des Spiels ab
try:
    wiederhole_spiellogik()
except turtle.Terminator:
    print("Das Spiel wurde beendet.")
    # exit(0) beendet das Program sauber
    exit(0)
