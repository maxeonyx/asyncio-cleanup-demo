## Graceful shutdown
### (How to clean up your shit asynchronously)

**I'm Max, I've been building Streaming APIs at the New Zealand Stock Exchange**

**Our apps now shut down gracefully in AWS Fargate.**

**I hope you learn something 😃**

<br/>
<br/>
<br/>
<br/>
<br/>


## What we want

**1. Shutdown.**

**2. Run as many cleanup handlers as possible.**

**3. Always shutdown before AWS shuts us down.**


<br/>
<br/>
<br/>
<br/>
<br/>
<br/>


## Why our app might crash

**1. `Exception`s which can't be handled.**

**2. `KeyboardInterrupt` (when running locally)**

**3. `SIGTERM` sent by AWS ECS Fargate**