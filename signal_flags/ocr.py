#!/usr/bin/python3

import pytesseract
from PIL import Image
import glob
import os
import cv2
import numpy as np
import hashlib

SIGNAL_MAP = {
    'c5d33cc8b54a99573afa98bb7a11e869': '6E',
    '8ea64310438ce21a9c96ec8e17695045': 'PE',
    'deabf1ae6ea6bda290ba311ba812b0ad': 'E',
    '1b632c39ca34d7db111d292a713a6426': 'I',
    '3dee675c26580c01dd888bf6c14ec7ab': 'R',
    'ee79a0783d0ad8ce1929831dc9032435': 'V',
    'af1243e10fe915cd6afd51c75540a2a0': 'B',
    '1defa182cd623ada500429c5b2015218': 'K',
    '0189ec23ec80ddae61c3d66cbd06e18b': 'L',
    '2e35e60d9500e755047a44f1f1e5e200': 'O',
    '34c8a67d4160bb4a7e73db97cbdf997d': 'H',
    '533b9f8737ca7e4c847b5bc27e18fbc6': 'N',
    '707dd897465a9d114ace722b231c2242': 'M',
    '946747f9516b2b68147fa9cdb369b238': 'Y',
    '93835ede18d369aa57c4f5dcdd0cf68b': 'VF',
    'e65f70e3c76cd25a2daed24d92f9672b': '2E',
    '051f79a24aa626178fa658040485a994': '8',
    '83e40e26f51e8ee6903f64167ff1c6df': 'A',
    '15bf3673b94fa3ce503de011f4e48668': 'C',
    '190c984193ab3153960813fb797686ce': 'D',
    'e5c818b3306c6171ab54f67c6d3e2bb9': 'E',
    '2379a7e796e4c54e5d8dfb87d6d1d4bf': 'BV',
    '5886d486608defb302ea826bd7d1697d': 'F',
    'c4a49e6cabcba2300dc04488187aba21': '2',
    '0d75dac22a9f01f2e0f982947fafba0e': '7',
    '2a5b936f1019c34411ec979b71de3df3': '6',
    '6bb444ab1f218eb026ec1d0f2d1d2e78': 'X',
    '61f64bc6a14e3398d01a774da6c22896': '4',
    '0360e68d0a2ff9b68c82010dc37b4fa7': '5',
    '4061ec1ce2f6d7d813e40847d717fadd': '9',
    '1463252f4aa2e5985e14104c44c2163b': '1',
    'a01c3f4dd967dc77276fb43b0db82739': '3',
    'f127fbe178af730769acf16a533b0528': '0',
}
CROP = 20

def parse_txt(txt):
    timestamp = None
    vessel = None
    for i in txt.split('\n'):
        if 'Timestamp' in i:
            timestamp = i[15:35]
        elif 'Ship object ID' in i:
            vessel = i[16:22]
    return (timestamp, vessel.strip())

def main():
    images = glob.glob(os.path.join('.', '*.png'))
    data = {}
    for i in images:
        img = Image.open(i)
        txt = pytesseract.image_to_string(img)
        timestamp, vessel = parse_txt(txt)
        if vessel not in data:
            data[vessel] = {}
        data[vessel][timestamp] = i
    for i in sorted(data.keys()):
        print('VESSEL:', i)
        for j in sorted(data[i].keys()):
            img = cv2.imread(data[i][j])
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            lower_green = np.array([35, 100, 100])
            upper_green = np.array([85, 255, 255])
            mask = cv2.inRange(hsv, lower_green, upper_green)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            signal = ''
            for c in contours:
                x, y, w, h = cv2.boundingRect(c)
                if w<200:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    roi = img[y:y+h, x:x+w]
                    roi = roi[CROP:h-CROP, CROP:w-CROP]
                    roi_bytes = cv2.imencode('.png', roi)[1].tobytes()
                    md5h = hashlib.md5(roi_bytes).hexdigest()
                    signal = SIGNAL_MAP.get(md5h, '.') + signal
            if signal[0:2] == '0X':
                decoded_str = ''
                for char in [signal[2:][x:x+2] for x in range(0, len(signal[2:]), 2)]:
                    decoded_str += chr(int(char, 16))
                signal = decoded_str
            print(j, signal, data[i][j])

main()
