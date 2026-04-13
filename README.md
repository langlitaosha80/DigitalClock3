# 数字时钟 (Digital Clock) - Android 应用

一款可在安卓手机上运行的数字时钟应用，支持显示小时、分钟、秒，可更改背景色和时钟颜色，可置顶显示。

## 功能特性

- **数字时钟显示**: HH:MM:SS 格式，24小时制，实时更新
- **置顶显示**: 可将时钟置于其他应用之上
- **颜色自定义**: 可更改背景色和文字颜色（各6种预设颜色）
- **简洁界面**: 全屏数字显示，轻点屏幕底部打开设置

## 所需工具软件

### 在电脑上构建 APK（推荐）

#### CentOS / NewStartOS 环境配置步骤：

```bash
# 1. 安装 Python 3.9+ 和 pip
sudo dnf update
sudo dnf install python3 python3-pip python3-venv

# 2. 安装 Java JDK 11（系统已有，跳过此步）
# sudo dnf install java-11-openjdk java-11-openjdk-devel

# 3. 下载并安装 Android SDK command line tools（使用 Java 11 兼容版本）
mkdir -p ~/android-sdk/cmdline-tools
cd ~/android-sdk/cmdline-tools
curl -O https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip
unzip commandlinetools-linux-8512546_latest.zip
mv cmdline-tools latest
chmod +x latest/bin/sdkmanager

# 4. 设置环境变量（添加到 ~/.bashrc）
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
export ANDROID_HOME=~/android-sdk
export PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH

# 5. 接受许可证并安装 SDK 组件
printf 'y\ny\ny\ny\ny\ny\ny\ny\n' | sdkmanager --licenses
sdkmanager --install "platforms;android-33" "build-tools;33.0.0" "platform-tools"

# 6. 安装 Python 依赖
pip3 install kivy==2.2.0 buildozer

# 7. 构建 APK
cd /home/10035687@zte.intra/Dpan/geweiTest/pytest/androidpytest
buildozer -v android debug
```

**注意**: 如果 `sdkmanager` 版本 (8512546) 提示需要 Java 17，请下载更新的版本但需要先安装 JDK 17。

### Ubuntu 环境配置

```bash
# 1. 安装 Python 3.9+
sudo apt update
sudo apt install python3 python3-pip python3-venv

# 2. 安装 Java JDK 11
sudo apt install openjdk-11-jdk

# 3. 设置 JAVA_HOME 环境变量
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# 4. 安装 Android SDK
mkdir -p ~/android-sdk/cmdline-tools
cd ~/android-sdk/cmdline-tools
wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip
unzip commandlinetools-linux-11076708_latest.zip
mv cmdline-tools latest

# 5. 设置环境变量（添加到 ~/.bashrc）
export ANDROID_HOME=~/android-sdk
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools

# 6. 安装 Android SDK 组件
sdkmanager --install "platforms;android-33" "build-tools;33.0.0" "platform-tools"

# 7. 安装 Python 依赖
pip install kivy==2.2.0 buildozer

# 8. 构建 APK
buildozer -v android debug
```

### Windows 环境配置

1. 安装 Python 3.9+: https://www.python.org/downloads/
2. 安装 JDK 11: https://adoptium.net/temurin/releases/?version=11
3. 安装 Android Studio 或 command line tools
4. 设置环境变量 JAVA_HOME 和 ANDROID_HOME
5. 使用 WSL2 或直接在 Linux 上构建（推荐）

### macOS 环境配置

```bash
# 1. 安装 Homebrew（如果未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. 安装依赖
brew install python3 openjdk@11 android-sdk

# 3. 设置环境变量
export JAVA_HOME=$(/usr/libexec/java_home)
export ANDROID_HOME=~/Library/Android/sdk

# 4. 构建
pip3 install kivy==2.2.0 buildozer
buildozer -v android debug
```

## 使用 GitHub Actions 构建 APK（推荐，无需本地环境）

### 步骤：

1. **创建 GitHub 账号**（如果没有）：https://github.com/

2. **上传代码到 GitHub**
   - 在 GitHub 上创建新仓库（例如 `digital-clock`）
   - 将项目文件上传到仓库

3. **配置 GitHub Actions**
   - `.github/workflows/build.yml` 已包含在项目中
   - 推送代码后，GitHub Actions 会自动构建

4. **下载 APK**
   - 进入 `Actions` 标签页
   - 点击最新的 workflow 运行
   - 在 Artifacts 中下载 `digital-clock-apk`

### 项目结构

```
androidpytest/
├── main.py                        # 主程序代码
├── buildozer.spec                # Buildozer 构建配置
├── SPEC.md                       # 功能规范文档
├── README.md                     # 本说明文件
└── .github/
    └── workflows/
        └── build.yml             # GitHub Actions 构建配置
```

## 构建说明

1. 确保所有依赖工具已安装并配置好环境变量
2. 在项目目录下运行：
   ```bash
   buildozer -v android debug
   ```
3. 生成的 APK 文件位于 `bin/` 目录下

## 安装 APK

将生成的 APK 文件传输到安卓手机，在手机上允许"安装未知来源应用"后安装。

## 运行说明

1. 打开应用后，全屏显示当前时间
2. 点击屏幕底部的"设置"按钮打开设置面板
3. 可选择：
   - 开启/关闭置顶模式
   - 选择背景颜色（白、黑、红、绿、蓝、黄）
   - 选择文字颜色（白、黑、红、绿、蓝、黄）
4. 点击"关闭"关闭设置面板

## 技术栈

- **语言**: Python 3.9+
- **UI框架**: Kivy 2.2.0
- **打包工具**: Buildozer
- **目标平台**: Android 5.0+ (API 21)

## 注意事项

- 构建需要在 Linux 环境下进行（推荐使用 CentOS/Ubuntu）
- Android SDK 和 JDK 是必需的开发工具
- 确保有足够的磁盘空间（约 2-3 GB）用于 Android SDK
