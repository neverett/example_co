from dagster import Definitions, load_assets_from_modules

from .assets import etl  # noqa: TID252

all_assets = load_assets_from_modules([etl])

defs = Definitions(
    assets=all_assets,
)
