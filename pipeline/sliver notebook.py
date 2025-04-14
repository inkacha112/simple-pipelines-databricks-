# Databricks notebook source
from datetime import datetime

current = datetime.now().strftime("%Y-%m-%d")

# COMMAND ----------

from pyspark.sql.functions import when, col

df = spark.read.option("multiline","true").json(f"/Volumes/ctl_central_published/test_sc_dg_pg/ext_vol_pg/{current}_db_all_characters.json")


# COMMAND ----------


df = df.drop(*["deletedAt", "description" , "image"])
df = df.withColumn(
    "race",
    when(col("race").contains("Nucleico"), "grind").otherwise(col("race"))
)


# COMMAND ----------

path = "/Volumes/ctl_central_published/test_sc_dg_pg/ext_vol_pg/sv_db_parquet/"

df.write.mode('overwrite').parquet(path)