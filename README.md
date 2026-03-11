# inverter sender

## Branch Description
This is the zero branch where development of the inverter sender happens.

## Future Work
This program may read command line data for setting the loglevel before the configuration file is read.

## Description
This daemon sends decoded inverter data onto the HAL network.

The division ratios prototyped in the inverter decoder are not applied: https://github.com/MAGLaboratory/inverter_decoder 

### Modbus Publishing
Each inverter frame is published onto the network under the `run` topic.

Each time the `reporter/checkup_req` is received, cached data is published under the `checkup` topic

## Dependencies
* [MAGLabPyLib](https://github.com/MAGLaboratory/MAGLabPyLib)  (included as a submodule)
* minimalmodbus

## Installation
(optional) Move files where appropriate:
* `MAGLabPyLib` may be installed using `pip install`
* `inverter.py` may be installed in `/usr/local/bin/`
* `inv_cfg.json` may be installed in `/etc/`
* `inverter.env` may be installed in the same location as the former

Modify the included `inverter_sender.service` to your installation:
* where the python script is
* where the .env file is
* which user is running this script

Copy the `inverter_sender.service` to `/usr/lib/systemd/system/` or where your distribution stores systemd scripts

## Help
Please do not hesitate to leave a Github issue or email the MAG Laboratory contact email: contact [at] maglaboratory [dot] org.
Our social media locations are on the website.

## Authors
* @blu006

## Version History
todo

## License
The Unlicense
