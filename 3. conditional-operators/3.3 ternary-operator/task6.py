m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

note_1, note_2, note_3 = map(int, input().split())
print(f"{"#" + m[note_1 - 1] if m[note_1 - 1] in ["до", "фа"] else m[note_1 - 1]} {"#" + m[note_2 - 1] if m[note_2 - 1] in ["до", "фа"] else m[note_2 - 1]} {"#" + m[note_3 - 1] if m[note_3 - 1] in ["до", "фа"] else m[note_3 - 1]}" )