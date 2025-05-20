GET_KIDS = """
    SELECT
        *
    FROM hive_metastore.{schema}.{table}{country}
"""