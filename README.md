# Governance Vote Alerter:

## Description
Cosmos Governance vote alerter

## Configuration

```bash
cp config.json.example config.json
```

Use your favorite editor and edit config.json

- under app_config :
  - `timeout` represent how long we should wait before the next vote checks
  - `votes_file` is the filename that stores all the on-going vote in all supported network
  - `format`: The format of the log messages. Can be `json` or `text`.
  - `level`: The log level. Can be `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`.
  - `default_pagination_limit`: The default number of proposal the program will fetch per request
  - `prometheus_port`: The port for the prometheus metrics
- under alerts_config
  - set to `true` the integration you would like to enable, and make sure to fill up the requirement information
- under chain_config and for each network :
  - `api_endpoint` is the governance api endpoint that list all the proposals
  - `network` is only used to provide more information in the alert
  - `explorer_governance` is the link without the proposal ID, ie program will add /<proposal ID>
  - `pagination_limit` is the number of proposal the program will fetch per request (optional, default is 100)

## Prometheus metrics

Prometheus metrics are available at http://localhost:<PROMETEHEUS_PORT>, PROMETEHEUS_PORT is the port from the app_config.prometheus_port

```bash
curl http://localhost:<PROMETEHEUS_PORT>
```
Example of metrics
```bash
governance_votes_api_req_status_total{api_endpoint="https://rest.cosmos.directory/haqq/cosmos/gov/v1beta1/proposals",name="haqq",network="mainnet",status="success"} 1.0
```
The status value can be success or failed

## TODO 
- [ ] Add a license




