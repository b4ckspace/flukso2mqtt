# flukso to mqtt

This script reads the sensor values from your flukso through HTTP and publishes the value on a given MQTT topic

## settings

You can adjust your settings in settings.py:

* num_avg_values - How many values to use for the average (default: 10)
* mqtt_host - Hostname of your mqtt broker
* mqtt_base_topic - MQTT topic under which the sensor values will be published
* flukso_host - Flukso hostname or IP address
* sensors - List of the name and ids of your sensor

You can grab the sensor ID (e.g. hash) from the flukso webinterface

