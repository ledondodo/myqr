# QR Code
Create a QR code of a text from terminal command line

## Launch the program
Launch the program with python by typing `python myqr.py` in the program directory from the Terminal command line.

I personally use a shortcut with the short keyword `myqr` that launches the code from the right directory.

## How does it work ?
When you launch the program, you'll be able to enter some text and generate your QR code from the Terminal command line. An image "myQR.png" will be created in the program's directory, and it will open. This QR Code contains the text you entered.

<p align="center">
  <img src="img/myQR.png" width=30% height=30%>
</p>

## Use Terminal alias (mac)
Open or create the shell configuration file by typing `open ~/.zprofile` in the user’s home directory.

Add the line: `alias myqr='python /pathtofile/myqr.py'` with the right path to your file.

Now you can type `myqr` in the Terminal command line to launch the program.

## Libraries
This program uses qrcode v6.1 package: `pip install qrcode==6.1`

## License
[MIT License](LICENSE)
