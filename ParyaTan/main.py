from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapView
from kivy.core.window import Window

Window.size = (360,800)

screen_helper = """

ScreenManager:
    MenuScreen:
    TempleScreen:
    OmkarScreen:
    BhagScreen:
    TalaScreen:
    PadiScreen:
    GoldScreen:
    MruScreen:
    WaterScreen:
    AbbScreen:
    IruScreen:
    MalScreen:
    CheScreen:
    NapScreen:
    DevScreen:
    FueScreen:
    FoodScreen:
    GrowScreen:
    WineScreen:
    RentScreen:
    MapScreen:
    HospScreen:


<MenuScreen>:
    name: 'menu'
    MDIconButton:
        icon: 'nut'
        pos_hint:{'center_x' :0.9, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
    Image:
        source: "back.jpg"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
    Image:
        source: "logo.png"
        size_hint: 0.55,0.55
        pos_hint: {'center_x' :0.5, 'center_y' :0.87}
    ScrollView:
        do_scroll_x: True
        pos_hint: {'center_x':0.48,'center_y':0.73}
        size_hint: 1,0.1
        BoxLayout:
            orientation: 'horizontal'
            size_hint_x: None
            width: 2150
            padding: "20dp"
            spacing: "40dp"
            MDIconButton:
                on_press: root.manager.current = 'fue'
                Image:
                    source: "gas.png"
                    size_hint: 2.3,2.3
            MDIconButton:
                on_press: root.manager.current = 'food'
                Image:
                    source: "food.png"
                    size_hint: 2.3,2.3
            MDIconButton:
                on_press: root.manager.current = 'grow'
                Image:
                    source: "grocery.png"
                    size_hint: 2.3,2.3
            MDIconButton:
                on_press: root.manager.current = 'wine'
                Image:
                    source: "wine.png"
                    size_hint: 2.3,2.3
            MDIconButton:
                on_press: root.manager.current = 'rent'
                Image:
                    source: "rent.png"
                    size_hint: 2.3,2.3
            MDIconButton:
                on_press: root.manager.current = 'hosp'
                Image:
                    source: "medi.png"
                    size_hint: 2.3,2.3
            MDRectangleFlatButton:
                text: 'Bamboo Shoot'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                md_bg_color: 143/255,177/255,236/255,1
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
            MDRectangleFlatButton:
                text: 'Noolputtu'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                md_bg_color: 230/255,155/255,253/255,1
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
            MDRectangleFlatButton:
                text: 'Curd Rice'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                md_bg_color: 236/255,171/255,143/255
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
            MDRectangleFlatButton:
                text: 'Jackfruit'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                md_bg_color: 143/255,177/255,236/255,1
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.57}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'temple'
        Image:
            source: "temple.png"
            size_hint: 1.3,1.3
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.57}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'water'
        Image:
            source: "water.png"
            size_hint: 1.3,1.3
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        Image:
            source: "mountain.png"
            size_hint: 1.3,1.3
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        Image:
            source: "resort.png"
            size_hint: 1.3,1.3
    MDRectangleFlatButton:
        text: 'Rafting'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "25sp"
        pos_hint: {'center_x':0.5,'center_y':0.09}
        size_hint: 0.88,0.1
        md_bg_color: 159/255,0/255,255/255,1
        Image:
            source: "rafting.png"
            size_hint: 1.45,1.33
            
    MDIconButton:
        pos_hint: {'center_x':0.5,'center_y':0.21}
        on_press: root.manager.current = 'map'
        Image:
            source: "google-maps.png"
            size_hint: 2.5,2.5

    
    

    
<MapScreen>:
    name: 'map'
    MapView:
        id: map_view
        lat: 12.4244
        lon: 75.7382
        zoom: 15
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    
            
            
<TempleScreen>:
    name: 'temple'
    Image:
        source: "back1.jpg"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    MDLabel:
        text: 'Temples'
        pos_hint: {'center_x' :0.5, 'center_y' :0.90}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.5
        font_style : 'Button'
        font_size: '40sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.45}
        size_hint: 1,0.8
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 750
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                text: 'Omkareshwar Temple'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 94/255,140/255,255/255,1
                text_color: 1,1,1,1
                font_size: "50sp"
                font_style: 'H6'
                on_press: root.manager.current = 'omkar'
            MDRectangleFlatButton:
                text: 'Bhagandeshwara Temple'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'H6'
                size_hint: 0.88,0.1
                md_bg_color: 94/255,140/255,255/255,1
                on_press: root.manager.current = 'bhag'
            MDRectangleFlatButton:
                text: 'Talakaveri Temple'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'H6'
                size_hint: 0.88,0.1
                md_bg_color: 94/255,140/255,255/255,1
                on_press: root.manager.current = 'tala'
            MDRectangleFlatButton:
                text: 'Padi Igguthappa Temple'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'H6'
                size_hint: 0.88,0.1
                md_bg_color: 94/255,140/255,255/255,1
                on_press: root.manager.current = 'padi'
            MDRectangleFlatButton:
                text: 'Golden Temple' 
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 94/255,140/255,255/255,1
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'H6'
                on_press: root.manager.current = 'gold'
            MDRectangleFlatButton:
                text: 'Mruthunjaya Temple'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'H6'
                size_hint: 0.88,0.1
                md_bg_color: 94/255,140/255,255/255,1
                on_press: root.manager.current = 'mru'

<OmkarScreen>:
    name:'omkar'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'temple'
    Image:
        source: "omkar.jpg"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Omkareshwar Temple'
        pos_hint: {'center_x' :0.5, 'center_y' :0.6}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.32}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'Built in 1820 CE by Lingarajendra, Omkareshwar Temple is one of the popular and ancient shrines located in Coorg. Dedicated to Lord Shiva, it is one of the must-include places in Coorg Tour Packages. The Shivalinga installed inside the temple is believed to be brought from the divine land of Kashi. Constructed in both Islamic and Gothic style of architecture, the structure of the temple comprises of a large central dome with four minarets standing at four corners. The walls are decorated with intriguing paintings and the bars of the windows were made of Panchaloha. Surrounded by a beautiful pond, the temple is frequented by thousands of local devotees and tourists who come here to catch a glimpse of the pristine Shivalinga placed inside the sanctum. The main festival here is Mahashivaratri that is celebrated with much fervor.' 
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'

<BhagScreen>:
    name:'bhag'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'temple'
    Image:
        source: "bhag.jpg"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Bhagandeshwara Temple'
        pos_hint: {'center_x' :0.5, 'center_y' :0.6}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.3}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'Bhagandeshwara Temple, also known as Bhagundeshwara Kshetra is an ancient sacred shrine situated in the Bhagamandala village. It is one of the famous places of pilgrimage in Karnataka. he confluence of three rivers namely Kaveri, Sujyoti and Kannike is well-known as Triveni Sangama and also considered as Dakshina Kashi. Also, there is a practice that pilgrims to take a dip in the sangama and perform rituals to their ancestors before proceeding to Talacauvery. Enclosed with huge walls and facing east, the temple complex is said to have been built by the Cholas prior to the 11th century follows the gabled roof style of the Kerala temple architecture. Apart from Bhagandeshwara, one can also see the beautiful sculptures of Lord Narayana, Lord Ganesha, and Lord Subramanya. The temple attracts huge crowd during the Thula Sankramana jatra and the entire Thula month (October-November) in which thousands of oil lamps are lit in the temples.' 
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'
                    
<TalaScreen>:
    name: 'tala'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'temple'
    Image:
        source: "tala.jpg"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Talakaveri Temple'
        pos_hint: {'center_x' :0.5, 'center_y' :0.6}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.3}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'Talakaveri or Talacauvery is the place that is generally considered to be the source of the river Kaveri and a holy place for many Hindus. It is located on Brahmagiri hills near Bhagamandala in Kodagu district (Coorg), in the South Indian state of Karnataka. It is located close to the border with Kasaragod district, Kerala. Talakaveri stands at a height of 1,276 meters above sea level. Despite its traditional status as the source of the Kaveri, there is no permanent visible flow from this place to the main rivercourse, except during the monsoon rains.The river originates as a spring feeding this tank, which is considered to be a holy place to bathe on special days. The waters are then said to flow underground to emerge as the Kaveri river some distance away. The temple has been renovated extensively, most recently in 2007 by the state government.' 
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'
                    
<PadiScreen>:
    name: 'padi'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'temple'
    Image:
        source: "padi.jpg"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Padi Igguthappa Temple'
        pos_hint: {'center_x' :0.5, 'center_y' :0.6}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.32}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'This temple is considered to be one of the ancient ones as it was constructed by the king Lingarajendra in 1810 in the town of Kakkabe. It is situated in the Igguthappa Devara betta in the Aiyengeri forest that is around 45 km away from Madikeri. The architecture of the temple is similar to those of the ancient Keralite temples. It is quite significant to the locals of Coorg, as the temple dignifies Lord Igguthappa or Lord Subramanya, who is deemed to be their chief instructor as well as the lord of crops and rain. The best time to visit this temple might be the one when the annual festival is conducted, i.e. in the month of March, during which worshippers from all parts collectively offer their devotion and prayers to the Lord who is known to fulfil all the desires if prayed with genuine devotion and a true heart, followed by numerous dance performances afterwards.' 
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'
                    
<GoldScreen>:
    name: 'gold'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'temple'
    Image:
        source: "gold.jpg"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Golden Temple'
        pos_hint: {'center_x' :0.5, 'center_y' :0.6}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.32}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'The Namdroling Monastery, popularly referred to as ‘The Golden Temple’ is one of the largest Tibetan settlements in India. Located in Bylakuppe, about 5 kms from Kushalanagara in Kodagu district, The Golden Temple complex is home to about 16000 refugees and 600 monks. Namdroling Monastery’s main entrance is an attractive four story tower with a wheel portraying symbols of Buddhism. The main attractions inside the temple are the statues of Lord Buddha in the centre with statues of Lord Amitayus and Lord Padmasambhava on either sides. Visitors can pray, meditate, give their offerings and rotate the mani prayer drums. Rotating these prayer drums is believed to give the same benefit as chanting “Om Mani Padme Hum”, the Buddhist prayer. There is also a Tibetan shopping center that stands just opposite the Golden Temple where you can buy jewellery etc.' 
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'
                    
<MruScreen>:
    name: 'mru'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'temple'
    Image:
        source: "mru.JPG"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Mruthunjaya Temple'
        pos_hint: {'center_x' :0.5, 'center_y' :0.6}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.32}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'Mrithunjaya temple is one of the major temple of tourist attraction in Kodagu. This temple belongs to God Shiva and popular temple locally. A place filled with holiness and divinity,  is a destination for those who are searching for peace and serenity in the lap of nature. Sri Mrithunjaya Temple is surrounded by coffee plantation in the spacious place with a garden, and very calm place. The fresh air, unpolluted environment and majestic landscapes are the inviting features to tourists. This  temple is situated amidst nature which is a feast to the eyes. In addition to all these, this temple is located in a peaceful yet beautiful area. Usually this place will be less crowded during the weekdays. There are many different  poojas that is being done in this temple , few of which include, Navagraha pooja, Rudrabisheka, Sri Sathya narayana pooja, Vasantha pooja, Ekhadasha pooja, Vahana pooja.' 
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'
                    
                    
<WaterScreen>:
    name: 'water'
    Image:
        source: "back2.jpg"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    MDLabel:
        text: 'Waterfalls'
        pos_hint: {'center_x' :0.5, 'center_y' :0.90}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.5
        font_style : 'Button'
        font_size: '40sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.45}
        size_hint: 1,0.8
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 750
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                text: 'Abbey Falls'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 27/255,79/255,114/255,1
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'H6'
                on_press: root.manager.current = 'abb'
            MDRectangleFlatButton:
                text: 'Iruppu Falls'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'H6'
                size_hint: 0.88,0.1
                md_bg_color: 27/255,79/255,114/255,1
                on_press: root.manager.current = 'iru'
            MDRectangleFlatButton:
                text: 'Mallalli Falls'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'H6'
                size_hint: 0.88,0.1
                md_bg_color: 27/255,79/255,114/255,1
                on_press: root.manager.current = 'mal'
            MDRectangleFlatButton:
                text: 'Chelavara Falls'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'H6'
                size_hint: 0.88,0.1
                md_bg_color: 27/255,79/255,114/255,1
                on_press: root.manager.current = 'che'
            MDRectangleFlatButton:
                text: 'Napandapole Falls' 
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 27/255,79/255,114/255,1
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'H6'
                on_press: root.manager.current = 'nap'
            MDRectangleFlatButton:
                text: 'Devaragundi Falls'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'H6'
                size_hint: 0.88,0.1
                md_bg_color: 27/255,79/255,114/255,1
                on_press: root.manager.current = 'dev'
                
<AbbScreen>:
    name: 'abb'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'water'
    Image:
        source: "abb.jpg"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Abbey Falls'
        pos_hint: {'center_x' :0.5, 'center_y' :0.6}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.32}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'Abbey Falls (also spelled Abbi Falls and Abbe Falls) is a waterfall in Kodagu, in the Western Ghats of Karnataka, India. It is located 8 km from the Madikeri, 122 km from Mysore, 144 km from Mangalore and 268 km from Bangalore. The waterfall is on the early reaches of the river Kaveri, located between private coffee plantations with stocky coffee bushes and spice estates and trees entwined with pepper vines. There is a hanging bridge constructed just opposite the falls. Flow is much higher during the monsoon season. The falls was earlier called Jessi Falls, named after a British officers wife. However, the place was a thick jungle back then. Years later, the waterfall was discovered by Mr. Neravanda B. Nanaiah who bought the place from the government and converted it into a coffee and spice plantation, which still surrounds the waterfall today.' 
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'
                    
<IruScreen>:
    name: 'iru'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'water'
    Image:
        source: "iru.jpeg"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Iruppu Falls'
        pos_hint: {'center_x' :0.5, 'center_y' :0.6}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.32}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'The Irupu Falls (also Iruppu Falls) are located in the Brahmagiri Range in the Kodagu district of Karnataka, India, bordering the Wayanad district of Kerala. It is a fresh water cascade and is situated at a distance of 48 km from Virajpet on the highway to Nagarhole. The falls are also known as the Lakshmana Tirtha Falls, derived from the name of the tributary of Cauvery which starts from these falls, the Lakshmana Tirtha River. A forest trail leads from these falls to the Brahmagiri Peak in Southern Kodagu. Irupu falls is a major tourist attraction as well as a pilgrimage spot. A famous Shiva temple, the Rameshwara Temple is situated on the banks of the Lakshmana Tirtha River, en route to the Falls. This temple attracts many pilgrims during the festival of Shivaratri. The best time to visit the falls is during the monsoons, when the falls is at full capacity and is a breathtaking sight.' 
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'
                    

<MalScreen>:
    name: 'mal'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'water'
    Image:
        source: "mal.jpg"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Mallalli Falls'
        pos_hint: {'center_x' :0.5, 'center_y' :0.59}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.32}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'Mallalli Falls is a waterfall located in the Western Ghats of India, in Coorg, Karnataka. The falls are formed by the waters of River Kumaradhara, which originates on the Western Ghats. After plunging down the location of the falls, the river water flows down towards Mangalore passing through Kukke Subrahmany. The river then merges with River Netravati before flowing into the Arabian Sea. Mallalli Falls is one of the most mystifying waterfalls in Coorg and one of the best tourist places in Coorg, Karnataka. These falls lie 26 kilometres from the town of Somwarpet at the foot of the Pushpagiri Hills. Travellers can drive from Somwarpet to Kalahali Road which is a 10-kilometre drive. Beyond Kalahali Road, the route narrows down, just enough for a small car to pass. ' 
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'
                    
                    
<CheScreen>:
    name: 'che'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'water'
    Image:
        source: "che.jpg"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Chelavara Falls'
        pos_hint: {'center_x' :0.5, 'center_y' :0.6}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.32}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'Chelvara Falls is a natural waterfall formed by small stream, a tributary of Kaveri near Cheyyandane village which is on Virajpet - Talakaveri State Highway (SH 90) around 16 km from Virajpet, in the state of Karnataka, India. It is located on the way to Kabbe Holidays Homestay and is near Thadiyandamol, the highest point in Kodagu. The falls is visible after walking 200 meters into the forest from the place available for parking. One can easily get into dangerous waters and pulled in. It is approximately 100 feet deep. There are danger signs all over. Locals advise not getting into the water. About 20 people have died here. Chelavara falls is the perfect getaway for nature and adventure lovers and also escape from boredom city life. There is also a nearby viewpoint which is around 2 km from this place and worth a visit. '
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'
                    

<NapScreen>:
    name: 'nap'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'water'
    Image:
        source: "nap.jpg"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Napandapole Falls'
        pos_hint: {'center_x' :0.5, 'center_y' :0.6}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.32}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'This waterfall is truly a treasure to unravel. If you are a true explorer and an adventurous soul, you will love the torrential flow of the Napandapole Falls, dropping from 120 feet, lying at the foothills of the Kote Betta peak. Surrounded by three smaller waterfalls, and set in rocky terrain, this cascade is a great site for rappelling and invites adventurers from all over. There are plenty of unexplored corners around the falls, which also make for a great hiking destination. They are the best pick to enjoy a short break from everyday hustle and bustle. Napandapole is a rock-strewn valley, where the river flows fenced by forest. Tucked amidst the rocky terrain and forest area, these falls make a gorgeous picnic spot. You will have the time of your life here at this spot. Do not miss going to this place at any cost.'
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'
                    
                    
<DevScreen>:
    name: 'dev'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'water'
    Image:
        source: "dev.jpg"
        size_hint: 0.8,0.4
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDLabel:
        text: 'Devarakolli Falls'
        pos_hint: {'center_x' :0.5, 'center_y' :0.6}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        font_style : 'H6'
        font_size: '20sp'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.32}
        size_hint: 1,0.5
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 800
            padding: "20dp"
            spacing: "25dp"
            MDFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.88,0.1
                md_bg_color: 1,1,1,1
                MDLabel:
                    text: 'Compared to other waterfalls that you visit here, Devarakolli Falls is quite smaller. But if you are a big fan of a very beautiful trek with some scenic environment, then this should definitely be your pick while you are in Coorg. The dense forestland with the water falling from a high altitude is such a serene and calming sight that you will get to watch. The beauty of this waterfall lies with the tall, towering trees with lush greenery surrounding. Along with this, a clear pool of water in the foot of the waterfalls perfectly sets you up for a great experience. From the Coorg main bus stand, it will just take 30 minutes to reach this falls. Visit this waterfall for it being one of the best treks to the waterfalls in Coorg. Though, the height is too low that is, 75 feet but still this waterfall showcases breathtakingly beautiful views.'
                    theme_text_color: "Custom"
                    text_color: 0,0,0,1
                    font_size: "18sp"
                    font_style: 'H6'
                    
<FueScreen>:
    name: 'fue'
    Image:
        source: "fuel.jpg"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
        
        
        
        
        
        
        
<FoodScreen>:
    name: 'food'
    Image:
        source: "food.jpg"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    
        
        
        
        
        
        
<GrowScreen>:
    name: 'grow'
    Image:
        source: "grow.jpg"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
        
        
        
        
<WineScreen>:
    name: 'wine'
    Image:
        source: "wine.jpg"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
        
        
        
        
<RentScreen>:
    name: 'rent'
    Image:
        source: "rent.jpg"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
        
        
        
<HospScreen>:
    name: 'hosp'
    Image:
        source: "hosp.jpg"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    
"""


class MenuScreen(Screen):
    pass

class TempleScreen(Screen):
    pass

class OmkarScreen(Screen):
    pass

class BhagScreen(Screen):
    pass

class TalaScreen(Screen):
    pass

class PadiScreen(Screen):
    pass

class GoldScreen(Screen):
    pass

class MruScreen(Screen):
    pass

class WaterScreen(Screen):
    pass

class AbbScreen(Screen):
    pass

class IruScreen(Screen):
    pass

class MalScreen(Screen):
    pass

class CheScreen(Screen):
    pass

class NapScreen(Screen):
    pass

class DevScreen(Screen):
    pass

class FueScreen(Screen):
    pass

class FoodScreen(Screen):
    pass

class GrowScreen(Screen):
    pass

class WineScreen(Screen):
    pass

class RentScreen(Screen):
    pass

class MapScreen(Screen):
    pass

class HospScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(TempleScreen(name='temple'))
sm.add_widget(OmkarScreen(name='omkar'))
sm.add_widget(BhagScreen(name='bhag'))
sm.add_widget(TalaScreen(name='tala'))
sm.add_widget(PadiScreen(name='padi'))
sm.add_widget(GoldScreen(name='gold'))
sm.add_widget(MruScreen(name='mru'))
sm.add_widget(WaterScreen(name='water'))
sm.add_widget(AbbScreen(name='abb'))
sm.add_widget(IruScreen(name='iru'))
sm.add_widget(MalScreen(name='mal'))
sm.add_widget(CheScreen(name='che'))
sm.add_widget(NapScreen(name='nap'))
sm.add_widget(DevScreen(name='dev'))
sm.add_widget(FueScreen(name='fue'))
sm.add_widget(FoodScreen(name='food'))
sm.add_widget(GrowScreen(name='grow'))
sm.add_widget(WineScreen(name='wine'))
sm.add_widget(RentScreen(name='rent'))
sm.add_widget(MapScreen(name='map'))
sm.add_widget(HospScreen(name='hosp'))


class PrayaTanApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def show_map(self):
        map_view = self.root.ids.map_view
        map_view.lat = 37.7749
        map_view.lon = -122.4194
        map_view.zoom = 10

if __name__ == "__main__":
    PrayaTanApp().run()