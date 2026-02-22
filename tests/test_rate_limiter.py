import time

from src import AgentRateLimiter


def test_rate_limiter_blocks_after_limit():
    limiter = AgentRateLimiter(max_requests=2, window=60)
    assert limiter.allow("agent-1") is True
    assert limiter.allow("agent-1") is True
    assert limiter.allow("agent-1") is False


def test_remaining_resets_after_window():
    limiter = AgentRateLimiter(max_requests=1, window=1)
    assert limiter.allow("agent-2") is True
    assert limiter.get_remaining("agent-2") == 0
    time.sleep(1.1)
    assert limiter.get_remaining("agent-2") == 1
