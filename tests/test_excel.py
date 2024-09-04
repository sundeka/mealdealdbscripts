from pathlib import Path
from modules import excel

def test_parse_category_names():
    files = [
        Path("excels/hedelmat_ja_vihannekset.xlsx"),
        Path("excels/juomat.xlsx"),
        Path("excels/juustot.xlsx"),
        Path("excels/kala_ja_merenelavat.xlsx"),
        Path("excels/leivat_keksit__ja_leivonnaiset.xlsx"),
        Path("excels/liha_ja_kasviproteiinit.xlsx"),
        Path("excels/maito_munat_ja_rasvat.xlsx"),
        Path("excels/oljyt_mausteet_ja_maustaminen.xlsx"),
        Path("excels/pastat_riisit_ja_nuudelit.xlsx"),
        Path("excels/snacksit.xlsx"),
    ]
    expected_titles = [
        ['Berries', 'Fruits', 'Mushrooms', 'Vegetables', 'Vegetables (root)'],
        ['Drinks'],
        ['Cheese'],
        ['Fish'],
        ['Bagels', 'Bread'],
        ['Chicken', 'Ground beef', 'Pork', 'Sausages and bacon'],
        ['Butter', 'Creams', 'Eggs', 'Milks & sour milks', 'Yoghurts'],
        ['Dressings', 'Ketchup & mustard', 'Mayonnaise', 'Oils'],
        ['Noodles', 'Pasta', 'Rice'],
        ['Chips', 'Nuts', 'Other snacks'],
    ]
    for file, titles in zip(files, expected_titles):
        names = excel.parse_category_names(file)
        assert names == titles