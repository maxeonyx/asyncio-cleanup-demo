## What we want

**1. Shutdown.**

**2. Run as many cleanup handlers as possible.**

**3. Always shutdown before AWS shuts us down.**


<br/>
<br/>
<br/>
<br/>
<br/>

## Why our app might crash

**1. Unhandled `Exception`s**

**2. Shutdown requested via `SIGTERM`**

**3. Shutdown requested via `Ctrl`-`C` (`SIGINT`)**