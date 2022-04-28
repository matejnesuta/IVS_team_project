#!/bin/sh
mkdir -p ../installer/usr/share/calculator 2>/dev/null
cp  calculator.py ../installer/usr/share/calculator/calculator.py && chmod +x ../installer/usr/share/calculator/calculator.py
cp -r  ./mathlib ../installer/usr/share/calculator/mathlib
cp  gui.ui ../installer/usr/share/calculator/gui.ui
mkdir -p ../installer/usr/local/bin 2>/dev/null
ln -sf /usr/share/calculator/main.py ../installer/usr/local/bin/calculator
mkdir ../installer/tmp 2>/dev/null
cp requirements.txt ../installer/tmp/requirements.txt
chmod +x ../installer/DEBIAN/postinst
dpkg-deb --build ../installer/ ../installer/calculator.deb
