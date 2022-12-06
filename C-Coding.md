# C-Programmieren
 +{0b1001, 0b1010, 0b0110, 0b0101}; (Schrittmotor)
 ## Daten-Typen
 Nummerische-Datentypen
  * int8_t  (Größe: 1Byte) (0 - 255)
  * uint8_t (Größe: 1Byte) (-128 - 127)
  * int16_t  (Größe: 2Byte) (0 - 65535)
  * uint16_t (Größe: 2Byte) (-32768 - 32767)
  ---
 ## PORTs
  * PORT0 (Schalter)
  * PORT1 (LED / 7-Seg / Schrittmotor)
  * PORT2 (nix)
  * PORT3 (Interrupt taster)
  ---
 ## INIT_Funktionen
  Alle initialisierungs Funktionen:
  * lcd_init();
  * adc_init();
  * byte_init(PORTx, IN/OUT);
  * bit_init(PORTx, 0-8, IN/OUT) ;
  ---
 ## PIN IN/OUT
  Bit I/O (Ein pin von PORT)
  * bit_write(PORTx, 0-8, value);
  * uint8_t value = bit_read(PORTx, 0-8);
  ---
  Byte I/O (Gesamter PORT)
  * byte_write(PORTx, value);
  * uint8_t value = byte_read(PORTx, value);
 ---
 ## LCD-Screen
  Steuerung des LCD-Display's
  * lcd_clear();
  * lcd_setcursor(row, col);     <--(Fängt bei 1 an!)
  * lcd_print("Hello World"); <--(gibt string an aktueller Stelle aus)
  * lcd_int(); <--(0 - 255 | gibt int an aktueller stelle aus)
  * lcd_byte(); <--(0 - 65535)
  * lcd_char(); <--(0 - 255 als ascii-zeichen)
 ---
 ## AD-Wandler
  Abfrage des AD-Wandlers
  * adc_in1();
  * adc_in2();
 ## Delay
  Funktionen für ein Delay
  * delay_ms(ms); 
  * delay_100us(us);
 ## Swich-Case
  * 
  