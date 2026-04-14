import pandas as pd

# 1. dosyalari oku
main = pd.read_excel("Final2.xlsx", engine="openpyxl")
fifa = pd.read_csv("players19.csv")

# 2. kolon isimlerini temizle
main.columns = main.columns.str.strip().str.lower()
fifa.columns = fifa.columns.str.strip().str.lower()

# 3. dogru isim kolonlarini sec
main = main.rename(columns={"player": "player_name"})
fifa = fifa.rename(columns={"long_name": "player_name"})

# 4. isimleri temizle
main["player_name"] = main["player_name"].astype(str).str.lower().str.strip()
fifa["player_name"] = fifa["player_name"].astype(str).str.lower().str.strip()

# 5. merge
merged = pd.merge(main, fifa, on="player_name", how="inner")

# 6. gereksiz kolonlari sil
merged = merged.loc[:, ~merged.columns.str.contains('unnamed')]

# 7. kaydet
merged.to_csv("merged_data.csv", index=False)

# 8. kontrol
print("\n--- MAIN ---")
print(main["player_name"].head(10))

print("\n--- FIFA ---")
print(fifa["player_name"].head(10))

print("\n--- MERGED ---")
print(merged.head())

print("\nSHAPE:", merged.shape)
print("\nNULL VALUES:\n", merged.isnull().sum())

print("\nBitti ✅")