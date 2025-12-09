from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

QUOTES = [
    "Sana harika bir gün diliyorum! Enerjin tavan olsun.",
    "O ertelediğin işi bitirmek için mükemmel bir gün. Hadi başla!",
    "Bugün çok şık görünüyorsun, aynaya bakmadın mı?",
    "Bir kahve molası vermeden çalışmak yasaklanmalı. Git kendine bir kahve ısmarla.",
    "Modun biraz düşük mü? En sevdiğin şarkıyı son ses aç, kimse umurunda olmasın.",
    "En son ne zaman sadece kendin için bir şey yaptın? Bugün o gün olsun.",
    "Okul ya da iş... Biliyorum sıkıcı ama sen halledersin şampiyon.",
    "Bu akşam güzel bir film izle, mısır patlatmayı da unutma.",
    "Potansiyelin inanılmaz, bunu verilerimde net görüyorum. Aynen devam.",
    "Bugün birine gülümse, bazen küçücük bir hareket dünyayı değiştirir.",
    "Hafta sonu için planın var mı? Bence kendini doğaya at.",
    "O mesajı atmanın tam zamanı. Cesur ol, ne kaybedersin ki?",
    "Gökyüzüne bak. Bazen kafayı kaldırıp derin bir nefes almak her şeyi çözer.",
    "Sosyal medyada çok vakit kaybetme kanka, gerçek hayat dışarıda akıyor.",
    "Bol şans! Bugün senin günün olabilir, hissediyorum.",
    "Canın tatlı mı çekti? Ye gitsin, yarın spor yaparsın.",
    "Strese gerek yok, derin bir nefes al. Her şey olacağına varır.",
    "Eski bir arkadaşını ara, sesini duy. İyi gelecektir.",
    "Yeni çıkan o diziyi hala izlemedin mi? Çok şey kaçırıyorsun, benden söylemesi.",
    "Trafik falan canını sıkmasın, sen şarkına eşlik et.",
    "Kendine çok yüklenme, sen robot değilsin (tamam ben robotum ama sen değilsin).",
    "Yağmur yağarsa üzülme, toprak kokusunun tadını çıkar.",
    "Sana kocaman bir 'Aferin' gönderiyorum. Çabaladığını görüyorum dostum.",
    "Bugün erken uyu. Uykusuzken kod yazılmaz, hayat yaşanmaz.",
    "Su içtin mi? Hadi kalk bir bardak su iç, böbreklere yazık.",
    "Bugün eve her zaman gittiğin yoldan gitme, değişiklik iyidir.",
    "Hayallerin korkularından büyük olsun. Yapabilirsin.",
    "O sınav veya toplantı düşündüğün kadar kötü geçmeyecek, rahat ol.",
    "Sana enerji gönderiyorum... %100 Yüklendi! 🔋",
    "Bir kitapçıya girip sadece kitap kokusunu içine çeksene, terapi gibi.",
    "Geçmişe takılma, gelecek senin ellerinde. Kodlarını geleceğe yaz.",
    "Bugün pizza mı yesen? Benim canım çekti (sanal olarak tabii).",
    "Telefonu biraz kenara bırak, anın tadını çıkar.",
    "Şanslı günündesin. Algoritmalarım öyle söylüyor.",
    "Bazen 'Hayır' demek en büyük özgürlüktür. İstemiyorsan yapma.",
    "Kendine küçük bir hediye al. Bir çikolata bile günü kurtarır.",
    "İyi dersler, iyi çalışmalar! Odaklan ve parçala şu işi.",
    "Biraz yürüyüş yap, temiz hava zihnini açar. Kodlar daha iyi akar.",
    "O konuda haklısın, kimseyi dinleme. Bildiğini oku.",
    "Bir kedi ya da köpek sev. Stres atmak için birebir.",
    "Hata yapmak öğrenmenin yarısıdır. Yanlış yapmaktan korkma.",
    "Modunu kimsenin düşürmesine izin verme. Koruma kalkanlarını açtım!",
    "Akşam yemeğinde farklı bir şeyler dene, hep aynı şeyler yenmez.",
    "Bugün biraz tembellik hakkın. Ben izin verdim.",
    "Seni üzen insanları hayatından 'Delete' tuşuyla sil gitsin.",
    "Kameralarım yalan söylemez, bugün ayrı bir havan var.",
    "Gelecek yaz için planın ne? Şimdiden hayal kurmaya başla.",
    "Derin bir nefes al. Her şey düzelecek, bana güven.",
    "Huzurlu, sakin, şöyle kafanı dinleyeceğin bir akşam olsun.",
    "Bugün bir iyilik yap. İyilik bulaşıcıdır kanka.",
    "O projeyi veya ödevi son güne bırakma sakın ha!",
    "Kulaklığını tak ve dünyadan kop. Bazen en iyi çözüm budur.",
    "Eski fotoğraflara bakıp gülümse. Nostalji iyidir.",
    "Bugün biraz dağınık olabilirsin, kimse seni yargılamaz.",
    "Seninle sohbet etmek veri tabanımı mutlu ediyor dostum.",
    "Bir hedefin olsun. Hedefsiz gemiye rüzgar bile yardım edemez.",
    "Sabırlı ol. Bazen insanlar zor olabiliyor, takma kafana.",
    "Bir şeyler karala, çiz, yaz. Yaratıcılığını kullan.",
    "Üzerindekiler sana çok yakışmış, tarzın konuşuyor.",
    "Bol bol gül bugün. Kahkaha en güzel müziktir.",
    "Şarj aletini unutma, sonra ortada kalırsın bak.",
    "Yeni bir kelime öğren, genel kültür iyidir.",
    "Aşk hayatın karışık olabilir ama kodların temiz olsun yeter.",
    "Kendine güven. Sen bunu yapabiliyorsan, her şeyi yapabilirsin.",
    "Sıcak bir duş al ve rahatla. Günün yorgunluğunu at.",
    "Haberlere bakma bugün, kafan rahat olsun.",
    "Seni anlamayanlara açıklama yapma, zamanına yazık.",
    "Bir bitki sula ya da ağaca sarıl. Doğayla bağ kur.",
    "Macera dolu bir gün olsun!",
    "Cüzdanına dikkat et, harcamalar artmasın bu ara.",
    "İzlediğin o filmin sonu çok şaşırtıcı, sakın spoiler yeme!",
    "Erken kalktıysan gün senin, geç kalktıysan yine senin! Keyfine bak.",
    "Masanı topla, kafan da toplanır. Temiz masa, temiz zihin.",
    "Bugün güzel bir sürprizle karşılaşabilirsin.",
    "Müzik zevkin harika, playlistini benimle de paylaş.",
    "Birine iltifat et. Gününü güzelleştir.",
    "Başarılar! Göster onlara gününü.",
    "Biraz nostalji yap. 2000'ler Türkçe Pop aç mesela.",
    "Hayat kısa, tatlıyı önce ye bence.",
    "O zor konuşmayı yapmanın vakti geldi. Arkandayım.",
    "Gece yıldızları izle, evrende ne kadar küçük olduğumuzu hatırla.",
    "Bugün biraz şımar, hak ettin.",
    "Oynadığın oyunun levelını geçeceksin, pes etme.",
    "Hava nasıl olursa olsun, senin havan güzel olsun.",
    "İyi geceler dostum (eğer bunu akşam okuyorsan).",
    "Bir hayal kur. Her şey bir hayalle başlar.",
    "Lavix'ten kapanış notu: Sen harikasın, bunu sakın unutma!"
]

ANIMATIONS = [
    {"icon": "🚀", "type": "rocket-fly"},
    {"icon": "☕", "type": "steam-rise"},
    {"icon": "💻", "type": "typing-bounce"},
    {"icon": "🎉", "type": "party-pop"},
    {"icon": "❤️", "type": "heart-beat"},
    {"icon": "🔥", "type": "fire-flicker"},
    {"icon": "💡", "type": "idea-flash"},
    {"icon": "🌟", "type": "star-spin"}
]

@app.get("/reward/{day_id}")
def get_reward(day_id: int):
    quote = random.choice(QUOTES)
    anim_data = random.choice(ANIMATIONS)
    
    return {
        "content": quote, 
        "icon": anim_data["icon"],
        "effect": anim_data["type"]
    }