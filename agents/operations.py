class OperationsAgent:
    """
    Generates internal instructions for staff and logistics teams.
    Tone: calm, professional, precise.
    """

    def instruct(self, task):
        return (
            f"Operations Note: Please ensure {task} is handled with precision. "
            f"Maintain guest communication, timing, and courtesy at every step."
        )

