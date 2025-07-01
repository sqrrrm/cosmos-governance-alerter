from prometheus_client import Counter

governance_votes_api_req_status_counter = Counter(
    "governance_votes_api_req_status",
    "Count the number of success or failed api call for a given network",
    ["name", "network", "api_endpoint", "status"],
)
