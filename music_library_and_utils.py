from multiprocessing import Process
from pygame import mixer as mx
import time


parent_path = "Notes/"
file_extension = ".mp3"

notes = {
"do4": f"{parent_path}C4{file_extension}",
"do4#": f"{parent_path}C4#{file_extension}",
"re4": f"{parent_path}D4{file_extension}",
"re4#": f"{parent_path}D4#{file_extension}",
"mi4": f"{parent_path}E4{file_extension}",
"fa4": f"{parent_path}F4{file_extension}",
"fa4#": f"{parent_path}F4#{file_extension}",
"sol4": f"{parent_path}G4{file_extension}",
"sol4#": f"{parent_path}G4#{file_extension}",
"la4": f"{parent_path}A4{file_extension}",
"la4#": f"{parent_path}A4#{file_extension}",
"si4": f"{parent_path}B4{file_extension}"
}


chords = {
"do_chord" : [notes["do4"], notes["mi4"], notes["sol4"]],
"dom_chord" : [notes["do4"], notes["do4#"], notes["sol4"]],
"do#m_chord" : [notes["do4#"], notes["mi4"], notes["sol4#"]],
"do7_chord" : [notes["do4"], notes["mi4"], notes["sol4"], notes["la4#"]],
"do#7_chord" : [notes["do4#"], notes["fa4"], notes["sol4#"], notes["si4"]], #test
"dom7_chord" : [notes["do4"], notes["re4#"], notes["sol4"], notes["la4#"]], #test

"re_chord" : [notes["re4"], notes["fa4#"], notes["la4"]],
"rem_chord" : [notes["re4"], notes["fa4"], notes["la4"]],
"re#m_chord" : [notes["re4#"], notes["fa4#"], notes["la4#"]],
"re7_chord" : [notes["re4"], notes["fa4#"], notes["la4"], notes["do4"]], #test
"re#7_chord" : [notes["re4#"], notes["sol4"], notes["la4#"], notes["do4#"]], #test
"rem7_chord" : [notes["re4"], notes["fa4"], notes["la4"], notes["do4"]], #test

"mi_chord" : [notes["mi4"], notes["sol4#"], notes["si4"]],
"mim_chord" : [notes["mi4"], notes["sol4"], notes["si4"]],
"mi7_chord" : [notes["mi4"], notes["sol4#"], notes["si4"], notes["re4"]],
"mim7_chord" : [notes["mi4"], notes["sol4"], notes["si4"], notes["re4"]], #test

"fa_chord" : [notes["fa4"], notes["la4"], notes["do4"]],
"fam_chord" : [notes["fa4"], notes["sol4#"], notes["do4"]],
"fa#m_chord" : [notes["fa4#"], notes["la4"], notes["do4#"]],
"fa7_chord" : [notes["fa4"], notes["la4"], notes["do4"], notes["la4#"]],  #test
"fa#7_chord" : [notes["fa4#"], notes["la4#"], notes["do4#"], notes["mi4"]],
"fam7_chord" : [notes["fa4"], notes["sol4#"], notes["do4"], notes["re4#"]], #test

"sol_chord" : [notes["sol4"], notes["si4"], notes["re4"]],
"solm_chord" : [notes["sol4"], notes["la4#"], notes["re4"]],
"sol#m_chord" : [notes["sol4#"], notes["si4"], notes["re4#"]],
"sol7_chord" : [notes["sol4"], notes["si4"], notes["re4"], notes["fa4"]],
"sol#7_chord" : [notes["sol4#"], notes["do4"], notes["re4#"], notes["fa4#"]], #test
"solm7_chord" : [notes["sol4"], notes["la4#"], notes["re4"], notes["fa4"]], #test

"la_chord" : [notes["la4"], notes["do4#"], notes["mi4"]],
"lam_chord" : [notes["la4"], notes["do4"], notes["mi4"]],
"la#m_chord" : [notes["la4#"], notes["do4#"], notes["fa4"]], #test
"la7_chord" : [notes["la4"], notes["do4#"], notes["mi4"], notes["sol4"]],
"la#7_chord" : [notes["la4#"], notes["re4"], notes["fa4"], notes["sol4#"]], #test
"lam7_chord" : [notes["la4"], notes["do4"], notes["mi4"], notes["sol4"]],

"si_chord" : [notes["si4"], notes["re4#"], notes["fa4#"]],
"sim_chord" : [notes["si4"], notes["re4"], notes["fa4#"]],
"si7_chord" : [notes["si4"], notes["re4#"], notes["fa4#"], notes["la4"]],
"sim7_chord" : [notes["si4"], notes["re4#"], notes["fa4#"], notes["la4"]] #test
}


harmonic_circles = {
    "circle_do" : [chords["do_chord"], chords["lam_chord"], chords["rem_chord"], chords["sol7_chord"]],
    "circle_re" : [chords["re_chord"], chords["sim_chord"], chords["mim_chord"], chords["la7_chord"]],
    "circle_mi" : [chords["mi_chord"], chords["do#m_chord"], chords["fa#m_chord"], chords["si7_chord"]],
    "circle_fa" : [chords["fa_chord"], chords["rem_chord"], chords["solm_chord"], chords["do7_chord"]],
    "circle_sol" : [chords["sol_chord"], chords["mim_chord"], chords["lam_chord"], chords["re7_chord"]],
    "circle_la" : [chords["la_chord"], chords["fa#m_chord"], chords["sim_chord"], chords["mi7_chord"]],
    "circle_si" : [chords["si_chord"], chords["sol#m_chord"], chords["do#m_chord"], chords["fa#7_chord"]],
}

mx.init()

def play_notes(notePath, duration=1): 
    print(f"This is the value of the note to play{notePath}")    
    mx.music.load(notePath)
    mx.music.play()
    time.sleep(duration)

def play_chord(chord, duration=1):
    print(f" This is the value of the chord to play {chord}")
    for note in chord:
        P = Process(target = play_notes, args = (note, duration,))
        P.start()

def play_harmonic_circle(circle): #harmonics_circles[circle_do]

    for chord in circle:
        play_chord(chord)
        time.sleep(1)


if __name__ == '__main__':

    #play_notes(notePath = notes["do4#"])
    play_chord(chord=chords["la_chord"])    