* https://github.com/gliderlabs/logspout
* https://github.com/micahhausler/logspout-gelf

```
docker run --rm \
--log-driver gelf \
--log-opt gelf-address=udp://am-graylog-test.allo-media.tech:12201 \
alpine echo hello world
```