# How Does It work (HDIW)

How Does It Work is a CLI program which allows you to view what makes a certain program / game run. HDIW makes it super simple to find out what certain programs use, but just making you input the directory!

## Usage

To use HDIW, simply run it with a directory parameter, for example: `python3 hdiw "C:\Users\user\Downloads"` would scan the entire Downloads directory, but you probably don't want to do that.

Below is an example of an output generated by HDIW

.![Code_UTTnrPXlNB](https://i.imgur.com/7Jdq5l8.png)

The most common way of using HDIW is on games, you just need to copy the game's directory and then run HDIW like shown above!

## Installation

To install HDIW you can simply just download the zip from github, and then unzip it. To test if it works you can type run the command `python3 hdiw.py -h`. If you get a help message, you have succesfully installed HDIW!

## hdiwignore.json

Let's say you want to scan a directory, but there's some folders in there you don't want to scan. That's what hdiwignore is for! To utilize hdiwignore, make a file called `hdiwignore.json` in the directory you want to scan, and then just put a json list of the files / directories you want to ignore!

For example:

```json
["bin", "theme.eft"]
```

would ignore everything in the bin folder, and ignore theme.eft.

## Contributing

There are many things that HDIW needs help with, whether it's adding new Game Engines / Frameworks, or optimizations, bugfixes, or quality of life features. We're always open to accepting pull requests!

### Adding New Technologies

To add a new technology, open the `main.json` file. You will see `file-extension`, `name-contains`, and `name-colors`. Let's say you want to make files ending with .py add Python as a result, you would add the following to `file-extension`:

```json
".py": {
	"name": "Python",
	"chance": 100,
	"category": "Programming Languages"
}
```

`name`: The name of the technology
`chance`: How certain you are that the directory contains this technology.
`category`: The category of thetechnology

You can also use `name-contains` the same way, except make the key of the dictionary the text you want to look for.

Next, you want to set a color for your technology. Under `name-colors` add a new line. For this example it will be `"python": "YELLOW"`.

The colors you can currently use are

```
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX
```
