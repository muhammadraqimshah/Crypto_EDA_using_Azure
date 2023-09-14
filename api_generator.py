from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn
import pandas as pd
import json
import asyncio

app = FastAPI()

async def csv_row_generator_pandas(csv_filenames):
    for csv_filename in csv_filenames:
        df = pd.read_csv(csv_filename)
        for index, row in df.iterrows():
            yield json.dumps(row.to_dict())
            await asyncio.sleep(2)

@app.get("/api")
async def get_data():
    dataset_filenames = [
        "dataset/1_Bitcoin.csv", "dataset/2_Ethereum.csv", "dataset/3_Tether.csv", 
        "dataset/4_BNB.csv", "dataset/5_USD_Coin.csv", "dataset/6_XRP.csv", "dataset/7_Cardano.csv",
        "dataset/8_Dogecoin.csv", "dataset/9_Polygon.csv", "dataset/10_Solana.csv", "dataset/11_Polkadot.csv", 
        "dataset/12_Binance USD.csv", "dataset/13_Litecoin.csv", "dataset/14_Shiba_Inu.csv", "dataset/15_TRON.csv", "dataset/16_Avalanche.csv"
    ]

    return StreamingResponse(csv_row_generator_pandas(dataset_filenames), media_type='application/json')

if __name__ == '__main__':
    uvicorn.run(app, reload=True, host='0.0.0.0', port=8000)


# To Run
# uvicorn api_generator:app --reload