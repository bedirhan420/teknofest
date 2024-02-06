import random
import csv

num_examples = 500

cinsiyetler = ['Erkek', 'Kadin']
beslenme_sekilleri = ['Normal', 'Vegan', 'Glutensiz']
egzersiz_tipleri = ['a', 'b', 'c', 'd']

veri_seti = []

for _ in range(num_examples):
    cinsiyet = random.choice(cinsiyetler)
    yas = random.randint(15, 85)
    boy = random.randint(150, 200)
    kilo = random.randint(45, 120)
    beslenme_sekli = random.choice(beslenme_sekilleri)
    uyku_saati = random.randint(4, 9)
    egzersiz_tipi = random.choice(egzersiz_tipleri)
    
    veri_seti.append([cinsiyet, yas, boy, kilo, beslenme_sekli, uyku_saati, egzersiz_tipi])

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Age', 'Height', 'Weight', 'Diet', 'SleepTime', 'ExcersiseType'])
    for veri in veri_seti:
        writer.writerow(veri)