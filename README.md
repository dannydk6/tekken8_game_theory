# tekken8_game_theory

To run the scripts, You need to use conda or a virtual environment with Python >= 3.8.

You will need to install the package locally:

pip install .

Then, while in the root directory of the repo, run the following script to generate up-to-date output files for each character:
python tekken8_gto.py --name $CHARACTER_NAME

Currently supported character names are 'azucena', 'reina', 'bryan', 'eddy', and 'cammy' from SF6.

Please note input excel files must follow the schema of a metadata tab with the following rows:

| Key        | Value          |
|------------|----------------|
| Title      | Scenario Name  |
| P1         | Player1        |
| P2         | Player2        |
| Comment    | sample comment |

then you need a second tab with the name of the scenario. The first column is called strats and contains P1 strats. The first row contains P2 strats as such:

| strats | b | db | 1 |
|--------|---|----|---|
| b      | 0 | 0  | 0 |
| db     | 0 | 0  | 0 |
| 1      | 0 | 0  | 0 |

Credit to https://wavu.wiki/t/Template:Mixup for the json2gbt.py script for converting JSON to .gbt files.

Credit to Kalki for the basis on analysis from the wavu wiki.
