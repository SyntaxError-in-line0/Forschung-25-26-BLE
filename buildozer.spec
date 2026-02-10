[app]

# Name der App (wird auf dem Handy angezeigt)
title = BLE Arduino Connect

# Paketname (muss klein sein, keine Umlaute!)
package.name = bleconnect

# Domain (frei wählbar)
package.domain = org.example

# Quellcode
source.dir = .
source.include_exts = py

# Version
version = 1.0

# Einstiegspunkt
entrypoint = main.py

# Benötigte Bibliotheken
requirements = python3,kivy,jnius, android

# Anzeige
fullscreen = 0
orientation = portrait

# Android SDK / NDK
android.api = 33
android.minapi = 26
android.sdk = 33
android.ndk = 25b

# Berechtigungen
android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_SCAN,BLUETOOTH_CONNECT,ACCESS_FINE_LOCATION

# Architektur
android.archs = arm64-v8a

# Debug (optional)
android.logcat_filters = *:S python:D

# Buildozer
warn_on_root = 1
