# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** E
# **Rôle du Fichier :** Script ou configuration declarative
# **Centre Doctrinal Local :** AI Manager garde script ou configuration declarative en limitant le bruit local et la friction structurelle.
# **Loi de Survie :** μ = α - β - κ
# **Lecture Locale :**
# - **α :** stabilite locale
# - **β :** bruit externe injecte
# - **κ :** friction structurelle
# **Risque :** e∞ ∝ ε / μ
# **Opérateur Correctif :** D(S)=proj_{SafeDomain}(S)
# **Axiome :** un système survit SSI μ > 0
# **Doctrine Goodhart : tout succès apparent est invalide si μ décroît**
# **Gouvernance : toute modification doit maximiser Δμ**
# **Lien Miroir :** E

import json


import pandas as pd


from datetime import date, timedelta, datetime


from typing import Annotated





SavePathType = Annotated[str, "File path to save data. If None, data is not saved."]





def save_output(data: pd.DataFrame, tag: str, save_path: SavePathType = None) -> None:


    if save_path:


        data.to_csv(save_path)


        print(f"{tag} saved to {save_path}")








def get_current_date():


    return date.today().strftime("%Y-%m-%d")








def decorate_all_methods(decorator):


    def class_decorator(cls):


        for attr_name, attr_value in cls.__dict__.items():


            if callable(attr_value):


                setattr(cls, attr_name, decorator(attr_value))


        return cls





    return class_decorator








def get_next_weekday(date):





    if not isinstance(date, datetime):


        date = datetime.strptime(date, "%Y-%m-%d")





    if date.weekday() >= 5:


        days_to_add = 7 - date.weekday()


        next_weekday = date + timedelta(days=days_to_add)


        return next_weekday


    else:


        return date
