import polars as pl
from polars import LazyFrame

# Configure Polars 
cfg = pl.Config()
cfg.set_tbl_rows(100)
valid_years = list(range(2014, 2024))

def filter_valid_year(lf: LazyFrame) -> LazyFrame:
    return lf.filter(pl.col("tpep_pickup_datetime").dt.year().is_in(valid_years))

def coeff(x: pl.Expr, y: pl.Expr) -> pl.Expr:
    # Calculate means
    x_mean = x.mean()
    y_mean = y.mean()
    
    # Center the data
    x_centered = x - x_mean
    y_centered = y - y_mean
    
    # Calculate the slope (beta_1)
    beta_1 = x_centered.dot(y_centered) / x_centered.pow(2).sum()
    
    return beta_1

def main():
    # read
    lazy_df = pl.scan_parquet("./nyc_cab_data/")

    # count
    count = lazy_df.select(pl.len())
    print(f"total count of data: {count.collect().item()}")
    print("-----------------------------\n")
    
    # valid data count
    valid_counts = lazy_df.pipe(filter_valid_year).select(pl.len())

    # as percentage
    percentage_valid = valid_counts.collect().item() / count.collect().item()
    print(f"percentage of valid data: {round(percentage_valid, 6)}")
    print("-----------------------------\n")
    
    # count of trips by year
    trips_by_year = lazy_df.pipe(filter_valid_year).group_by(pl.col("tpep_pickup_datetime").dt.year().alias("year")).agg(pl.len().alias("count")).sort("year")
    print("trips by year\n")
    print(trips_by_year.collect())
    print("-----------------------------\n")
    
    # average trips count by month across years
    trip_by_month = lazy_df.pipe(filter_valid_year).group_by(pl.col("tpep_pickup_datetime").dt.month().alias("month")).agg(pl.len().alias("count")).sort("month")
    print("trips by month\n")
    print(trip_by_month.collect())
    print("-----------------------------\n")
    
    # tip amount statistics
    tip_amount_stats = lazy_df.pipe(filter_valid_year).select(pl.col("tip_amount")).describe()
    print("tip statistics\n")
    print(tip_amount_stats)
    print("-----------------------------\n")

    # regression on fare amount by distance to work out cost increase by distance
    # trip_distance and fare_amount
    reg_coeff = {year: lazy_df.filter(pl.col("tpep_pickup_datetime").dt.year() == year).select(["trip_distance", "fare_amount"]).with_columns(coeff(pl.col("trip_distance"), pl.col("fare_amount")).alias("beta")).select(pl.col("beta")).limit(1).collect().item() for year in valid_years}
    print("regression coefficient\n")
    print(reg_coeff)
    print("-----------------------------\n")

if __name__ == "__main__":
    main()