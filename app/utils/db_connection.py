import pandas as pd
import streamlit as st
import logging
from databricks import sql
from databricks.sdk.core import Config
from settings import DATABRICKS_WAREHOUSE_ID, PERSONAL_ACCESS_TOKEN

logger = logging.getLogger(__name__)

class DB_Query:
    """Repository class for handling queries."""
    
    @staticmethod
    @st.cache_data(ttl=3600, show_spinner="Executing query...")
    def sqlQuery(query: str) -> pd.DataFrame:
        """
        Executes a SQL query on a Databricks warehouse and returns the result as a pandas DataFrame.

        Parameters
        ----------
        query : str
            The SQL query to be executed.

        Returns
        -------
        pd.DataFrame
            The result of the SQL query as a pandas DataFrame.
        """
        cfg = Config() 
        with sql.connect(
            server_hostname=cfg.host,
            http_path=f"/sql/1.0/warehouses/{DATABRICKS_WAREHOUSE_ID}",
            # credentials_provider=lambda: cfg.authenticate,
            access_token=PERSONAL_ACCESS_TOKEN
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall_arrow().to_pandas()
                
    @staticmethod
    def get_query(query_template: str, **kwargs) -> pd.DataFrame:
        """
        Execute a query template with the given parameters.
        
        Parameters
        ----------
        query_template : str
            The SQL query template with placeholders
        **kwargs
            Variables to replace in the template
            
        Returns
        -------
        pd.DataFrame
            Query results
        """
        query = query_template.format(**kwargs)
        return DB_Query.sqlQuery(query)

# class ExpServiceError(Exception):
#     """
#     Custom exception for ExpService errors.

#     Attributes:
#         message (str): Description of the error.
#         errors (Any): Additional details about the error.
#     """
#     def __init__(self, message, errors):
#         super().__init__(message)
#         self.errors = errors

# class EmptyDataFrameError(Exception):
#     """
#     Custom exception for empty DataFrame errors.

#     Attributes:
#         message (str): Description of the error.
#         errors (Any): Additional details about the error.
#     """
#     def __init__(self, message, errors):
#         super().__init__(message)
#         self.errors = errors

# class Service:
#     @staticmethod
#     def get_exps_empty_df() -> pd.DataFrame:
#         """
#         Returns an empty DataFrame with the necessary columns to represent Exptions.

#         Returns
#         -------
#         pd.DataFrame
#             An empty DataFrame with the necessary columns to represent Exptions.
#         """
#         return pd.DataFrame(columns=ExpModel.schema()["properties"].keys())