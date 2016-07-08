import paho.mqtt.client as mqtt
import requests
import settings
base_url = 'http://%s:8080/sensor/%s?version=1.0&interval=minute&unit=watt'

mqttc = mqtt.Client()
mqttc.connect(settings.mqtt_host)
mqttc.loop_start()

total = 0

for sensor in settings.sensors:

  r = requests.get(base_url % (settings.flukso_host, sensor['id']))
  values = r.json()

  if not values:
    continue

  num = 0
  sum = 0

  for value in values[(settings.num_avg_values * -1):]:
    if value[1] == 'nan':
      continue

    num += 1
    sum += value[1]

  power = round(sum/num)
  mqttc.publish(settings.mqtt_base_topic + sensor['name'], power, retain=True)

  total += power

mqttc.publish(settings.mqtt_base_topic + 'total', power, retain=True)
mqttc.loop_stop()
mqttc.disconnect()
