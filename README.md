# Pokemonify your terminal

These notbooks will help you to make your bash/fish/whaterish terminal with a pokemon greeting



## Requirements

First:

- make sure you have `python3` installed
- make sure you have `pip3` installed

If not, get them using your favorite package manager `apt-get`, `dnf`, `brew`, `wathever`

Second: Make sure you have the libraries

- `jupyter` (to use the notebooks)
- `numpy`
- `PIL` (for image IO)
- `magic` (to list image attributes)
- `ansi` (to get color codes)

If not, get them using `pip3 install <my_missing_package>`

## Launch the experiment

First, go to the root of the folder, and **launch jupyter**: `jupyter notebook`

Next, open the `01_cut_pokemon.ipynb`, and launch cells until error.
If any, please report it.
This notebook will transform a pokedex image (will 255 Pokemons) to 255 images (with one pokemon each).

It will work for most of them, but some will have troubles, and you will have to edit. (at least, you will not cut 255 Pokemon with gimp ;)

After that, you will have small images in the `Poke/` directory

## Set up your terminal

### Read the script

Notebook `02_RGB_to_ANSI.ipynb` will show you what we are going to do.
We will convert pixels of our small images to squares of color. 

### For all

In the `greeting.py` file, change the path in order to access into the `Poke/` folder.

### Fish terminal

Write into fish terminal: 

```fish
function fish_greeting
        set c  (eval tput cols)
        eval "/PATH/TO/THE/CODE/greeting.py" $c
echo -e (cat str_img.txt)
rm str_img.txt
end
funcsave fish_greeting
```
And change `/PATH/TO/THE/CODE/` in order to access the script `greeting.py`

### Bash

Do it yourself :D




