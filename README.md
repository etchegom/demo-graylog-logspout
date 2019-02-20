
## Graylog stack demo with logspout

The docker stack contains the following services:
- a graylog server
- a mongodb database (for graylog config)
- an elasticsearch index
- a kibana dashboard
- a simple python app that generates some logs
- a logspout server in charge of collecting and sending the python app logs to graylog

#### How to run locally
- Run the docker stack
```
docker-compose up -d --build
```

- Login to [graylog](http://localhost:9000)
Using credentials admin/admin

- Setup a new GELF UDP input

- Set a JSON extractor to this input

#### Useful links

* https://github.com/gliderlabs/logspout
* https://github.com/micahhausler/logspout-gelf
* https://github.com/madzak/python-json-logger
* http://docs.graylog.org/en/2.5/pages/extractors.html#using-the-json-extractor
