# create conntion to kafka
# pip install Git+git://github.com/mumrah/kafka-python
from kafka import SimpleClient, SimpleProducer, KafkaConsumer

from adl_lrs.settings import KAFKA_HOST

kafka = SimpleClient(KAFKA_HOST)


def productS():

    producer = SimpleProducer(kafka)
    return producer

def consumerC(topic):

    consumer = KafkaConsumer(kafka, "python", topic)
    return consumer

def close():
    kafka.close()
    exit()

{"verb": {"id": "http://adlnet.gov/expapi/verbs/launched", "display": {"fr-FR": "a lanc\u00e9", "de-DE": "startete", "en-US": "launched", "es-ES": "lanz\u00f3"}}, "version": "1.0.0", "timestamp": "2017-07-26T09:00:59.057301+00:00", "object": {"definition": {"name": {"en-US": "How to Make French Toast xapi-jqm Performance Support Demo: 04-video"}}, "id": "http://adlnet.gov/xapi/samples/xapi-jqm/ps/04-video", "objectType": "Activity"}, "actor": {"mbox": "mailto:297221517@qq.com", "name": "zsh1", "objectType": "Agent"}, "stored": "2017-07-26T09:00:59.057301+00:00", "authority": {"mbox": "mailto:297221517@qq.com", "objectType": "Agent", "name": "zsh"}, "context": {"contextActivities": {"parent": [{"definition": {"name": {"en-US": "How to Make French Toast xapi-jqm Performance Support Demo"}, "description": {"en-US": "A sample HTML5 mobile app with xAPI tracking that teaches you how to make french toast."}}, "id": "http://adlnet.gov/xapi/samples/xapi-jqm/ps/", "objectType": "Activity"}]}}, "id": "730d559d-5a99-45fa-9130-3cf2d36a1e19"}