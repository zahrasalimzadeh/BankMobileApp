[app]
title = Bank
package.name = bankmobileapp
package.domain = org.zahra
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs = .venv,.idea,.git,.github,__pycache__
version = 0.1
requirements = python3,kivy==2.3.1,kivymd==1.2.0,pillow
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1