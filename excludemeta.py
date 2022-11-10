def exclude_meta(filename, sheet_name, filename_to_save):
    import pandas as pd

    df = pd.read_excel(filename, sheet_name=sheet_name, engine="openpyxl")
    df_excluding_meta = df.drop(df.index[0:9])
    df_excluding_meta.columns = df_excluding_meta.iloc[0].values
    df_excluding_meta = df_excluding_meta[2:]
    x = df_excluding_meta.columns[0]
    if sheet_name == "Monthly Data":
        df_excluding_meta[x] = pd.to_datetime(df_excluding_meta[x])
        df_excluding_meta[x] = df_excluding_meta[x].dt.strftime('%Y'"  "'%B')
    df_excluding_meta.reset_index(drop=True, inplace=True)
    # df_excluding_meta.to_excel(filename_to_save, sheet_name=sheet_name, if_sheet_exists='overlay', engine='openpyxl')
    dynamically_adjust_column_width(df_excluding_meta, filename_to_save, sheet_name)


def dynamically_adjust_column_width(dataframe, filename_to_save, sheet_name):
    import pandas as pd
    import openpyxl
    import os.path
    import os.path
    if os.path.exists(filename_to_save):
        writer = pd.ExcelWriter(filename_to_save, engine="openpyxl", mode='a')
    else:
        writer = pd.ExcelWriter(filename_to_save, engine="openpyxl", mode='w')
    dataframe.to_excel(writer, sheet_name=sheet_name, index=False, na_rep='NaN')
    for column in dataframe:
        column_length = max(dataframe[column].astype(str).map(len).max(), len(column))
        col_idx = dataframe.columns.get_loc(column)
        sheet = writer.sheets[sheet_name]
        sheet.column_dimensions[openpyxl.utils.cell.get_column_letter(col_idx + 1)].width = column_length
    writer.save()

