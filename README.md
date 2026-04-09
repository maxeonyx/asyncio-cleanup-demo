## asyncio cleanup demo

Demo code and slide materials from a talk about graceful async shutdown in Python's `asyncio`.

This repo walks through progressively better approaches to shutdown and cleanup, from basic `try`/`finally` handling through signal handling, `TaskGroup`, and a custom `asyncio.run` wrapper with a timeout.

These are presentation materials, not a library.

Requires Python 3.11+ because the examples use `asyncio.TaskGroup`.
