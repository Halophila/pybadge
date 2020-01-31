from adafruit_pybadger import PyBadger

pybadger = PyBadger()

pybadger.show_badge(name_string="Jason", hello_scale=1, hello_font="fonts/Noto-18.bdf",my_name_is_scale=2, name_scale=3)

while True:
    pybadger.auto_dim_display(delay=10)
    if pybadger.button.a:
        pybadger.show_business_card(image_name="pics/face.bmp", name_scale=2)
    elif pybadger.button.b:
        pybadger.show_business_card(image_name="pics/vcard.bmp", name_scale=2)
    elif pybadger.button.start:
        pybadger.show_badge(name_string="Jason", hello_scale=1, hello_font="fonts/Noto-18.bdf",my_name_is_scale=2, name_scale=3)
    elif pybadger.button.up:
        pybadger.show_qr_code(data="https://www.choptanktransport.com")
