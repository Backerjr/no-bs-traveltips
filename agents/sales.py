class SalesAgent:
    """
    Calculates pricing, highlights savings, and adds charm to numbers.
    """

    def quote(self, name, official, exclusive):
        try:
            off = int(official.split()[0])
            exc = int(exclusive.split()[0])
            savings = off - exc
        except Exception:
            return f"{name}: Official {official} | Exclusive {exclusive}"

        return (
            f"• {name}: Official {official} | Exclusive {exclusive} "
            f"→ Save {savings} AED instantly with Ahmed’s rate."
        )

