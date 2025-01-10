# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

def pregunta_01():
    import matplotlib.pyplot as plt 
    import pandas as pd 
    import os 

    if not os.path.exists("docs"):
        os.makedirs("docs")

    df = pd.read_csv("files/input/shipping-data.csv")

    df.head()
    print(df.head())

    def shware(df):
        df = df.copy()
        plt.figure()
        counts = df.Warehouse_block.value_counts()
        counts.plot.bar(
                title="envios por almacenamiento"
            )
        plt.savefig("docs/shipping_per_warehouse.png")
    shware(df)

    def vimoshi(df):
        df = df.copy()
        plt.figure()
        counts = df.Mode_of_Shipment.value_counts()
        counts.plot.pie(
            title = "Forma de envío"
        )
        plt.savefig("docs/mode_of_shipment.png")

    vimoshi(df)

    def vicusrat(df):
        df = df.copy()
        plt.figure()
        df = (
            df[["Mode_of_Shipment", "Customer_rating"]].groupby("Mode_of_Shipment").describe
            
        )
        #df.columns = df.columns.droplevel()
        #df = df[["mean", "min", "max"]]
        plt.savefig("docs/average_customer_rating.png")
        return df
    vicusrat(df)

    def wedi(df):
        df = df.copy()
        plt.figure()
        df.Weight_in_gms.plot.hist()
        plt.savefig("docs/weight_distribution.png")
    wedi(df)

    html_content = """<!DOCTYPE html>
    <html>
    <body>
        <h1>Shipping Dashboard Example</h1>
        <div style="width:45%;float:left">
        <img src="shipping_per_warehouse.png" alt="Fig 1">
        <img src="mode_of_shipment.png" alt="Fig 2">
        </div>
        <div style="width:45%;float:left">
        <img src="average_customer_rating.png" alt="Fig 3">
        <img src="weight_distribution.png" alt="Fig 4">
        </div>
    </body>
    </html>
    """

    # Escribir el contenido en un archivo HTML
    with open("docs/index.html", "w") as file:
        file.write(html_content)

    

