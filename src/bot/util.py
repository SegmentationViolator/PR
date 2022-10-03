from typing import NoReturn

MAX_API_CALLS: int = 960
TOTAL_TIME = 60*60*24 # seconds

def calculate_interval(role_count: int) -> float:
    iterations = MAX_API_CALLS / role_count
    return TOTAL_TIME/iterations

def report(execption: Exception) -> NoReturn:
    raise execption