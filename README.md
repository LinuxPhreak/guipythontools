# GUI Python Tools

GUI Python Tools is designed to offer GUI envirenments to some of the common Python tools. Such as `pyuic venv`

To run you will need the python3 dependencies

* python3.7
* subprocess
* PyQt5

**Note do to large file sizes and problems configuring git lfs on my Fedora box I'm unable to upload needed files to the repo. As mentioned above PyQt5 is needed, you can get all the PyQt5 dependencies by downloading them from my server below. After download follow the instructions.**

**Note: If your using Linux you can use the `linux-installer.sh` file. Read the Linux section below**

[Download PyQt5](http://bennix.net/downloads/site-packages.zip)
After you have downloaded the compressed zip file extract the contents to `guipythontools/compiler/lib/python3.7/site-packages/` After you have extracted them to the location the directory should have the following sub directories.

* pip
* pip-18.1.dist-info
* pkg_resources
* __pycache__
* PyQt5
* PyQt5-5.11.3.dist-info
* PyQt5_sip-4.19.13.dist-info
* setuptools
* setuptools-40.4.3.dist-info

![Program Running](images/program.png)


## Linux Installer
To use the Linux installer simply type the following.
`chmod +x linux-installer.sh`
`sh ./linux-installer.sh`

If all goes well everything should be installed.