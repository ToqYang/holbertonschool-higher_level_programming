#!/bin/bash
# cURL only methods 
curl -sLI 0.0.0.0:5000/route_4 | head -n4 | tail -n 1 | cut -d " " -f2-
