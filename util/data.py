import pandas as pd


def get_element_label_lists(num_elements):
    # Define the appropriate lists of elements based on the structure type
    if num_elements == 2:
        A_list = [
            "Fe",
            "Co",
            "Ni",
            "Ru",
            "Rh",
            "Pd",
            "Os",
            "Ir",
            "Pt",
        ]
        B_list = [
            "Si",
            "Ga",
            "Ge",
            "In",
            "Sn",
            "Sb",
        ]
        return A_list, B_list

    if num_elements == 3:
        R_List = [
            "Sc",
            "Y",
            "La",
            "Ce",
            "Py",
            "Nd",
            "Pm",
            "Sm",
            "Eu",
            "Gd",
            "Tb",
            "Dy",
            "Ho",
            "Er",
            "Tm",
            "Yb",
            "Lu",
            "Th",
            "U",
        ]
        M_List = [
            "Fe",
            "Co",
            "Ni",
            "Ru",
            "Rh",
            "Pd",
            "Os",
            "Ir",
            "Pt",
        ]
        X_List = [
            "Si",
            "Ga",
            "Ge",
            "In",
            "Sn",
            "Sb",
        ]
        return R_List, M_List, X_List


def get_mendeleev_numbers(data):
    data = "data/element_Mendeleev_numbers.xlsx"
    df = pd.read_excel(data, header=None)
    elements = df.iloc[
        :, 0
    ]  # Assuming elements are in the first column
    mendeleev_numbers = df.iloc[
        :, 1
    ]  # Assuming Mendeleev numbers are in the 6th column
    return dict(zip(elements, mendeleev_numbers))


def get_element_property_values(data, element_col_num):
    data = "data/element_properties_for_ML.xlsx"
    df = pd.read_excel(data, header=None, engine="openpyxl")
    elements = df.iloc[
        :, 0
    ]  # Assuming elements are in the first column
    property_values = df.iloc[
        :, element_col_num
    ]  # Choose the property (by default Mendeleev number)
    return dict(zip(elements, property_values))
