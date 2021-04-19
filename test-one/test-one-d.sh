#!/bin/bash
result1=$(sed "s/|url|/$RANDOM/" data.json);
echo $result1 > data.json;
result1=$(sed "s/|user|/$RANDOM/" data.json);
echo $result1 > data.json;