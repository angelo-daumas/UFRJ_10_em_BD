import pandas as pd

def get_bar_chart(df: pd.DataFrame, x_column, y_column, width=80):

    bg_color = "rgba(158,202,225,0.8)"

    if not isinstance(df, pd.DataFrame):
        raise Exception("Not a pandas dataFrame")

    return {
            "labels": df[x_column].tolist(),
            "datasets": [{
                "label": "",
                "data": df[y_column].tolist(),
                "backgroundColor": bg_color,
                "barThickness": width,
            }]
        }

def get_card(value: str, desc: str, icon: int) -> dict:
    # ajust
    max_desc_len = 60

    if len(desc) > max_desc_len:
        raise Exception(f'Description text too big. Keep under {max_desc_len} chars')

    return {
        "value": value,
        "desc":  desc,
        "icon":  icon
    }
