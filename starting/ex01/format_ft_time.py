import time as ft_time

secs = ft_time.time()
int_part = int(secs)
frac_part = secs - int_part
formatted = f"{int_part:,}" + f"{frac_part:.5f}"[1:]

print("Seconds since January 1, 1970:", formatted,
      "or", format(secs, ".0e"), "in scientific notation")
print(ft_time.strftime("%b %d %Y", ft_time.localtime()))
