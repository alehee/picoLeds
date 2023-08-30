# picoLeds

<p align="center">
  <img src="https://github.com/alehee/picoLeds/blob/main/bar.jpg">
</p>

## Description

System of WS2812B leds controled by Raspberry Pico W using API server hosted on the Pico device.

## Used technology

Languages:

- MicroPython

Leds library:

- blaz-r [pi_pico_neopixel](https://github.com/blaz-r/pi_pico_neopixel)

## Download

You can download the master branch with code.

## How to use

1. Rename `config_template.json` to `config.json` and fill all the data
   - _endpointUrl_ points to the endpoint where Pico W will sync his IP address. Comment if not needed. My that kind of endpoint example is located below.
   - _pin_ is the number of Pico W output pin where board communicate with led strip.
2. Upload the code to the Pico W device.
3. Connect led strip with the Pico W and start the system!

## API Documentation

Here's the endpoints that system handles at the moment.

API response will be _200 OK_ if the call will be accurate and realizable. Otherwise the response will be _400 Bad request_ with error message.

### Color

`GET /color/hex`

    curl --location 'http://192.168.1.2/color/ff0000'

Changes strip color to desired hex. This example will change the color to red.

### Brightness

`GET /brightness/0-255`

    curl --location 'http://192.168.1.2/color/50'

Changes brightness of the led strip. Scale of the brightness if 0-255.

### Turning on/off

`GET /turn/on or off`

    curl --location 'http://192.168.1.2/turn/off'

Changes the strip color to black so practically it will turn the lights off. To turn it on just change the _off_ to _on_!

## Pico W IP endpoint example

```
<?php

$THE_ID = "RYBNICKALEDS";
$FILENAME = "leds.json";

if(isset($_GET["id"]) && isset($_GET["ip"]) && $_GET["id"] == $THE_ID) {
    $obj = array();

    $obj["id"] = $_GET["id"];
    $obj["ip"] = $_GET["ip"];
    $obj["timestamp"] = date("Y-m-d H:i:s");

    $json = json_encode($obj, JSON_PRETTY_PRINT);
    $fp = fopen($FILENAME, 'w');
    fwrite($fp, $json);
    fclose($fp);

    unset($_GET["id"]);
    unset($_GET["ip"]);

    echo "OK";
}
```

## Thank you!

Thank you for peeking at my project!

If you're interested check out my other stuff [here](https://github.com/alehee)
