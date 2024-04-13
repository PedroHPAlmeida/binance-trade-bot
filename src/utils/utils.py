from datetime import datetime, timezone, timedelta


def timestamp_ptbr() -> str:
    now_utc = datetime.now(timezone.utc)
    brasilia_timezone = timezone(timedelta(hours=-3))
    now_timezone_brasilia = now_utc.astimezone(brasilia_timezone)
    return now_timezone_brasilia.strftime('%d/%m/%Y %H:%M:%S')
