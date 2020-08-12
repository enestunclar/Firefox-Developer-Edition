### Changelog

**11.08.2020**
Upgrade version Firefox Developer Edition(Version 80.0b6)

**12.08.2020**
Update version (Version 80.0b7)

### Installation 

Create workspace
```
cd ~/Downloads
mkdir firefox-dev-install
cd firefox-dev-install
```

Download Github Files:
```
git clone https://github.com/enestunclar/Firefox-Developer-Edition.git
cd Firefox-Developer-Edition
```

Download Firefox Developer Source Code

```
wget https://download-installer.cdn.mozilla.net/pub/devedition/releases/80.0b7/linux-x86_64/tr/firefox-80.0b7.tar.bz2

bzip2 -d firefox-80.0b7.tar.bz2
tar xvf firefox-80.0b7.tar
```

To install Firefox Developer Edition, follow the steps below.

```
sudo python3 install.py
```

The sucsessfully install Firefox Developer Edition.


