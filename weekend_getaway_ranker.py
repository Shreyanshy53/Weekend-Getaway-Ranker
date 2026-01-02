import pandas as pd

print("=== Weekend Getaway Ranker ===")

# CSV load
data = pd.read_csv("data/Top Indian Places to Visit.csv")

# Columns rename
data = data.rename(columns={
    "Name": "Destination",
    "Google review rating": "Rating",
    "Number of google review in lakhs": "Popularity"
})

# User input
source_city = input("Enter source city: ")

# City filter (use copy to avoid warning)
city_data = data[data["City"].str.lower() == source_city.lower()].copy()

if city_data.empty:
    print("Is city ke liye data nahi mila")
else:
    # Score calculation
    city_data.loc[:, "Score"] = (
        city_data["Rating"] * 0.7 +
        city_data["Popularity"] * 0.3
    )

    # Sort
    result = city_data.sort_values(by="Score", ascending=False)

    print("\nTop Weekend Destinations:\n")
    print(result[["Destination", "Rating", "Popularity"]].head(5))
