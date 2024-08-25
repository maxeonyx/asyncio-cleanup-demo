import asyncio
from functools import wraps

BOLD = "\033[1m"
BLACK = "\033[30m"
LIGHT_GRAY = "\033[37m"
RESET = "\033[0m"


async def ainput(prompt):
    return await asyncio.to_thread(input, prompt)


def curr_task_name():
    try:
        return asyncio.current_task().get_name()
    except Exception:
        return "main"


def name_task(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            task = asyncio.current_task()
            if task is not None:
                task.set_name(func.__name__)
        except Exception as e:
            print(f"failed to set name for {func.__name__}: {e}")
            pass
        return await func(*args, **kwargs)

    return wrapper


def log(*args, **kwargs):
    print(
        f"{BOLD}{curr_task_name()}: {' '.join(str(arg) for arg in args)}{RESET}",
        **kwargs,
        flush=True,
    )


def trace(*args, **kwargs):
    print(
        f"{LIGHT_GRAY}{curr_task_name()}: {' '.join(str(arg) for arg in args)}{RESET}",
        **kwargs,
        flush=True,
    )
