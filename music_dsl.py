from textx import metamodel_from_str, metamodel
from textx.export import metamodel_export, model_export
import os
import time
import music_library_and_utils


chord_player = music_library_and_utils

context = "(' FLOAT?','? FLOAT?','? INT? ')"
 

grammar = f"""

SENTENCE: Chord=CHORD | Circle=CIRCLE ;
CHORD: ('do_chord{context}' | 'dom_chord{context}' | 'do#m_chord{context}' | 'do7_chord{context}' | 'do#7_chord{context}' | 'dom7_chord{context}' | 
       're_chord{context}' | 'rem_chord{context}' | 're#m_chord{context}' | 're7_chord{context}' | 're#7_chord{context}' | 'rem7_chord{context}' |
       'mi_chord{context}' | 'mim_chord{context}' | 'mi7_chord{context}' | 'mim7_chord{context}' | 
       'fa_chord{context}' | 'fam_chord{context}' | 'fa#m_chord{context}' | 'fa7_chord{context}' | 'fa#7_chord{context}' | 'fam7_chord{context}' |
       'sol_chord{context}' | 'solm_chord{context}' | 'sol#m_chord{context}' | 'sol7_chord{context}' | 'sol#7_chord{context}' | 'solm7_chord{context}' | 
       'la_chord{context}' | 'lam_chord{context}' | 'la#m_chord{context}' | 'la7_chord{context}' | 'la#7_chord{context}'  | 'lam7_chord{context}' |
       'si_chord{context}' | 'sim_chord{context}' | 'si7_chord{context}' | 'sim7_chord{context}' | 
       'repetition('INT?')')*; 
CIRCLE: 'circle_do' | 'circle_re' | 'circle_mi' | 'circle_fa' | 'circle_sol' | 'circle_la' | 'circle_si'; 
"""



def main():
    mymetamodel = metamodel_from_str(grammar)
    metamodel_export(mymetamodel, 'myAst.dot')

   
    while True:
        
        try:
            Input = input("Enter sentence to evaluate: ")
            Sentence = mymetamodel.model_from_str(Input)
            model_export(Sentence, 'Parse-tree1.dot')
            print("It is a valid sentence")
        except:
            print("Sentence is not correct according to Grammar") 

        switch = input("Continue? 1)Yes 2)No ")
        if switch == '2':
            break
    return Input


def format_string(string_to_format): # do_chord(1, 7, 7)
    print("nothing")

    if string_to_format.__contains__("_chord"):

        input_list = string_to_format.split("(") # ["do_chord(", "1 ,7 ,7)"]    
        chord = input_list[0] #do_chord( --> do_chord                                
        times = input_list[1].split(",") # [ "1", " 7", "4)"]
        print(f"value of {times}") 
        try:
            duration = times[0] # 1, --> 1
            silence = times[1] # 7, -->7
            chord_repetition = times[2].replace(")", "") #"7)" -->7
            duration = float(duration)
            silence = float(silence)
            chord_repetition = int(chord_repetition)
            
        except:
            chord = string_to_format.replace("(", "")
            chord = chord.replace(")", "")
            duration = 1
            silence = 1
            chord_repetition= 1
        print(f"Silence value is: {silence}")
        return chord, duration, silence, chord_repetition
    else:
        harmonic_circle = string_to_format
        return harmonic_circle
        

def check_if_repetition_exists(last_element):
    repetition_exists = False
    repetition = last_element
    if repetition.__contains__("repetition"):
        repetition = repetition.replace("repetition(","")
        repetition = int(repetition.replace(")", ""))
        repetition_exists = True
    else:
        repetition = 0
    
    return repetition_exists, repetition
    

def play(chord_sequence, is_circle=False): # do_chord() re_chord()
    if is_circle:
        circle_or_chord = chord_player.harmonic_circles
        chord_player.play_harmonic_circle(circle_or_chord[chord_sequence])
    else:
        for chord_to_play in chord_sequence: # do_chord() re_chord()
            (chord, duration, silence, chord_repetition) = format_string(string_to_format=chord_to_play)
            print(f"play chord {chord} with a duration of {duration}s and a silence of {silence} with a repetition cycle of {chord_repetition}")
            circle_or_chord = ""
            if chord.__contains__("chord"):
                circle_or_chord = chord_player.chords

                if chord_repetition != 1:
                    for i in range(chord_repetition):
                        chord_player.play_chord(chord=circle_or_chord[chord], duration=duration)
                        time.sleep(silence)
                else:
                    chord_player.play_chord(chord=circle_or_chord[chord])
                    time.sleep(silence)
                
            else:                    
                chord_player.play_harmonic_circle(circle= circle_or_chord[chord])



if __name__ == '__main__':

    
    input_string = main() # do_chord(1,1,4) re_chord() repetition(2) | circle_do
    # if input string contains "circle"

    try:
        chord_sequence = input_string.split()
        last_element = chord_sequence[-1]
        (repetition_exists, repetition) =check_if_repetition_exists(last_element=last_element)
        print(f"repetition_exist: {repetition_exists} repetition: {repetition}")

        if repetition_exists:
            chord_sequence.pop()
            for i in range(repetition):
                play(chord_sequence=chord_sequence)
        else:
            play(chord_sequence=chord_sequence)
    except:
        circle_to_play = input_string
        print(f" The circle to be played is {circle_to_play}")
        play(chord_sequence=circle_to_play, is_circle=True)





