# tekken8_game_theory

To run the scripts, You need to use conda or a virtual environment with Python >= 3.8.

You will need to install the package locally:

pip install .

Then, while in the root directory of the repo, run the following script to generate up-to-date output files for each character:
python tekken8_gto.py --name $CHARACTER_NAME

Currently supported character names are 'azucena' or 'reina'.

Credit to https://wavu.wiki/t/Template:Mixup for the json2gbt.py script for converting JSON to .gbt files.

Credit to Kalki for the basis on analysis from the wavu wiki.
