import io
import pandas as pd


def export_to_csv(columns, data):

    df = pd.DataFrame(data)

    if columns:
        df = df[columns]

    output = io.StringIO()

    df.to_csv(
        output,
        index=False
    )

    output.seek(0)

    return output

def export_to_excel(columns, data):

    df = pd.DataFrame(data)

    if columns:
        df = df[columns]

    output = io.BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(
            writer,
            index=False,
            sheet_name="Results"
        )

    output.seek(0)

    return output