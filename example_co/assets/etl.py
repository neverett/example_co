import dagster as dg

# raw data assets
@dg.asset(
    kinds={"parquet"},
    group_name="sensitive_data",
    tags={"private":''},
    owners=["ada.dagster@example.com", "team:data_eng"],
    key_prefix="my_prefix"
)
def raw_data_a() -> None:
    pass

@dg.asset(
    kinds={"parquet"},
    owners=["ada.dagster@example.com", "team:data_eng"],
    group_name="sensitive_data",
    tags={"private":''},
)
def raw_data_b() -> None:
    pass

@dg.asset(
    group_name="sensitive_data",
    tags={"private":''},
    kinds={"s3"},
    owners=["ada.dagster@example.com", "team:data_eng"],
)
def raw_data_c() -> None:
    pass

# cleaned data assets

@dg.asset(
    deps=[dg.AssetKey(["my_prefix", "raw_data_a"])],
    group_name="public_data",
    kinds={"postgres", "polars"},
    owners=["team:data_eng"],
    tags={"public":''}
)
def cleaned_data_a() -> None:
    pass

@dg.asset(
    deps=["raw_data_b"],
    group_name="public_data",
    kinds={"postgres", "polars"},
    owners=["team:data_eng"],
    tags={'public':''}
)
def cleaned_data_b() -> None:
    pass

@dg.asset(
    deps=["raw_data_c"],
    group_name="public_data",
    kinds={"postgres", "polars"},
    owners=["team:data_eng"],
    tags={'public':''}
)
def cleaned_data_c() -> None:
    pass

# combo assets

@dg.asset(
    deps=[
        "cleaned_data_a",
        "cleaned_data_b",
        "cleaned_data_c"
    ],
    group_name="public_data",
    kinds={"postgres"},
    tags={'public':''},
    owners=["john.dagster@example.com", "team:data_eng"],
)
def combo_a_b_c_data() -> None:
    pass

@dg.asset(
    deps=[
        "cleaned_data_b",
        "cleaned_data_c"
    ],
    group_name="public_data",
    kinds={"postgres"},
    tags={'public':''},
    owners=["john.dagster@example.com", "team:data_eng"],
)
def combo_b_c_data() -> None:
    pass

# summary stats assets

@dg.asset(
    deps=[
        "combo_a_b_c_data"
    ],
    group_name="public_data",
    kinds={"powerbi"},
    owners=["team:analysts"],
    tags={'public':''}
)
def summary_stats_1() -> None:
    pass

@dg.asset(
    deps=[
        "combo_b_c_data"
    ],
    kinds={"powerbi"},
    owners=["team:analysts"],
    group_name="public_data",
    tags={'public':''}
)
def summary_stats_2() -> None:
    pass

# assets for sales

@dg.asset(
    deps=[
        "combo_a_b_c_data"
    ],
    owners=["team:sales"],
    group_name="public_data",
    tags={'public':''},
    kinds={"csv"}
)
def a_b_c_for_sales() -> None:
    pass

@dg.asset(
    deps=[
        "combo_b_c_data"
    ],
    owners=["team:sales"],
    group_name="public_data",
    kinds={"csv"},
    tags={'public':''}
)
def b_c_for_sales() -> None:
    pass