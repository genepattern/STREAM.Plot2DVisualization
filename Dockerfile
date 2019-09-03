FROM pinellolab/stream:0.3.8

RUN mkdir /stream
COPY viz2d_command_line.py /stream/viz2d_command_line.py

ENTRYPOINT []
