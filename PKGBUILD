# Maintainer: Ben P. Dorsi-Todaro <ben@bigbenshosting.com>
_pkgbasename=guipythontools
pkgname=$_pkgbasename-git
pkgrel=1
pkgver=v1.0
pkgdesc="GUI Tools for Python"
arch=('any')
url="https://linuxphreak.github.io/guipythontools"
license=('GPL')
depends=('python3' 'python-pyqt5')
source=(git+https://github.com/LinuxPhreak/guipythontools)
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/$_pkgbasename"
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
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
    mv $srcdir/$_pkgbasename/lib/$_python/site-packages/$_pkgbasename.py $pkgdir/usr/bin/$_pkgbasename
    chmod +x "$pkgdir/usr/bin/$_pkgbasename"

}