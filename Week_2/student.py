# coding: utf-8


dict = {'Curi Pachas, Sofia Belinda': (2342915),
   'Leon Macias, Ava Sofia': (2342514),
   'Mora Silva, Valeria': (2322596),
   'Nguyen, Quoc Anh': (2342768),
   'Serrano Fragoso, Anais': (2343003)}

def file_name(name, id):  # defining a function called circle
    """Receives the name and id number of a student and returns the file name in the format:\n 
    WIM250_SU25_A2_Name_id requested by the college.""" 
    
    return f'WIM250_SU24_A2_{name}_{id}'    

def student_name(id):
    """Receive the student ID and return the student's name."""
    for name, current_id in dict.items():
        if current_id == id:
            print(name)
    