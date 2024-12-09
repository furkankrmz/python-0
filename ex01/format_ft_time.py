import time
from datetime import datetime

first_str = "Seconds since January 1, 1970:"

# Get current time in seconds since January 1, 1970
current_time = time.time()
frmttd_time = "{:,.4f}".format(current_time)

# Format the current time in scientific notation
scientific_time = "{:.4e}".format(current_time)

# Get current date in the required format
current_date = datetime.now().strftime("%b %d %Y")


print(first_str, frmttd_time, "or", scientific_time, "in scientific notation$")
print(current_date)
