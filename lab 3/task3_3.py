def power_bill(units: int, slabs=((100, 1.5), (100, 2.5), (300, 4.0), (None, 6.0))) -> float:
    """Calculate electricity bill using slab rates in a few lines."""
    u, total = max(0, int(units)), 0.0
    for cap, rate in slabs:
        if u <= 0: break
        take = u if cap is None else min(u, cap)
        total += take * rate; u -= take
    return round(total, 2)


if __name__ == "__main__":
    print(power_bill(int(float(input("Units: ").strip() or 0))))


