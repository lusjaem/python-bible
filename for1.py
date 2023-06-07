samogloski = 0
spolgloski = 0

answer = input('''Wpisz tekst, w którym chciałbyś sprawdzić ilość samogłosek i spółgłosek: ''').lower().strip()

print(answer)

for letter in answer:
    if letter.lower() in "aoeuiy":
        samogloski = samogloski + 1
    elif letter.lower() == "" or letter.lower() == " ":
        pass
    else:
        spolgloski = spolgloski + 1    

print("Mamy {} samogloski.".format(samogloski))
print("Mamy {} spolgloski.".format(spolgloski))
