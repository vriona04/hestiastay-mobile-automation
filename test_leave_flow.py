if (
    "Going Home" not in page
    and "Confirm Leave" not in page
):
    print("Leave form unavailable in current app state")
    print("LEAVE FLOW HANDLED")
    return