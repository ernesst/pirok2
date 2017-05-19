#!/usr/bin/python

import time # pour tempo 1s
import mydigole #for digole screen 

# Parametres font / couleur
cBlanc = 254
cBleu = 0x32 #2
cRouge = 0xC4 #224
cVert = 28
fBig=200
fSmall=201

welcomelogo = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x7c,0x00,0x00,0x00,0x1f,0x80,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x07,0xff,0xf0,0x00,0x07,0xff,0xf0,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x7f,0xff,0xfc,0x00,0x0f,0xff,0xff,0x00,0x00,0x00,0x00
,0x00,0x00,0x03,0xff,0xdd,0xff,0x00,0x7f,0xed,0xff,0xe0,0x00,0x00,0x00
,0x00,0x00,0x07,0xf6,0x00,0x3f,0xc0,0xff,0x00,0x1f,0xf0,0x00,0x00,0x00
,0x00,0x00,0x07,0xe0,0x00,0x07,0xc1,0xf0,0x00,0x01,0xf8,0x00,0x00,0x00
,0x00,0x00,0x07,0x00,0x00,0x00,0xe3,0xc0,0x00,0x00,0x38,0x00,0x00,0x00
,0x00,0x00,0x07,0x00,0x00,0x00,0x73,0x80,0x00,0x00,0x78,0x00,0x00,0x00
,0x00,0x00,0x07,0x00,0x00,0x00,0x77,0x00,0x00,0x00,0x78,0x00,0x00,0x00
,0x00,0x00,0x07,0x00,0x00,0x00,0x3f,0x00,0x00,0x00,0x38,0x00,0x00,0x00
,0x00,0x00,0x07,0x00,0x00,0x00,0x3e,0x00,0x00,0x00,0x78,0x00,0x00,0x00
,0x00,0x00,0x07,0x00,0x08,0x00,0x1e,0x00,0x0c,0x00,0x70,0x00,0x00,0x00
,0x00,0x00,0x07,0x00,0x06,0x00,0x1e,0x00,0x18,0x00,0x70,0x00,0x00,0x00
,0x00,0x00,0x03,0x80,0x01,0x80,0x1e,0x00,0x60,0x00,0xf0,0x00,0x00,0x00
,0x00,0x00,0x03,0xc0,0x00,0xe0,0x1e,0x01,0xc0,0x00,0xe0,0x00,0x00,0x00
,0x00,0x00,0x01,0xc0,0x00,0x70,0x1e,0x07,0x00,0x00,0xe0,0x00,0x00,0x00
,0x00,0x00,0x01,0xe0,0x00,0x1c,0x3f,0x0e,0x00,0x01,0xe0,0x00,0x00,0x00
,0x00,0x00,0x01,0xf0,0x00,0x0e,0x7f,0x9c,0x00,0x03,0xc0,0x00,0x00,0x00
,0x00,0x00,0x00,0xf0,0x00,0x07,0xff,0xf8,0x00,0x03,0xc0,0x00,0x00,0x00
,0x00,0x00,0x00,0xf8,0x00,0x03,0xff,0xf0,0x00,0x07,0x80,0x00,0x00,0x00
,0x00,0x00,0x00,0x7c,0x00,0x03,0xff,0xe0,0x00,0x0f,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x3c,0x00,0x03,0xff,0xf0,0x00,0x0e,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x1f,0x00,0x07,0xff,0xf8,0x00,0x7e,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x0f,0x80,0x0f,0xff,0xfc,0x00,0x7c,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x07,0xf0,0x3f,0xff,0xff,0x03,0xf0,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x03,0xff,0xff,0xc1,0xff,0xff,0xe0,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x03,0xff,0xfe,0x00,0x3f,0xff,0xc0,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x07,0xe0,0x38,0x00,0x1e,0x07,0xe0,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x0f,0x80,0x30,0x00,0x0e,0x01,0xf0,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x1f,0x00,0x70,0x00,0x06,0x00,0x78,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x1e,0x00,0xe0,0x00,0x03,0x00,0x3c,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x3c,0x01,0xe0,0x00,0x03,0x80,0x1e,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x78,0x03,0xf0,0x00,0x07,0xc0,0x1e,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x78,0x07,0xf8,0x00,0x07,0xe0,0x0f,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x70,0x0f,0xfc,0x00,0x1f,0xf0,0x0f,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0xf0,0x1f,0xff,0x80,0x7f,0xfc,0x07,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0xf0,0x3f,0x8f,0xff,0xf0,0x3e,0x07,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0xe0,0xfc,0x01,0xff,0xc0,0x0f,0x07,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0xe1,0xf0,0x00,0xff,0x80,0x07,0xc7,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0xff,0xe0,0x00,0x7f,0x00,0x03,0xf7,0x80,0x00,0x00,0x00
,0x00,0x00,0x01,0xff,0xc0,0x00,0x3f,0x00,0x01,0xff,0xc0,0x00,0x00,0x00
,0x00,0x00,0x03,0xff,0x80,0x00,0x3e,0x00,0x00,0xff,0xe0,0x00,0x00,0x00
,0x00,0x00,0x07,0xdf,0x80,0x00,0x1e,0x00,0x00,0xf9,0xf0,0x00,0x00,0x00
,0x00,0x00,0x0f,0x8f,0x00,0x00,0x1e,0x00,0x00,0x70,0xf8,0x00,0x00,0x00
,0x00,0x00,0x0f,0x07,0x00,0x00,0x1e,0x00,0x00,0x70,0x78,0x00,0x00,0x00
,0x00,0x00,0x1e,0x07,0x00,0x00,0x1e,0x00,0x00,0x30,0x3c,0x00,0x00,0x00
,0x00,0x00,0x1c,0x06,0x00,0x00,0x1e,0x00,0x00,0x30,0x1c,0x00,0x00,0x00
,0x00,0x00,0x3c,0x06,0x00,0x00,0x1e,0x00,0x00,0x30,0x1e,0x00,0x00,0x00
,0x00,0x00,0x38,0x06,0x00,0x00,0x3e,0x00,0x00,0x30,0x1e,0x00,0x00,0x00
,0x00,0x00,0x38,0x06,0x00,0x00,0x3f,0x00,0x00,0x30,0x0e,0x00,0x00,0x00
,0x00,0x00,0x38,0x07,0x00,0x00,0x3f,0x00,0x00,0x70,0x0e,0x00,0x00,0x00
,0x00,0x00,0x38,0x0f,0x00,0x00,0x7f,0x80,0x00,0x70,0x0e,0x00,0x00,0x00
,0x00,0x00,0x38,0x0f,0x00,0x00,0xff,0xc0,0x00,0x78,0x0e,0x00,0x00,0x00
,0x00,0x00,0x38,0x0f,0x80,0x01,0xff,0xe0,0x00,0xf8,0x0e,0x00,0x00,0x00
,0x00,0x00,0x38,0x0f,0xc0,0x03,0xff,0xf0,0x01,0xf8,0x1e,0x00,0x00,0x00
,0x00,0x00,0x3c,0x0f,0xe0,0x07,0xc0,0xfc,0x03,0xf8,0x1e,0x00,0x00,0x00
,0x00,0x00,0x3c,0x1f,0xfc,0x3e,0x00,0x3f,0xff,0xfc,0x3c,0x00,0x00,0x00
,0x00,0x00,0x1e,0x1f,0xff,0xfc,0x00,0x1f,0xff,0xfc,0x3c,0x00,0x00,0x00
,0x00,0x00,0x1e,0x3f,0xff,0xf8,0x00,0x0f,0xff,0xc6,0x78,0x00,0x00,0x00
,0x00,0x00,0x0f,0xff,0xff,0xf1,0xff,0xc7,0xfe,0x03,0xf0,0x00,0x00,0x00
,0x00,0x00,0x07,0xf0,0x7f,0xe1,0xff,0xe3,0xfc,0x01,0xf0,0x00,0x00,0x00
,0x00,0x00,0x07,0xe0,0x1f,0xe1,0xc0,0xe3,0xf8,0x01,0xe0,0x00,0x00,0x00
,0x00,0x00,0x03,0xc0,0x0f,0xe1,0xc0,0xe1,0xf0,0x01,0xe0,0x00,0x00,0x00
,0x00,0x00,0x03,0xc0,0x07,0xc1,0xc0,0xe1,0xe0,0x01,0xe0,0x00,0x00,0x00
,0x00,0x00,0x03,0xc0,0x03,0xc1,0xff,0xc1,0xc0,0x01,0xe0,0x00,0x00,0x00
,0x00,0x00,0x01,0xc0,0x01,0xc1,0xff,0xc1,0xc0,0x01,0xc0,0x00,0x00,0x00
,0x00,0x00,0x01,0xc0,0x01,0xe1,0xc1,0xe1,0x80,0x01,0xc0,0x00,0x00,0x00
,0x00,0x00,0x01,0xe0,0x00,0xe1,0xc0,0xe3,0x80,0x01,0xc0,0x00,0x00,0x00
,0x00,0x00,0x01,0xe0,0x00,0xe1,0xc0,0xe3,0x00,0x01,0xc0,0x00,0x00,0x00
,0x00,0x00,0x00,0xe0,0x00,0x70,0x00,0x07,0x00,0x03,0xc0,0x00,0x00,0x00
,0x00,0x00,0x00,0xf0,0x00,0x78,0x00,0x0f,0x00,0x03,0x80,0x00,0x00,0x00
,0x00,0x00,0x00,0xf0,0x00,0x7c,0x00,0x1f,0x00,0x07,0x80,0x00,0x00,0x00
,0x00,0x00,0x00,0x78,0x00,0x7e,0x00,0x3f,0x00,0x0f,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x3c,0x00,0x7f,0xe3,0xff,0x00,0x1f,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x3e,0x00,0x7f,0xff,0xff,0x00,0x3e,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x1f,0x80,0xff,0xff,0xff,0x00,0xfc,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x0f,0xe1,0xff,0x80,0x3f,0xc3,0xf8,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x03,0xff,0xf8,0x00,0x07,0xff,0xf0,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x01,0xff,0xf0,0x00,0x03,0xff,0xc0,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x7f,0xe0,0x00,0x01,0xff,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x1f,0xe0,0x00,0x03,0xfc,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x0f,0xf0,0x00,0x03,0xf0,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x03,0xf8,0x00,0x07,0xc0,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x7c,0x00,0x1f,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x3f,0x00,0x7e,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x1f,0xff,0xfc,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x07,0xff,0xf8,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x03,0xff,0xe0,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x3f,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x01,0xff,0xf0,0x7f,0xfe,0x1f,0xff,0x0f,0x0f,0x8f,0xff,0x9f,0xff,0xa0
,0x01,0xff,0xf8,0xff,0xff,0x3f,0xff,0x8f,0x1f,0x0f,0xff,0x9f,0xff,0x80
,0x01,0xe0,0x7c,0xf8,0x1f,0x3c,0x07,0x8f,0x3e,0x0f,0x00,0x00,0xf0,0x00
,0x01,0xe0,0x3c,0xf0,0x0f,0x3c,0x00,0x0f,0xfc,0x0f,0x00,0x00,0xf0,0x00
,0x01,0xe0,0x7c,0xf0,0x0f,0x3c,0x00,0x0f,0xf8,0x0f,0xff,0x80,0xf0,0x00
,0x01,0xff,0xf8,0xf0,0x0f,0x3c,0x00,0x0f,0xfc,0x0f,0xff,0x80,0xf0,0x00
,0x01,0xff,0xf8,0xf0,0x0f,0x3c,0x07,0x8f,0x3e,0x0f,0x00,0x00,0xf0,0x00
,0x01,0xe0,0x78,0xf8,0x1f,0x3f,0xff,0x8f,0x1f,0x0f,0x00,0x00,0xf0,0x00
,0x01,0xe0,0x7c,0xff,0xff,0x1f,0xff,0x0f,0x0f,0x8f,0xff,0x80,0xf0,0x00
,0x01,0xe0,0x3c,0x7f,0xfe,0x0f,0xfe,0x0f,0x07,0x8f,0xff,0x80,0xf0,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x01,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x80
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x01,0xe1,0xc7,0x0e,0x1c,0x38,0x70,0xe0,0x11,0x11,0x03,0x09,0x0e,0x00
,0x01,0xe3,0xc7,0x0e,0x1c,0x78,0xf1,0x10,0x1f,0x11,0x07,0x8d,0x11,0x00
,0x01,0x00,0x44,0x09,0x10,0x08,0x11,0x10,0x15,0x11,0x04,0x8b,0x11,0x00
,0x01,0xe3,0x84,0x09,0x1c,0x70,0xe0,0xe0,0x15,0x11,0xc4,0x89,0x0e,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]


#---------------------
#------ MAIN ---------
#---------------------

digole = mydigole.DigoleMaster()
digole.clearScreen()
digole.setWelcomeScreen(welcomelogo)
digole.close()