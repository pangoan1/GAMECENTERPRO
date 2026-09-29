[app]
title = Game Center Pro
package.name = gamecenterpro
package.domain = org.javad
source.dir = .
source.include_exts = py,json,png,jpg,kv,atlas,ttf,otf
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[buildozer:android]
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
