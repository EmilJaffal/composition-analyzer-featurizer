# Composition Analyzer/Featurizer (CAF)

Composition Analyzer/Featurizer (CAF) is a user-interactive Python script that offers tools for generating compositional features. It also provides interactive tools used for tasks such as filtering, sorting chemical formulas, and merging Excel files.

## Motivation

We developed this interactive tool to aid solid-state chemists and materials scientists in generating compositional training data ranging from dozens to tens of thousands of compounds. Both experimentalists and novices can use this tool to generate their own data with a basic understanding of Python. The codebase has been designed to allow beginners to customize it easily.

## Usage

Execute the following command to begin.

```bash
python main.py
```

Then, a prompt will appear and enter a number to proceed.

```text
Options:
1: Filter chemical formulas and generate periodic table heatmap
2: Sort chemical formulas in Excel
3: Create compositional features for formulas in Excel
4: Match .cif files in a folder against Excel
5: Merge two Excel files based on id/entry
Please enter the number of the option you want to run: 1
```

## Flow chart

<img width="839" alt="CAF-flowchart" src="https://github.com/bobleesj/composition-analyzer-featurizer/assets/14892262/7a66abae-54d2-4cc4-85af-44b34440f3b6">

## Options

CAF provides 5 interactive options detailed below.

**Option 1. Filter** - offers analysis capabilities for chemical formulas already prepared in Excel sheets or a folder containing .cif files. It counts and identifies unique elements present, detects errors within the data, and generates a periodic table heatmap. Optionally, it provides two filtering methods: one for removing specific elements and another for categorizing compounds into unary, binary, ternary, and quaternary groups.

![periodic talbe heatmap](https://shorturl.at/eDS05)

**Option 2. Sort** - rearranges a set of chemical formulas in an Excel file based on 3 options.

1. **By label** - Sorts elements by a pre-configured label for each element. This option is applicable only for binary and ternary compounds. You may modify the predefined set of elements in `data/label.xlsx` to add/remove any elements.

   ```text
   # Binary compounds
   A: Fe, Co, Ni, Ru, Rh, Pd, Os, Ir, Pt
   B: Si, Ga, Ge, In, Sn, Sb

   # Ternary compounds
   R: Sc, Y, La, Ce, Py, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Th, U
   M: Fe, Co, Ni, Ru, Rh, Pd, Os, Ir, Pt
   X: Si, Ga, Ge, In, Sn, Sb
   ```

2. **By index** - sorts compounds by stoichiometric ratio in either increasing or decreasing order. If the index is the same, the formulas are sorted based on the Mendeleev number provided in `data/element_Mendeleev_numbers.xlsx`
3. **By property** - sorts by the value of an elemental chemical property, choosing from 27 options available in the Oliynyk database. This sorting is limited to 33 elements provided in the Oliynyk elemental property Excel file located at `data/element_properties_for_ML.xlsx`.

   ```text
   Available columns for sorting
   1. Atomic weight
   2. Atomic number
   3. Period
   4. Group
   5. Mendeleev number
   6. valence e total
   7. unpaired electrons
   8. Gilman no. of valence electrons
   9. Zeff
   10. Ionization energy (eV)
   11. CN
   12. ratio n closest/CN
   13. polyhedron distortion (dmin/dn)
   14. CIF radius element
   15. Pauling, R(CN12)
   16. Pauling EN
   17. Martynov Batsanov EN
   18. Melting point, K
   19. Density, g/mL
   20. Specific heat, J/g K
   21. Cohesive energy
   22. Bulk modulus, GPa
   23. Abundance in Earth's crust
   24. Abundance in solar system (log)
   25. HHI production
   26. HHI reserve
   27. cost, pure ($/100g)
   ```

**Option 3. Features -** generates compositional features for formulas in an Excel file and, optionally, a composition-normalized vector using hot encoding. The database for the featurziation is based on the Oliynyk peer-reviewed data ([DOI](https://doi.org/10.1016/j.dib.2024.110178)).

```text
Options:
  1: Filter chemical formulas and generate periodic table heatmap.
  2: Sort chemical formulas in an Excel file
  3: Create compositional features for formulas in an Excel file.
  4: Match .cif files in a folder against an Excel file.
  5: Merge two Excel files based on id/entry.
Please enter the number of the option you want to run: 3

Available Excel files with 'Formula' in the first column:
1. A-B database.xlsx
2. A-B features.xlsx
3. binary M-X.xlsx
4. binary_excel.xlsx
5. formulas.xlsx

Enter the number corresponding to the Excel file you wish to select: 5
Selected Excel file: /Users/imac/Downloads/CAF/formulas.xlsx
```

1. **For binary compounds**, 133 binary features defined in `feature/binary.py` are generated and saved in an Excel file.
2. **For ternary compounds**, 204 ternary features from `feature/ternary.py` are generated for each formula and stored in an Excel file.
3. **For all compounds**, regardless of the formula type, a universal set of 112 sorted features and 156 unsorted (containing first and last element values) generated using `feature/universal.py`
4. (Optional) Extended features - You can generate an extensive list of features using `feature/universal_long.py`, `feature/binary_long.py`, and `feature/ternary_long.py`. These files include arithmetic operations provided in `feature/operation.py`. Any columns with overflow or undefined values are removed before the data is saved in Excel files. The column lengths can reach into the thousands.

**Option 4. Match** - matches .cif files in a folder against an Excel file

This option allows the user to select a folder containing .cif files and an Excel file. The Excel file should include an "Entry" column containing the IDs of the .cif files. The script parses the IDs from the .cif files and compares them with the entries in the Excel file. The Excel file is then updated to filter and display only the entries that match the existing .cif files.

**Option 5. Merge** - combines two Excel files based on an "Entry" column.

User selects two Excel files to merge based on a common column labeled "Entry". This feature is useful for combining datasets, such as one from a database and another generated using this CAF (Composition Analyzer/Featurizer) or SAF (Structure Analyzer/Featurizer).

## Installation

```bash
git clone https://github.com/bobleesj/composition-analyzer-featurizer.git
cd composition-analyzer-featurizer
conda create -n cif python=3.12
conda activate cif
pip install -r requirements.txt
```

## Feedback

If you have any questions or any feedback, please feel free to email me at [sl5400@columbia.edu](mailto:sl5400@columbia.edu). The code is currently actively developed and improved. Any feedback is appreciated.

## Contributors

- Alex Vtorov - feature
- Anton Oliynyk - project lead, ideation
- Danila Shiryaev - sort
- Emil Jaffal - filter
- Nikhil Kumar Barua - feature
- Sangjoon Bob Lee - development lead, integration

## Changelog

- 20240514 - Released repository public
