#Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
#Oct 21 2022$
import time
from datetime import datetime

# Get current time in seconds since January 1, 1970
current_time = time.time()

# Format the current time in scientific notation
scientific_time = "{:.4e}".format(current_time)

# Get current date in the required format
current_date = datetime.now().strftime("%b %d %Y")


print("Seconds since January 1, 1970:", current_time, "or", scientific_time, "in scientific notation$")
print(current_date)