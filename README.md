# Eba Ders Atayıcı

Haftalık ders programını EBA'ya aktarmak için kullanabilirsiniz.

## Gereksinimler

- Google Chrome

## Kurulum

Aşağıdaki komutları terminalde çalıştırın:

```
    git clone https://github.com/emirhanbayar/course_assigner.git
    cd course_assigner
    chmod +x ./install.sh
    ./install.sh
```


## Kullanım

- Haftalık ders prgramınız DersProgram.txt dosyasına giriniz. Her satırda tek bir ders tanımlanmalı ve her bir dersin formatı şu şekilde olmalı:

```
    ["Ders Adı", "Şube", "Sınıf", "Zoom görüşme linki", "Zoom görüşme şifresi"]
```

Örneğin,

```
["Matematik", "1/H", "1", "https://us04web.zoom.us/j/sdkvsf", "5xQ9wv"]
["Türkçe", "1/A", "1", "https://us04web.zoom.us/j/sdkvsf", "5xQ9wv"]
            .
            .
            .
```

- Daha sonra aşağıdaki komutla programı çalıştırın:
```
python3 assigner.py
```

- Program kullanıcı adı ve şifrenizi girmenizi isteyecek, kullanıcı adı ve şifrenizi girin. Daha sonra program her ders için gerekli alanları dolduracak. Sadece tarih ve zamanı elle girmek gerekiyor. Bunun için 20 saniye vaktiniz var. 


