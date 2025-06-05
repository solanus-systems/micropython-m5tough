name = "m5tough"


class M5Tough:
    def __init__(self):
        # Init LVGL
        import lvgl as lv

        lv.init()

        # Power Management
        from power import Power

        self.power = Power()

        # LCD screen
        from ili9XXX import ili9341

        self.display = ili9341(
            mosi=23,
            miso=38,
            clk=18,
            dc=15,
            cs=5,
            invert=True,
            rot=0x10,
            width=320,
            height=240,
            half_duplex=False,
            rst=-1,
            power=-1,
            backlight=-1,
        )

        # Touch sensor
        from ft6x36 import ft6x36

        self.touch = ft6x36(i2c_dev=1, width=320, height=280)

        # SD reader
        # TODO
