# Reverse Engineering the Branch Target Buffer Organizations on Apple M2 #

## How to Run ##

Follow the steps below to execute the script.

### 1) Set the device environment variable ###

First, export the `M1N1DEVICE` variable so the script can find your connected device:

```bash
export M1N1DEVICE=/dev/cu.usbmodemQ6MRQYX6W11
```
Make sure the device path is correct for your system.
You can check available devices under /dev/ if needed.

### 2) Run the script ###

After setting the environment variable, run the Python script:

```bash
./re_m2_btb_size.py
```

### Reference / Acknowledgement ###

This implementation was developed with reference to the m2e project:
https://github.com/eigenform/m2e
