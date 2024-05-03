# MicroPython for M5Stack TOUGH

This repository adds a board definition for the [M5Stack Tough](https://shop.m5stack.com/products/m5stack-tough-esp32-iot-development-board-kit?variant=40644956160172) for use with `lv_micropython`.

## Developing

> [!NOTE]
> These instructions assume you are working on a Mac with Apple silicon. For different architectures or operating systems, it may be helpful to start from [LV-MicroPython's setup documentation](https://github.com/lvgl/lv_micropython/blob/master/ports/esp32/README.md#setting-up-the-toolchain-and-esp-idf).

### Setup

Clone this repository:

```sh
git clone https://github.com/solanus-systems/micropython-m5tough.git
```

Clone LV-MicroPython, including its submodules:

```sh
git clone --recursive https://github.com/lvgl/lv_micropython.git
```

Clone esp-idf, including its submodules, using the latest version known to work with LV-MicroPython:

```sh
git clone -b v4.4.6 --recursive https://github.com/espressif/esp-idf.git
```

Install esp-idf:

```sh
# in esp-idf/
./install.sh
```

Install cmake using Homebrew:

```sh
brew install cmake
```

Link the m5tough custom board definition into the LV-MicroPython boards directory:

```sh
ln -s /path/to/micropython-m5tough/boards/M5TOUGH /path/to/lv_micropython/ports/esp32/boards/M5TOUGH
```

Build the micropython cross-compiler:

```sh
# in lv_micropython/
make -C mpy-cross
```

### Compiling

Ensure the ESP-IDF environment is set up:

```sh
# in esp-idf/
source ./export.sh
```

Compile the firmware:

```sh
# in lv_micropython/ports/esp32
make submodules
make BOARD=M5TOUGH all
```

### Flashing

> [!NOTE]
> Check the port name of your M5Tough before running the following commands. You
> can find it by running `ls /dev/tty.usb*` in the terminal when the M5 is connected
> to your computer via USB cable.

Erase existing firmware on the M5Tough (if e.g. UIFlow is currently installed):

```sh
# in lv_micropython/ports/esp32
esptool.py --port /dev/tty.usbserial-54D80277501 --baud 115200 --before default_reset --after hard_reset --chip esp32 erase_flash
```

Deploy the firmware to the M5Tough:

```sh
# in lv_micropython/ports/esp32
esptool.py --port /dev/tty.usbserial-54D80277501 --baud 115200 --before default_reset --after hard_reset --chip esp32 write_flash -z 0x1000 build-M5TOUGH/firmware.bin
```

idf.py build

make erase (if this is the first time uploading the firmware)

### Updating

To update the micropython version, you need to perform these steps in the lv_micropython directory:

```sh
git checkout v1.20.0 # or the version you want to update to
git submodule update --recursive
make -C mpy-cross
```

The process to update esp-idf is similar:

```sh
git checkout release/v4.4 # or the version you want to update to
git submodule update --recursive
./install.sh
```

Then, you can build the firmware as described above.

## See Also

- https://github.com/russhughes/ili9342c_mpy
