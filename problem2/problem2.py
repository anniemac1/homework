def date_format(date_str):
    parts = date_str.split('/')
    year = parts[2]
    month = parts[0].zfill(2)
    day = parts[1].zfill(2)
    return f"{year}-{month}-{day}"