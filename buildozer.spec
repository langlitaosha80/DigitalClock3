[app]

# App name
title = DigitalClock

# Package name
package.name = digitalclock

# Package domain
package.domain = com.example

# Source directory
source.dir = .

# Version
version = 0.1

# Source files
source.include_exts = py,png,jpg,kv,atlas

# Python version
osx.python_version = 3
python3.version = 3.9

# Requirements
requirements = python3,kivy==2.2.0

# Android p4a branch
android.p4a_branch = main

# Android specific
fullscreen = 1
android.permissions = SYSTEM_ALERT_WINDOW
android.api = 33
android.minapi = 21

# Orientation
orientation = portrait

[buildozer]

# Build log level
log_level = 2

# Warn on missing files
warn_on_missing = True
