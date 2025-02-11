from datetime import datetime, timezone
from zoneinfo import ZoneInfo

arrival_nyc = "2024-03-10 03:31:18"
time_format = "%Y-%m-%d %H:%M:%S"
nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
# New York
eastern = ZoneInfo("US/Eastern")
nyc_dt = nyc_dt_naive.replace(tzinfo=eastern)
utc_dt = nyc_dt.astimezone(timezone.utc)
print("EDT:", nyc_dt)  # EDT: 2024-03-10 03:31:18-04:00
print("UTC:", utc_dt)  # UTC: 2024-03-10 07:31:18+00:00

# San Francisco
pacific = ZoneInfo("US/Pacific")
sf_dt = utc_dt.astimezone(pacific)
print("PST:", sf_dt)  # PST: 2024-03-09 23:31:18-08:00
