"""Agent Rate Limiter - Rate limiting for agent requests."""
import time
from collections import defaultdict
from typing import Dict

class AgentRateLimiter:
    def __init__(self, max_requests: int = 100, window: int = 60):
        self.max_requests = max_requests
        self.window = window
        self.requests: Dict[str, list] = defaultdict(list)
    
    def allow(self, agent_id: str) -> bool:
        now = time.time()
        self.requests[agent_id] = [t for t in self.requests[agent_id] if now - t < self.window]
        if len(self.requests[agent_id]) < self.max_requests:
            self.requests[agent_id].append(now)
            return True
        return False
    
    def get_remaining(self, agent_id: str) -> int:
        now = time.time()
        self.requests[agent_id] = [t for t in self.requests[agent_id] if now - t < self.window]
        return max(0, self.max_requests - len(self.requests[agent_id]))

__all__ = ["AgentRateLimiter"]
