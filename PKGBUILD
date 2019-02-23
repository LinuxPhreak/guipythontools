# Maintainer: Ben P. Dorsi-Todaro <ben@bigbenshosting.com>
_pkgbasename=guipythontools
pkgname=$_pkgbasename-git
pkgrel=1
pkgver=58db73aa4eec7f5914eaf774e82db5c134b30e63
pkgdesc="GUI Tools for Python"
arch=('any')
url="https://linuxphreak.github.io/guipythontools"
license=('GPL')
depends=('python3' 'python-pyqt5')
source=(git+https://github.com/LinuxPhreak/guipythontools)
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/$_pkgbasename"
    git rev-parse HEAD | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "$srcdir/$_pkgbasename"
    
    python setup.py bdist
}


package() {
    _pkg=$(ls "$srcdir/$_pkgbasename/dist/")
    tar -xC "$pkgdir/" -f "$srcdir/$_pkgbasename/dist/$_pkg"

    mkdir -p "$pkgdir/usr/bin"

    _python=$(ls "$pkgdir/usr/lib/")
    mv $srcdir/$_pkgbasename/lib/$_python/site-packages/compile.py $pkgdir/usr/bin/compile.py
    chmod +x "$pkgdir/usr/bin/compile.py"

}