import pandas as pd

DATE_COLUMNS = {
    'Year': lambda s: s.dt.year,
    'Month': lambda s: s.dt.month_name(),
    'Day': lambda s: s.dt.day
}

class BitcoinAnalysis:

    def __init__(self, base: pd.DataFrame, column: str):
        self.base = base
        self.column = column
        self.base_2025 = None

    def formate_data(self) -> pd.DataFrame:
        self.base[self.column] = pd.to_datetime(self.base[self.column], unit='s')
        for new_col, func in DATE_COLUMNS.items():
            self.base[new_col] = func(self.base[self.column])

        self.base_2025 = self.base[self.base['Year'] == 2025].copy()

        return self


    def _get_specific_dates(self) ->pd.DataFrame:
        dates_df = self.base_2025[
            (self.base_2025[self.column].dt.day ==1) |
            (self.base_2025[self.column].dt.day ==15) |
            (self.base_2025[self.column].dt.is_month_end)
        ]

        return dates_df
    
    def prepare_final_dataframe(self):
        dates_df = self._get_specific_dates()

        bitcoin_filtrado_df = (dates_df.drop(columns=[self.column])
        .drop_duplicates(subset=['Year', 'Month', 'Day'])
        .reset_index(drop=True))

        bitcoin_filtrado_df['Variacao_Pct'] = (
            bitcoin_filtrado_df['Close']
            .pct_change()
            .mul(100)
            .round(2)
            .fillna(0)
        )
    
        return  bitcoin_filtrado_df

df = pd.read_csv("btcusd_1-min_data.csv", sep=',')
analysis = BitcoinAnalysis(df, 'Timestamp')
resultado = (analysis.formate_data().prepare_final_dataframe())
resultado.to_csv('result_bitcoin_2025.csv', index=False)
