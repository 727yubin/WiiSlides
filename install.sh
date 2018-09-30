sudo apt-get install gawk bison flex libbluetooth-dev libgtk2.0-dev libgtk2.0 autoconf autogen automake bluetooth pkg-config python-dev git

git clone https://github.com/azzra/python3-wiimote.git

cd python3-wiimote

sudo aclocal

sudo autoconf

sudo ./configure

sudo make

sudo make install
