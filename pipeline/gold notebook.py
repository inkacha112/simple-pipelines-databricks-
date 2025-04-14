# Databricks notebook source
# df.write.mode("overwrite").format("delta").saveAsTable("ctl_central_published.test_sc_dg_pg.sv_db_characters")

# COMMAND ----------

df = spark.read.parquet("/Volumes/ctl_central_published/test_sc_dg_pg/ext_vol_pg/sv_db_parquet/")

# COMMAND ----------

df.display()

# COMMAND ----------

#top 5 maxki on each race
from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number

window_spec = Window.partitionBy("race").orderBy(col("maxKI").desc())

df_ranked = df.withColumn("rank", row_number().over(window_spec))

# Filter top 5 per race
df_top5 = df_ranked.filter(col("rank") <= 5)

display(df_top5)
