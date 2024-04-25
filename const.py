"""
定义整个项目中的常量
"""


# login information
userID = "zxqh172"
password = "OiLFuJE95"

# time setting
START_DATE = "2019-06-31"
END_DATE = "2024-3-31"

# columns setting
PRICE_COLUMNS = 'open,high,low,close,avgPrice,changeRatio,volume,amount'

# path setting
PATH_DATABASES = "databases/{}"
PATH_BYX = PATH_DATABASES.format("byx.csv")
PATH_YY = PATH_DATABASES.format("yy.csv")
PATH_SL = PATH_DATABASES.format("sl.csv")

