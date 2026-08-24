def check_ticket_priority(fault_level):
    if fault_level >= 4:
        return "HIGH"
    elif fault_level >= 2:
        return "MEDIUM"
    else:
        return "LOW"