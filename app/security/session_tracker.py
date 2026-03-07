# Simple in-memory session tracking

session_store = {}

def track_session(ip_address: str):
    if ip_address not in session_store:
        session_store[ip_address] = 0

    session_store[ip_address] += 1

    return session_store[ip_address]