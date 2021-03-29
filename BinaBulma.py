import cv2 # opencv kutuphanesini cekiyoruz

resim = cv2.imread('karakopru.png') # resmi charm da calistiriyoruz


while(True):
    OrnekResim   =    cv2.imread('aranankar.jpeg') # tespit edecegimiz resim
    OrnekResimDonustur   =    cv2.cvtColor(OrnekResim,cv2.COLOR_BGR2GRAY) # tespit edecegimiz resimi gri formata donusturur

    EkranGoruntusuDonustur  =    cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY) #Ekran Goruntusunu Gri Formata Donusturuyoruz

    Sonuc  =    cv2.matchTemplate(EkranGoruntusuDonustur,OrnekResimDonustur, cv2.TM_CCOEFF_NORMED) #Ekran Grountusunun Icerisinde Resmi Ariyoruz
    sin_val, max_val, min_loc, max_loc    =    cv2.minMaxLoc(Sonuc) #Bulunan Objenin Koordinatlarini Bul
    Ust_Sol   =    max_loc #Bulunan Objenin Ust ve Sol Uzakligi
    Alt_Sag   =    (Ust_Sol[0]+20, Ust_Sol[1]+20) #Bulunan Objenin Alt ve Sag Uzakligi
    cv2.rectangle(resim, Ust_Sol, Alt_Sag, (0,150,0),2) #Ekranda Bulunan Nesnenin Koordinatlarini Isaretle
    cv2.imshow('Goruntu Isleme Uydu Goruntusunden Bina Tespiti - Mucahit Ozturk - Beyza Nur Butun',resim) #Ekran Goruntusunu Goster
    if cv2.waitKey(25) & 0xFF == ord('q'): #resimden cikis yapabilmek icin q tusuna basma gereksinimi koyduk.
        cv2.destroyAllWindows()
        break
cv2.imwrite('sonuc.jpeg',resim) # resmin ciktisini yazdiriyoruz

