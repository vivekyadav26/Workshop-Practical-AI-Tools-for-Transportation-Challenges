# Autogenerate Markdown Summary
def write_summary(stats_dict):
    summary = f"""
    ## LRTP Summary

    - Total Vehicle Miles Traveled: {stats_dict['vmt']:,}
    - Total Delay (minutes): {stats_dict['delay_min']:,}
    - Average Trip Length: {stats_dict['avg_trip_length']:.2f} mi

    This scenario assumes {stats_dict['growth_scenario']} growth by 2050.
    """
    return summary