"""
VoltGuard entry point.

Launches the physics-firewall dashboard, which continuously pulls
simulated packets and pipes them through:
    capture -> parser -> physics -> decision -> dashboard
"""

from dashboard.dashboard import run

if __name__ == "__main__":
    run()
