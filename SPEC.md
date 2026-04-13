# Digital Clock Android App Specification

## 1. Project Overview

- **Project Name**: DigitalClock
- **Project Type**: Android Mobile Application (Python/Kivy)
- **Core Functionality**: A digital clock widget that displays system time (hours, minutes, seconds) with customizable colors and always-on-top functionality

## 2. Technology Stack

- **Framework**: Kivy 2.2.0+ (Python GUI framework)
- **Build Tool**: Buildozer (Android packaging)
- **Language**: Python 3.9+
- **Key Libraries**:
  - Kivy (UI framework)
  - android (for always-on-top functionality via Android API)
  - datetime (system time)

## 3. Feature List

### Core Features
1. **Digital Time Display**
   - Show hours, minutes, seconds in digital format (HH:MM:SS)
   - Real-time update every second
   - 24-hour format

2. **Always-On-Top Mode**
   - Option to pin the clock above other apps
   - Toggle on/off from within the app

3. **Color Customization**
   - Change background color (preset color picker)
   - Change clock text color (preset color picker)
   - 6 preset colors for each: White, Black, Red, Green, Blue, Yellow

4. **Simple UI**
   - Full-screen clock display
   - Settings panel (collapsible/expandable)
   - Clean, minimal interface

## 4. UI/UX Design Direction

### Visual Style
- Modern, minimalist digital clock aesthetic
- Large, readable digits
- Clean sans-serif font

### Color Scheme
- Default: Dark background (#000000), White text (#FFFFFF)
- User can customize both independently

### Layout
- Main screen: Full-screen digital clock (centered)
- Bottom: Collapsible settings bar with:
  - "置顶" (Pin) toggle button
  - Background color selector
  - Text color selector

## 5. File Structure

```
androidpytest/
├── main.py              # Main Kivy application
├── buildozer.spec       # Buildozer configuration
├── README.md            # Installation guide
├── SPEC.md              # This specification
```

## 6. Prerequisites for Building

- Linux/macOS/Windows with Python 3.9+
- For Android build: Ubuntu 20.04+ (Linux recommended)
- Required tools: Python, pip, git, JDK 11, Android SDK
