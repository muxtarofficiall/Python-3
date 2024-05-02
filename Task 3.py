def duz(cumle):
    # Cümlədəki sözləri ayrı-ayrı qaytarır
    sozler = cumle.split()
    
    # Hər bir sözdəki hərfləri alfabetik sırasına görə düzəlt
    siralanmis_sozler = [''.join(sorted(soz)) for soz in sozler]
    
    # Yenidən cümlə şəklində birləşdir
    siralanmis_cumle = ' '.join(siralanmis_sozler)
    
    return siralanmis_cumle

# İstifadəçidən cümlə daxil etməsini istəyin
cumle = input("Bir cümlə daxil edin: ")

# Funksiyadan istifadə edərək sözləri sıralayın
siralanmis_cumle = duz(cumle)

# Sıralanmış cümləni çap edin
print("Sıralanmış cümlə:", siralanmis_cumle)


