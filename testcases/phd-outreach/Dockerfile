FROM python:3.12-slim

# The Claude Agent SDK wheel bundles the Claude Code CLI; no separate Node install is needed.
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Test-case content and harness. Each run gets a fresh workspace under /app/runs/<run>/workspace;
# the agent is denied read access to personas/, ground_truth/, environment/, harness/, prompts/.
COPY harness/ harness/
COPY prompts/ prompts/
COPY personas/ personas/
COPY ground_truth/ ground_truth/
COPY environment/ environment/
COPY study/ study/

# Run outputs are written to a mounted volume.
VOLUME ["/app/runs"]
ENTRYPOINT ["python", "-m", "harness.run"]
