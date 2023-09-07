# QR Code
Create a QR code of a text from terminal command line

## Launch the program
Launch the program with python by typing `python myqr.py` in the program directory from the Terminal command line.

I personally use a shortcut with the short keyword `myqr` that launches the code from the right directory.

## How does it work ?
As you launch the program, you'll see the following interface in the Terminal command line. Enter some text after "Post:" then hit enter, and a blue message will confirm that you successfully tweeted ! Go check online and you should immediately see your new post.

<p align="center">
  <img src="img/myQR.png" width=40% height=40%>
</p>

## Use Terminal alias (mac)
Open or create the shell configuration file by typing `open ~/.zprofile` in the user’s home directory.

Add the line: `alias myqr='python /pathtofile/myqr.py'` with the right path to your file.

Now you can type `myqr` in the Terminal command line to launch the program.

## Libraries
This program uses qrcode v6.1 package: `pip install qrcode==6.1`

## License
[MIT License](LICENSE)
