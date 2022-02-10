def update_bounds(bounds, estimate, value):
    if value >= bounds["low"]:
        bounds["low"] = value
    if value <= estimate:
        bounds["high"] = estimate

    return bounds
