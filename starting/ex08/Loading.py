def ft_tqdm(lst: range) -> None:
    soft_colors = True
    bg_char = '-'
    tqdm_style = False

    total = len(lst)
    bar_len = max(10, 80 - 12)
    for i, item in enumerate(lst):
        idx = i + 1
        pct = int(idx * 100 / total)
        filled = int((idx) * bar_len / total)
        if soft_colors:
            if pct < 25:
                color = '\033[91m'
            elif pct < 50:
                color = '\033[38;5;208m'
            elif pct < 75:
                color = '\033[33m'
            else:
                color = '\033[92m'
        else:
            if pct < 25:
                color = '\033[31m'
            elif pct < 50:
                color = '\033[33m'
            elif pct < 75:
                color = '\033[33m'
            else:
                color = '\033[32m'
        reset = '\033[0m'

        if tqdm_style:
            filled_blocks = int((idx) * bar_len / total)
            if filled_blocks > 0:
                bar = '=' * (filled_blocks - 1)
                bar = bar.ljust(bar_len, '=')
            else:
                bar = ' ' * (bar_len - 1)
            left = f"{pct:3d}%|"
            counts = f" {idx}/{total}"
            line = f"\r{left}[{bar}]|{counts}"
        else:
            if filled <= 0:
                bar = bg_char * bar_len
            else:
                filled_blocks = max(0, filled - 1)
                filled_part = color + '█' * filled_blocks + reset
                head_part = color + '█' + reset
                rest_len = max(0, bar_len - filled_blocks - 1)
                rest_part = bg_char * rest_len
                bar = filled_part + head_part + rest_part
            left = f"{pct:3d}%|"
            counts = f" {idx}/{total}"
            counts_col = f"{color}{counts}{reset}"
            line = f"\r{left}[{bar}]|{counts_col}"
        try:
            print(line, end='', flush=True)
        except Exception:
            print(line, end='')
        yield item
    print()
